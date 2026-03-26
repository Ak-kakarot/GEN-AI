import qrcode
x=qrcode.QRCode()
upi_id = "your upi ID"
name = "zenin"
note = "weekend party"
amount= "100"
link = f"upi://pay?pa={upi_id}&pn={name}&tn={note}&am={amount}&cu=INR"
x.add_data(link)
x.make(fit=True)
res =x.make_image(fill_color="black",back_color="white")
res.save("gpay.png")
print("QR code created")