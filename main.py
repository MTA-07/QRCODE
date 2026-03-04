import qrcode
data = "https://youtu.be/PvB0kWs2IPQ?si=73aLVAHqOb8QrIde"
resim = qrcode.make(data)
resim.save("ikinci_qr_kod.png")