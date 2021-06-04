from PIL import Image
from conf import user

img=Image.open("coder.jpg")
#rasmni ochib beradi
img.show()
#hajmini ekranga chiqaradi
print(img.size,user)
#fayl formatini chiqaradi
print(img.format)
#ranglar korinishi
print(img.mode)