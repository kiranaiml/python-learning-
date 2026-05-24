#The Liskov Substitution Principle (LSP)
#1.Learnig lsp
class Bird:
    def move(self):
        pass
class flylingbrid(Bird):
    def move(self):
        pass
class swimmingbird(Bird):
    def move(self):
        pass
class eagle(flylingbrid):
    def move(self):
        print("🦅 The eagle flies forward.")
    def fly(self):
        print("Soaring high in the sky!")
class penguin(swimmingbird):
    def move(self):
        print("🐧 The penguin waddles forward on the ice.")
    def swim(self):
        print("Swimming through the freezing water!")
if __name__ == "__main__":
    my_eagle = eagle()
    my_penguin = penguin()

    print("--- Moving all birds ---")
    my_eagle.move()
    my_penguin.move() 

    print("\n--- Specific Actions ---")
    my_penguin.swim()
    my_eagle.fly()