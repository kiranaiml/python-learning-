#The CLI Issue Tracker
import json
class Issuetracker:
    def __init__(self):
        self.jsonfile="tracker.db.json"
        
        try:
            with open(self.jsonfile,"a") as file:
                self.tickets=json.load(file)
        except :
            self.tickets={}
    def create_ticket(self,ticket_id, title, assignee):
        self.tickets[ticket_id] = {"title": title, "assignee": assignee, "status": "OPEN"}
        self.save_db()
        
    def update_status(self,ticket_id,new_status):
        try:
            self.tickets[ticket_id]["status"] = new_status
        except KeyError:
            print(" Warning⚠️!! ticket that doesn't exist")
        else:
            print(f" Your Ticket ID : {ticket_id}\n Ticket status : {new_status}")
        finally:
         self.save_db()
    def save_db(self):
        with open (self.jsonfile,"w") as file:
            json.dump(self.jsonfile,file)
    def view_board(self):
        with open(self.jsonfile,"r") as file:
            for ticket_id, info in self.tickets.items():
               print(f"[{ticket_id}] {info['title']} | Assignee: {info['assignee']} | Status: {info['status']}")
my_tracker = Issuetracker()
my_tracker.create_ticket("TASK-1", "Fix login bug", "Kiran")
my_tracker.create_ticket("TASK-2", "Update database", "Ajay")
my_tracker.update_status("TASK-1", "IN_PROGRESS")
my_tracker.update_status("TASK-99", "CLOSED")
print("\n--- LIVE KANBAN BOARD ---")
my_tracker.view_board()