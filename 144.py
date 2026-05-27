#The Core Banking Engine
import json
class BankEngine:
    def __init__(self,user_name):
        self.filename="bank.db.json"
        self.user_name=user_name
         
        try:
            with open(self.filename,"r") as file:
                self.database = json.load(file) 
        except Exception as e:
            self.database={}
    def log_transaction(self, message):
        log_file = "audit_log.txt"

        try:
            with open(log_file, "a") as file:
                file.write(message + "\n")
        except Exception as e:
            print(f"ERROR writing to log: {e}")
    
    def transfer_funds(self, sender, receiver, amount):
        print(f"\n--- Initiating Transfer: {amount} from {sender} to {receiver} ---")
        try:
            self.database[sender] = self.database[sender] - amount
            self.database[receiver] = self.database[receiver] + amount
            
        except KeyError:
            print("ERROR: One of those names doesn't exist in the database.")
        except TypeError:
            print("ERROR: You must use numbers for the amount, not text.")
        else:
            print("SUCCESS: Your transaction is complete.")
        finally:
            self.log_transaction(f"Transfer attempted: {amount} from {sender} to {receiver}")
    def save_system(self):
        with open (self.filename,"w") as file:
            self.database=json.dump(self.database,file)
my_bank = BankEngine("Kiran")
my_bank.database["Kiran"] = 1000
my_bank.database["Ajay"] = 500
my_bank.transfer_funds("Kiran", "Ajay", 200)
my_bank.transfer_funds("Kiran", "Ajay", "Fifty")
my_bank.transfer_funds("Kiran", "UnknownHacker", 100)
my_bank.save_system()