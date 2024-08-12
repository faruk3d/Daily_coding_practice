class User:
    def __init__(self, user_id, username) -> None:
        self.user_id = user_id
        self.username = username
        self.followers = 0


user_1 = User("001", "wololo")
print(user_1.username)
print(user_1.user_id)