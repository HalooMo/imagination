from PIL import Image, ImageFilter
import numpy as np
from PIL.ExifTags import TAGS


img = Image.open(r"C:\Imagin\imagination\img.jpg")
img.getexif()
exif = img.getexif()
print("ST")
print(exif)
for i in exif:
    print("Start")
    tag = TAGS.get(i, i)
    data = exif.get()
    print(type(data))
    if isinstance(data, bytes):
        data = data.decode()
    print("{0} --> {1}".format(tag, data))





'''
with Image.open("C:\pyln\imagination\jordan.jpg") as img:
    img_arr = np.ones((600, 600))
    img_arr[200:400, 200:400] = 255
    img = Image.fromarray(img_arr)
    img = img.convert("L")
    print(img.mode)
    img.filter(ImageFilter.)
    img.show()
    #img.transpose(Image.FLIP_TOP_BOTTOM).show()
    #img.transpose(Image.TRANSPOSE).show()
    #img.transpose(Image.TRANSVERSE).show()
    #img.transpose(Image.ROTATE_180).show()
    #img.rotate(34, expand=True).show()
    #img.filter(ImageFilter.BoxBlur(20)).show()
    #img.filter(ImageFilter.GaussianBlur()).show()
    #i.filter(ImageFilter.EMBOSS).show()

    def erbos(img, num, arg):
        for i in range(num):
            img = img.filter(ImageFilter.MinFilter(arg))
        return img
    def detail(img, num, arg):
        for i in range(num):
            img = img.filter(ImageFilter.MaxFilter(arg))
            return img
    red, green, blue = img.split()
    img = img.convert("L")
    blank =  red.point(lambda _:0)
    img1 = img.point(lambda x: 255 if x > 100 else 0)
    img2 = img.point(lambda x: 255 if x > 23 else 0)
    image1 = Image.composite(img, blank, img1)
    image2 = Image.composite(img, image1, img2)
    img.convert("1")
    img = erbos(img, 12, 5)
    img = detail(img, 5, 5)
    img.show()

    #emb = embose(img_mask, 10)
    #emb = delate(emb, 16)
    #emb.show()
    img.show()
    sharp = img.filter(ImageFilter.SHARPEN)
    img.filter(ImageFilter.SMOOTH).show()
    sm = sharp.filter(ImageFilter.SMOOTH).show()
    
    print(img.mode)
    red, green, blure = img.split()
    print(red.mode)
    redi = red.point(lambda _: 255)
    redi.show()
    
    img2 = img.crop((12, 34, 342, 233))
    img2.thumbnail()
    img2.show()
    '''