party_info=("may 15th","Retro Night")
invited={"Hassan","Alice","Bob","charlie"}
showed_up={"Hassan","Charlie"}
absent=invited-showed_up
showed_up.add("zeo")
everyone=invited|showed_up
print(everyone)