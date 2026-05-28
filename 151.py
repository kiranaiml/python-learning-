#image genaretion qr code
import qrcode
qr=qrcode.QRCode(version=3,border=4,box_size=8)
qr.add_data("https://drive.google.com/file/d/1YeyuJi0HIW8GBX42yCjzSKIYoyZBmcyU/view?usp=share_link")
qr.make(fit=True)
img=qr.make_image()
img.save("trail_2.png")
print("Your qrcode is successfully genareted")