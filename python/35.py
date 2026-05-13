items = ["Laptop", "Mouse", "Keyboard"]
stock_count = [10, 50, 20]
print(f" total stock in warehouse {sum(stock_count)}")
print(f"highest number in stock {max(stock_count)}")
warehouse=(items+stock_count)
print(f'is laptop in items?{"Laptop" in (items)}')
stock_count.sort()
print(f"sorted stock count:{stock_count}")
print(stock_count)