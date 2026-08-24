class UserRepository:
    def __init__(self) -> None:
        self._users = {1: {"id": 1, "name": "Ada"}}

    def get_user(self, user_id: int) -> dict[str, object]:
        return self._users[user_id]
