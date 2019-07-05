from domain.entity.user import User as UserEntity


class User:
    @classmethod
    def create(self, user: Dict) -> UserEntity:
        return UserEntity(**user)
