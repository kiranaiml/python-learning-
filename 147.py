#The Auth Engine
import json
class authengine:
    def __init__(self):
        self.filename="users_db_json"
        try:
            with open(self.filename,"r") as file:
                self.user=json.load(file)
        except:
            self.user={}
    def register(self,username,passward):
        if username in self.user:
            print("Username already exsists!")
        else:
            self.user[username]=passward
        self.save_db()
    def login(self,username,passward):
        try:
             stored_password = self.user[username]
        except KeyError:
            print("Account not found.")
        else:
            if stored_password==passward:
                print("Access Granted!")
            else:
                print("Access Denied: Wrong Password.")
    def save_db(self):
        with open(self.filename,"w") as file:
            json.dump(self.user,file)


my_auth = authengine()
print("\n--- 📝 REGISTRATION ---")
my_auth.register("Kiran", "SecurePass123")
my_auth.register("Kiran", "HackerPass999")

print("\n--- 🔐 LOGIN ATTEMPTS ---")
my_auth.login("Kiran", "SecurePass123")
my_auth.login("Kiran", "WrongPass456")
my_auth.login("GhostUser", "GhostPass")
