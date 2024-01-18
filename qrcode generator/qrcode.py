import qrcode

img = qrcode.make("this is me")
img.save('myQRcode.png')
img.show()