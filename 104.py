# 1. THE DATA HOLDER (Only handles data)
class PortfolioProject:
    def __init__(self, title, description):
        self.title = title
        self.description = description

# 2. THE UI WORKER (Noun class, Verb method)
class HtmlGenerator:
    # We pass the 'project' object into the method
    def generate_card(self, project):
        # We use project.title, NOT self.title!
        print(f"<div class='card'><h2>{project.title}</h2><p>{project.description}</p></div>")

# 3. THE STORAGE WORKER
class DatabaseSaver:
    def save_user(self, project):
        print(f"Connecting... Saving '{project.title}' to the database.")

# 4. THE EMAIL WORKER
class EmailService:
    def send_admin_alert(self, project):
        print(f"Emailing admin: A new project called '{project.title}' was just added!")


# --- 🎬 The Execution Block ---
if __name__ == "__main__":
    # 1. Create the project data
    my_project = PortfolioProject("Eco-Modern Climate Engine", "A backend Python architecture project.")
    
    # 2. Hire the specialized workers
    html_worker = HtmlGenerator()
    db_worker = DatabaseSaver()
    email_worker = EmailService()
    
    # 3. Put them to work!
    print("--- Running Portfolio Engine ---")
    html_worker.generate_card(my_project)
    db_worker.save_user(my_project)
    email_worker.send_admin_alert(my_project)