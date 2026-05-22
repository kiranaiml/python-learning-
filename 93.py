#THE ECO-MODERN CLIMATE ENGINE
class smartclimatehub:
    def __init__(self,zone_name):
        self.zone_name=zone_name
        self.__temperature=24
    def get_temperature(self):
        return self.__temperature
    def set_temperature(self,new_temp):
        if new_temp<18:
            self.__temperature=18
            print(f"Too cold for timber! snapping to 18˙C.")
        elif new_temp>28:
            print(f"Too hot for indoor greenhouse! Snapping to 28 c.")
        else:
            print(f"Temperature set to {new_temp}C.")
    def adjust_glass(self,tint_level=None):
        self.tint_level=tint_level
        if tint_level==None:
            print(f"🪟 No tint specified. Deployed standard timber blinds.")
        else:
            print(f"🕶️ Smart glass tint level set to : {tint_level}%")
living_room=smartclimatehub("Main Atrium")
living_room.set_temperature(15)
print(f"Current Temp is: {living_room.get_temperature()}C")
living_room.adjust_glass()
living_room.adjust_glass(85)