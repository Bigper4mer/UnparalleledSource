from service import UserService


def build_service() -> UserService:
    return UserService()


def main() -> str:
    service = build_service()
    return service.get_user_name(1)
