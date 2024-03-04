from app.database.model.user import User

from app.database.repository.abc import DAO


class UserDAO(DAO):

    def save_user(self, user: User) -> None:
        self.session.add(user)
        self.session.commit()
