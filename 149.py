#The GitHub Profile Link
import qrcode
my_profile = "https://github.com/kiranaiml"
img = qrcode.make(my_profile)
img.save("/Users/kiranlm/Desktop/portfolio_qr.png")
print("Successfully QR code genareted")