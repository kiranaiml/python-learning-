#The Stock Market Scanner
prices=[120,45,250,30,88]
for p in prices:
    if p>100:
        print(f"High value stock datected:{p} ")
    else:
        print(f"Regular stock logged:{p}")
print(f"\nMarket scan completed.")