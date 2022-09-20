from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/Users/Blacc/PycharmProjects/pythonProject/pyhon/Myqrcode1.png")

result = decode(img)

print(result)