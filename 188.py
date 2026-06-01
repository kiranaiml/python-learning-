# ---------------------------------------------------------
# THE RAW SYSTEM CHALLENGE: THE LOGIN PORTAL
# ---------------------------------------------------------
# 
# BUSINESS NEED:
# You are building the backend for a web portfolio's login page. 
# You need a custom object that stores a visitor's profile and 
# tracks exactly how many times they have logged in.
# 
# SYSTEM REQUIREMENTS:
# 1. Create a class named `UserAccount`.
# 2. In the setup engine (`__init__`), accept `username` and `email`.
#    Save them to the object.
# 3. INSIDE the setup engine, create a THIRD variable called 
#    `self.login_count` and permanently set it to 0. (Do not put 
#    this in the parentheses at the top!)
# 4. Create a method called `record_login(self)`. 
#    Inside it, add 1 to the object's `login_count`.
# 5. Outside the class, build a new object for a user with the 
#    username "kiran_dev" and an email of "admin@portal.com".
# 6. Call your login method EXACTLY THREE times in a row.
# 7. Print all three pieces of data (username, email, and the 
#    final login count) on separate lines using DOT NOTATION.
# 
# EXPECTED OUTPUT:
# Username: kiran_dev
# Email: admin@portal.com
# Total Logins: 3
# ---------------------------------------------------------
class useraccount:
    def __init__(self,username,email):
        self.username=username
        self.email=email
        self.login_count=0
    def record_login(self):
        self.login_count+=1
my_data=useraccount("Kiran backend","admin@portal.com")
my_data.record_login()
my_data.record_login()
my_data.record_login()
print(f"Username : {my_data.username}\nEmail: {my_data.email}\nTotal logins: {my_data.login_count}")