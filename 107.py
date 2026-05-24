from abc import ABC, abstractmethod

# 1. Specific Contract A (Only for working)
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

# 2. Specific Contract B (Only for eating)
class Eatable(ABC):
    @abstractmethod
    def eat_lunch(self):
        pass

# 3. The Human (Signs BOTH contracts)
class Human(Workable, Eatable):
    def work(self):
        print("👤 Writing Python code.")
        
    def eat_lunch(self):
        print("🥪 Eating a sandwich in the breakroom.")

# 4. The Robot (Only signs the Work contract!)
class Robot(Workable):
    def work(self):
        print("🤖 Vacuuming the office floors.")
    
    # Notice: The Robot completely ignores eat_lunch() and Python does not crash!


# --- 🎬 The Execution Block ---
if __name__ == "__main__":
    kiran_the_dev = Human()
    auto_cleaner = Robot()

    print("--- Office Work Time ---")
    # Both of them signed the Workable contract, so they both can work.
    kiran_the_dev.work()
    auto_cleaner.work()

    print("\n--- Office Lunch Time ---")
    # Only the human signed the Eatable contract!
    kiran_the_dev.eat_lunch()
    # We don't even ask the robot to eat, because it never signed the contract.