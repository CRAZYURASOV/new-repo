import qrcode
url = 'www.google.com'
img = qrcode.make(url)
img.save('qr.png')