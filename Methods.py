__author__ = 'alm1386'

from PIL import Image, ImageFilter, ImageOps, ImageChops, ImageStat

#convert image to negative for processing
def convertImage(image):
    image = image.convert(mode="L")
    image_negative = ImageOps.invert(image)
    return image_negative

#determine if images are the same
def same(image1, image2):
    neg_image1 = convertImage(image1)
    neg_image2 = convertImage(image2)

    diff = ImageChops.difference(neg_image1, neg_image2)

    stat = ImageStat.Stat(diff)
    mean = stat.mean[0]
    #print (mean)

    if mean < 1.0:
        print ("Same function: These 2 images are the SAME")
        return True
    else:
        print ("Same function: These 2 images are not the same.")
        return False

#determine the angle of rotation it takes to change image 1 into image 2
def rotate(image1, image2):
    neg_image1 = convertImage(image1)
    neg_image2 = convertImage(image2)
    angle = 0

    #Visual testing of presumed answer
    #answer = neg_image1.rotate(90)
    #answer.show()
    #neg_image2.show()

    for angle in range(0,360):
        rotated_image1 = neg_image1.rotate(angle)

        diff = ImageChops.difference(rotated_image1, neg_image2)

        stat = ImageStat.Stat(diff)
        mean = stat.mean[0]

        if mean < 1.0:
            print ("Rotate function: The angle is ", angle)
            return angle

    print ("Rotate function: Image 1 cannot be rotated to match Image 2")
    return False

#determine if vertical reflection turns image 1 into image 2
def verticalReflection(image1, image2):
    neg_image1 = convertImage(image1)
    neg_image2 = convertImage(image2)

    reflected_image1 = ImageOps.flip(neg_image1)

    diff = ImageChops.difference(reflected_image1, neg_image2)
    stat = ImageStat.Stat(diff)
    mean = stat.mean[0]

    if mean < 1.0:
        print ("Vertical Reflection Function: Reflected Vertically")
        return True
    else:
        print ("Vertical Reflection Function: Not reflected vertically")
        return False

#determine if horizontal reflection (mirroring) turns image 1 into image 2
def horizontalReflection(image1, image2):
    neg_image1 = convertImage(image1)
    neg_image2 = convertImage(image2)

    reflected_image1 = ImageOps.mirror(neg_image1)

    diff = ImageChops.difference(reflected_image1, neg_image2)
    stat = ImageStat.Stat(diff)
    mean = stat.mean[0]

    if mean < 1.0:
        print ("Horizontal Reflection Function: Reflected Horizontally")
        return True
    else:
        print ("Horizontal Reflection Function: Not reflected horizontally")
        return False


image1 = Image.open("A2.png")
image2 = Image.open("B2.png")
same(image1, image2)
rotate(image1, image2) #this function returns an angle if true and false if not true.
verticalReflection(image1, image2)
horizontalReflection(image1, image2)

"""
if same(image1, image2):
    print ("Images are the same. Now find a matching answer!")
elif rotate(image1, image2):
    print("Image was rotated. Now find a matching answer!")
elif verticalReflection(image1, image2):
    print ("Image was reflected vertically. Now find a matching answer!")
elif horizontalReflection(image1, image2):
    print ("Image was reflected horizontally. Now find a matching answer!")
"""