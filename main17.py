class User: 
    def __init__(self,user_id, username):
        self.id = user_id
        self.username = username
        self.follower = 0
        self.following = 0  #default value
    
    def follow(self):
        user.follower += 1
        self.following += 1





user_1 = User("001","jenny")
print(user_1)

print(user_1.username)