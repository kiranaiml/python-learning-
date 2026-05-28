import qrcode
while True:
    user=input("Enter a link (or type 'exit' to quit): ").lower()
    if user=="exit" or user=="break":
        print("Shutting down generator...")
        break
    else:
        qr=qrcode.QRCode(version=1,border=5,box_size=8)
        qr.add_data(user)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="yellow")
        img.save("trail_4.png")
        print("Your image genereted is successful")