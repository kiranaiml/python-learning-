# The Database Migration Engine
master_list=[]
while True:
    record=input("Enter the record ID : ")
    data_base=input("Enter the database name : ")
    if data_base=="corrupt" or data_base=="null":
        print("Data unreadable.Skipping...")
        continue
    elif data_base=="migrate":
        print("Commencing final migration...")
        break
    else:
        master_list.append((record, data_base))
print(f"\nFinal list is: {master_list}")
