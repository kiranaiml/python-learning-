#the Token Generator
department_code = input("Enter Department Code: ")
tokens = int(input("How many tokens to generate? "))
print()
for i in range(tokens):
    print(f"Token generated: {department_code}_{i + 1}")
print(f"\nSystem shutdown. {tokens} tokens successfully created for {department_code}.")