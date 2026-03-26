import qrcode
x=qrcode.QRCode()
msg = "Are you strong because you’re Satoru Gojo, or are you Satoru Gojo because you’re strong"
x.add_data(msg)
x.make(fit=True)
res = x.make_image(fill_color = "black", back_color = "white")
res.save("gokul.png")
print("the qr code is created")