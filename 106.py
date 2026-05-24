#learning lsp Q2
# The Master Blueprint
class FileStorage:
    def save_data(self, data):
        pass
        
    def get_local_path(self):
        pass

# The Hard Drive (Works perfectly)
class LocalDiskStorage(FileStorage):
    def save_data(self, data):
        print("Saving data to the C: Drive.")
        
    def get_local_path(self):
        return "/local/backups/data.json"

# The Cloud Server (The System Crasher!)
class AwsCloudStorage(FileStorage):
    def save_data(self, data):
        print("Uploading data to AWS S3 Cloud.")
        
    def get_local_path(self):
        # Cloud servers don't have local computer paths! 
        # This breaks the parent's rule and crashes the app.
        raise Exception("Error: Cloud storage does not have a local file path!")
if __name__ == "__main__":
    my_hard_drive = LocalDiskStorage()
    my_cloud = AwsCloudStorage()

    # Create a list of our different storage devices
    all_storage_systems = [my_hard_drive, my_cloud]

    print("--- Running Global Backup ---")
    # We can safely loop through EVERY storage system and save data without crashing!
    for system in all_storage_systems:
        system.save_data("User_Portfolio_Data")

    print("\n--- Requesting Local File Path ---")
    # If a system specifically needs a path, it ONLY asks the LocalDiskStorage
    path = my_hard_drive.get_local_path()
    print(f"Path found: {path}")