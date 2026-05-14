#"The Classroom"
classroom=("Room 101","Science","40")
moring_class={"Umesh","Ali","Ahmed"}
afternoon_class={"Sara","John","Ahmed"}
both_class=moring_class & afternoon_class
print(both_class)
both=moring_class.difference( afternoon_class)

print(both)
afternoon_class.add("Zeo")
