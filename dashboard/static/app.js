const elements = {
  live: document.querySelector('.live-run'),
  heading: document.querySelector('#live-heading'),
  task: document.querySelector('#task-name'),
  phase: document.querySelector('#run-phase'),
  elapsed: document.querySelector('#elapsed'),
  heartbeat: document.querySelector('#heartbeat'),
  runId: document.querySelector('#run-id'),
  summary: document.querySelector('#activity-summary'),
  fill: document.querySelector('#activity-fill'),
  pulse: document.querySelector('#activity-pulse'),
  runsBody: document.querySelector('#runs-body'),
  runsEmpty: document.querySelector('#runs-empty'),
  runCount: document.querySelector('#run-count'),
  approvals: document.querySelector('#approvals-list'),
  approvalsEmpty: document.querySelector('#approvals-empty'),
  approvalCount: document.querySelector('#approval-count'),
  connectors: document.querySelector('#connectors-list'),
  system: document.querySelector('.system-health'),
  systemLabel: document.querySelector('#system-label'),
  refreshed: document.querySelector('#last-refresh'),
  toast: document.querySelector('#toast'),
};

let state = null;
let sessionToken = '';

const statusLabels = {
  idle: 'IDLE',
  running: 'RUNNING',
  waiting_approval: 'WAITING APPROVAL',
  completed: 'COMPLETED',
  failed: 'FAILED',
  offline: 'OFFLINE',
};

function parseDate(value) {
  return value ? new Date(value) : null;
}

function relativeTime(value) {
  const date = parseDate(value);
  if (!date || Number.isNaN(date.valueOf())) return 'Not reported';
  const seconds = Math.max(0, Math.floor((Date.now() - date.valueOf()) / 1000));
  if (seconds < 5) return 'Just now';
  if (seconds < 60) return `${seconds}s ago`;
  const minutes = Math.floor(seconds / 60);
  if (minutes < 60) return `${minutes}m ago`;
  return `${Math.floor(minutes / 60)}h ago`;
}

function duration(seconds) {
  if (seconds === null || seconds === undefined) return '—';
  const total = Math.max(0, Math.floor(seconds));
  const hours = Math.floor(total / 3600);
  const minutes = Math.floor((total % 3600) / 60);
  const secs = total % 60;
  return [hours, minutes, secs].map(value => String(value).padStart(2, '0')).join(':');
}

function elapsed(run) {
  if (!run) return '—';
  if (run.duration_seconds !== null) return duration(run.duration_seconds);
  const started = parseDate(run.started_at);
  return started ? duration((Date.now() - started.valueOf()) / 1000) : '—';
}

function safeText(value) {
  return String(value ?? '').replace(/[&<>'"]/g, character => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', "'": '&#39;', '"': '&quot;',
  })[character]);
}

function deriveLiveRun(data) {
  const active = data.runs.find(run => run.id === data.active_run_id);
  if (active) return active;
  return data.runs[0] || null;
}

function effectiveStatus(run) {
  if (!run) return 'offline';
  if (run.status === 'running') {
    const heartbeat = parseDate(run.last_heartbeat_at);
    if (heartbeat && Date.now() - heartbeat.valueOf() > 30000) return 'offline';
  }
  return run.status;
}

function renderLive(data) {
  const run = deriveLiveRun(data);
  const status = effectiveStatus(run);
  elements.live.className = `live-run status-${status}`;
  elements.heading.textContent = statusLabels[status] || status.toUpperCase();
  elements.task.textContent = run?.task || 'No HiveForge run has been recorded';
  elements.phase.textContent = run?.phase || 'Ready for instrumentation';
  elements.elapsed.textContent = elapsed(run);
  elements.heartbeat.textContent = run ? relativeTime(run.last_heartbeat_at) : '—';
  elements.runId.textContent = run?.id || '—';
  const latestEvent = run?.events?.at(-1);
  elements.summary.textContent = latestEvent?.summary || run?.summary || 'Waiting for a run';
  const eventCount = run?.events?.length || 0;
  const percent = status === 'completed' ? 100 : status === 'failed' ? 100 : Math.min(88, 14 + eventCount * 9);
  elements.fill.style.width = `${percent}%`;
  elements.pulse.style.left = `calc(${percent}% - 6px)`;
}

