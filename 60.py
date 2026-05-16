#"The Vault Lockout"
attempts=0
secret_code="admin999"
while True:
    code=input("Enter the secret code to unlock the vault:")
    attempts+=1
    if code==secret_code:
        print("Vault unlocked successfully!")
        break
    elif attempts>=3:
        print("Too many failed attempts! Vault is now locked permanently.")
        break
    else:
        print("Incorrect code. Try again.")
        