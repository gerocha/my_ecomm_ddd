from my_ecomm.application.services.user import UserService


class UserModel:

    def __init__(self):
        self.db = []

    def __len__(self):
        return len(self.db)

    def add(self, user):
        self.db.append(user)


class TestUserService:

    def test_user_create(self):
        model = UserModel()
        service = UserService(user_model=model)

        service.create({'name': 'batima da silva',
                        'password': '123456',
                        'email': 'teste@teste.com'})

        assert len(model) == 1
