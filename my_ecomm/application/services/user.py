from my_ecomm.application.entity.user import User
from my_ecomm.repository.dao.interfaces.user import IUserDao


class UserService(object):
    user_model: IUserDao = None
    user_entity: User = None

    def __init__(self, user_model: IUserDao):
        self.user_model = user_model

    def create(self, user: User):
        self.user_entity = user
        self.user_model.add(user=user)
