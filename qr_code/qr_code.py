import qrcode

data = input("Enter any text or URL: ").strip()
file_name = input("Enter the name of file: ").strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image=qr.make_image(fill_color = "black", back_color = "white")
image.save(file_name)
print(f"Image saved in {file_name}")