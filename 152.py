#The Designer's Touch (Colors)
import qrcode
my_porject="harder.py"
qr=qrcode.QRCode(version=6,border=7,box_size=7)
qr.add_data("www.linkedin.com/in/kiran-lm-ai-ml")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="purple")
img.save("trail_3.png")
print(" Your QR genaretion is successful")