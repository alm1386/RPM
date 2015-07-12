__author__ = 'alm1386'

from PIL import Image, ImageFilter, ImageOps, ImageChops, ImageStat

#convert figure to negative for processing
def convertImage(image):
    image = image.convert(mode="L")
    image_negative = ImageOps.invert(image)
    return image_negative

def same(image1, image2):
    neg_image1 = convertImage(image1)
    neg_image2 = convertImage(image2)

    diff = ImageChops.difference(neg_image1, neg_image2)

    stat = ImageStat.Stat(diff)
    mean = stat.mean
    print (mean)

    if float(mean) < 10.0:
        print ("match!")
        return True
    else:
        print ("no match")
        return False


def rotate(image1, image2):
    neg_image1 = convertImage(image1)
    neg_image2 = convertImage(image2)
    angle = 0

    rotated_image1 = neg_image1.rotate(angle)

    for angle in range(0,360):
        rotated_image1 = neg_image1.rotate(angle)

        if rotated_image1 == neg_image2:
            print ("The angle is ", angle)
            return angle

    return False

def verticalReflection(image1, image2):
    neg_image1 = convertImage(image1)
    neg_image2 = convertImage(image2)

    reflected_image1 = ImageOps.flip(neg_image1)

    if reflected_image1 == neg_image2:
        print ("Reflected Vertically")
        return True
    else:
        return False

def horizontalReflection(image1, image2):
    neg_image1 = convertImage(image1)
    neg_image2 = convertImage(image2)

    reflected_image1 = ImageOps.mirror(neg_image1)
    reflected_image1.show()
    neg_image2.show()

    if reflected_image1 == neg_image2:
        print ("Reflected Horizontally")
        return True
    else:
        return False


image1 = Image.open("A.png")
image2 = Image.open("B.png")
if same(image1, image2):
    print ("Images are the same. Now find a matching answer!")
elif rotate(image1, image2):
    print("Image was rotated. Now find a matching answer!")
elif verticalReflection(image1, image2):
    print ("Image was reflected vertically. Now find a matching answer!")
elif horizontalReflection(image1, image2):
    print ("Image was reflected horizontally. Now find a matching answer!")
