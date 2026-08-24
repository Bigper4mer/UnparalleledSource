from repository import UserRepository


class UserService:
    def __init__(self, repository: UserRepository | None = None) -> None:
        self.repository = repository or UserRepository()

    def get_user_name(self, user_id: int) -> str:
        return self.repository.get_user(user_id)["name"]
