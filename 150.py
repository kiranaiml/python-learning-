#The Architect's Blueprint
import qrcode
my_porfolio="level_two.py"
qr = qrcode.QRCode(version=1, box_size=15, border=2)
qr.add_data("https://github.com/kiranaiml")
qr.make(fit=True)
img = qr.make_image()
img.save("trail.png")