#Solo Challenge
hassan_data=("Hassan","Karnataka","1952")
temples={"Belur","Halebidu","Gorur"}
print(f"Temples in hassan; {temples}")
visited={"Gorur","Shettihalli"}
print(f"You visited this place:{visited}")
all_places=temples|visited
print(f"Hassan major place:{all_places}")
missing=temples.difference(visited)
print(missing)
print(hassan_data[1])
