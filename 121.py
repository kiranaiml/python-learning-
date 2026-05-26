# --- 1. THE SUBSCRIBER BLUEPRINT (Interface) ---
# Anyone who wants to listen to the RideTracker must follow this rule.
class Subscriber:
    def update(self, destination):
        pass

# --- 2. THE SPECIFIC SUBSCRIBERS (The Listeners) ---
# These classes don't know about each other. They just do their own jobs.

class DatabaseLogger(Subscriber):
    def update(self, destination):
        print("  saving the destination to the database")
        pass

class SMSNotifier(Subscriber):
    def update(self, destination):
        print( "texting amma and papa about the safe arrival")
        pass

class VideoProcessor(Subscriber):
    def update(self, destination):
        print( "starting the Techno Reel render")
        pass


# --- 3. THE PUBLISHER (The Megaphone) ---
# This class doesn't do the jobs anymore. It just shouts that the ride is done.

class RideTracker:
    def __init__(self):
        self.susbricers=[]
        pass

    def attach(self, subscriber):
        self.susbricers.append(subscriber)
        # TODO: Append the passed `subscriber` to your `self.subscribers` list
        pass

    def finish_ride(self, destination):
        print(f"\n--- Ride to {destination} Completed! ---")
        print("Broadcasting to all systems...\n")
        for every_suscribers in self.susbricers:
            every_suscribers.update(destination)
        # TODO: Loop through your `self.subscribers` list. 
        # For every subscriber in the list, call their `.update(destination)` method!
        pass


# --- 4. EXECUTION (Wiring it up) ---

# 1. Create your publisher
my_tracker = RideTracker()

# 2. Create your listeners
db = DatabaseLogger()
sms = SMSNotifier()
video = VideoProcessor()

# 3. TODO: Use the `attach()` method to add `db`, `sms`, and `video` to the tracker.
my_tracker.attach(db)
my_tracker.attach(sms)
my_tracker.attach(video)
# 4. Finish the ride and watch the magic happen!
my_tracker.finish_ride("Sakleshpura")