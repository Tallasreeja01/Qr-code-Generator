import qrcode

data = input("Enter the text or URL: ")
img = qrcode.make(data)
img.save("myqr.png")
print("QR Code Generated Successfully! Check the project folder.")
