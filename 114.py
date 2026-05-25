from abc import ABC, abstractmethod

# ==========================================
# ❌ THE BROKEN SYSTEM (Violates DIP)
# ==========================================
class keyboard(ABC):
    @abstractmethod
    def type_key(self):
        pass
class CheapKeyboard(keyboard):
    @abstractmethod
    def type_keys(self):
        print("Typing softly... mush mush.")
class mechanicalkeyboard(keyboard):
    @abstractmethod
    def type_key(self):
        print("click clack")

class Computer:
    def __init__(self,keyboard):
        # DIP Violation: The computer is permanently glued to one specific keyboard!
        self.keyboard = CheapKeyboard() 

    def write_code(self):
        print("Booting up VS Code...")
        self.keyboard.type_keys()

# If we try to use it:
my_pc = Computer()
my_pc.write_code()