function renderRuns(data) {
  const runs = data.runs.slice(0, 8);
  elements.runCount.textContent = `${data.runs.length} recorded`;
  elements.runsEmpty.hidden = runs.length > 0;
  elements.runsBody.innerHTML = runs.map(run => `
    <tr>
      <td><span class="status-chip ${safeText(run.status)}">${safeText(statusLabels[run.status] || run.status)}</span></td>
      <td title="${safeText(run.task)}">${safeText(run.task)}</td>
      <td>${parseDate(run.started_at)?.toLocaleString([], {month:'short', day:'numeric', hour:'numeric', minute:'2-digit'}) || '—'}</td>
      <td>${elapsed(run)}</td>
    </tr>
  `).join('');
}

function renderApprovals(data) {
  const pending = data.approvals.filter(item => item.status === 'pending');
  elements.approvalCount.textContent = `${pending.length} pending`;
  elements.approvalsEmpty.hidden = pending.length > 0;
  elements.approvals.innerHTML = pending.map(item => `
    <div class="list-row">
      <div class="list-copy"><strong>${safeText(item.title)}</strong><span>${safeText(item.details || `Run ${item.run_id}`)}</span></div>
      <div class="actions">
        <button class="approve" data-approval="${safeText(item.id)}" data-decision="approve">Approve</button>
        <button class="deny" data-approval="${safeText(item.id)}" data-decision="deny">Deny</button>
      </div>
    </div>
  `).join('');
}

function renderConnectors(data) {
  elements.connectors.innerHTML = data.connectors.map(connector => `
    <div class="list-row">
      <div class="list-copy"><strong>${safeText(connector.name)}</strong><span>Checked ${relativeTime(connector.checked_at)}</span></div>
      <span class="connector-state ${safeText(connector.status)}">${safeText(connector.status)}</span>
    </div>
  `).join('');
}

function renderSystem(data) {
  const run = deriveLiveRun(data);
  const status = effectiveStatus(run);
  const connected = data.connectors.filter(item => item.status === 'connected').length;
  elements.system.className = `system-health ${status === 'failed' ? 'bad' : status === 'waiting_approval' ? 'warn' : 'good'}`;
  if (status === 'running') elements.systemLabel.textContent = 'Agent is running';
  else if (status === 'waiting_approval') elements.systemLabel.textContent = 'Operator decision required';
  else if (status === 'failed') elements.systemLabel.textContent = 'Latest run failed';
  else elements.systemLabel.textContent = `${connected}/${data.connectors.length} connectors reporting connected`;
  elements.refreshed.textContent = `State refreshed ${new Date().toLocaleTimeString()}`;
}

function render(data) {
  state = data;
  sessionToken = data.session_token || sessionToken;
  renderLive(data);
  renderRuns(data);
  renderApprovals(data);
  renderConnectors(data);
  renderSystem(data);
}

function showToast(message) {
  elements.toast.textContent = message;
  elements.toast.classList.add('visible');
  window.setTimeout(() => elements.toast.classList.remove('visible'), 2600);
}

async function refresh() {
  try {
    const response = await fetch('/api/state', {cache: 'no-store'});
    if (!response.ok) throw new Error(`State request failed: ${response.status}`);
    render(await response.json());
  } catch (error) {
    elements.system.className = 'system-health bad';
    elements.systemLabel.textContent = 'Dashboard disconnected';
  }
}

async function decide(approvalId, decision) {
  const response = await fetch(`/api/approvals/${encodeURIComponent(approvalId)}`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json', 'X-HiveForge-Token': sessionToken},
    body: JSON.stringify({decision}),
  });
  const result = await response.json();
  if (!response.ok) throw new Error(result.error || 'Decision failed');
  showToast(decision === 'approve' ? 'Run approved and resumed' : 'Run denied and stopped');
  await refresh();
}

document.addEventListener('click', event => {
  const button = event.target.closest('[data-approval]');
  if (!button) return;
  button.disabled = true;
  decide(button.dataset.approval, button.dataset.decision).catch(error => {
    showToast(error.message);
    button.disabled = false;
  });
});

refresh();
window.setInterval(refresh, 2000);
window.setInterval(() => state && renderLive(state), 1000);
