class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        if user not in self.users:
            self.users.append(user)
        else:
            return "User already exists!"  # OK

    def remove_user(self, user):
        if user in self.users:  # OK: Verificando se o usuário existe antes de tentar removê-lo.
            self.users.remove(user)
        else:
            return "User not found!"
