# The free fire weapon Engine
class weapon:
    def __init__(self,gun_name,ammo=30):
        self.gun_name=gun_name
        self.ammo=ammo
    def shoot(self):
        print(f"Firing the {self.gun_name}! bullets loaded: {self.ammo}")
gun1=weapon("AK47")
gun2=weapon("MP40",ammo=100)
gun1.shoot()
gun2.shoot()
