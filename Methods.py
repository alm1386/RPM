__author__ = 'alm1386'

from PIL import Image, ImageFilter, ImageOps

#convert figure to negative for processing
def convertImage(fig):
    fig = fig.convert(mode="L")
    #fig.show()
    fig_negative = ImageOps.invert(fig)
    #fig_negative.show()
    return fig_negative

def same(fig1, fig2):
    neg_Fig1 = convertImage(fig1)
    neg_Fig2 = convertImage(fig2)
   #neg_Fig1.show()
   #neg_Fig2.show()
    if neg_Fig1 == neg_Fig2:
        print ("match!")
        return True
    else:
        print ("no match")
        return False


def rotate(fig1, fig2):
    neg_Fig1 = convertImage(fig1)
    neg_Fig2 = convertImage(fig2)
    angle = 0

    #neg_Fig2.show()
    rotated_Fig1 = neg_Fig1.rotate(angle)
    #rotated_Fig1.show()

    for angle in range(0,360):
        rotated_Fig1 = neg_Fig1.rotate(angle)

        if rotated_Fig1 == neg_Fig2:
            print ("The angle is ", angle)
            return angle

    return False
    #neg_Fig1.show()
    #neg_Fig2.show()

def verticalReflection(fig1, fig2):
    neg_Fig1 = convertImage(fig1)
    neg_Fig2 = convertImage(fig2)

    reflected_Fig1 = ImageOps.flip(neg_Fig1)
    #reflected_Fig1.show()
    #neg_Fig2.show()

    if reflected_Fig1 == neg_Fig2:
        print ("Reflected Vertically")
        return True
    else:
        return False

def horizontalReflection(fig1, fig2):
    neg_Fig1 = convertImage(fig1)
    neg_Fig2 = convertImage(fig2)

    reflected_Fig1 = ImageOps.mirror(neg_Fig1)
    reflected_Fig1.show()
    neg_Fig2.show()

    if reflected_Fig1 == neg_Fig2:
        print ("Reflected Horizontally")
        return True
    else:
        return False


image1 = Image.open("A2.png")
image2 = Image.open("C2.png")
if same(image1, image2):
    print ("Images are the same. Now find a matching answer!")
elif rotate(image1, image2):
    print("Image was rotated. Now find a matching answer!")
elif verticalReflection(image1, image2):
    print ("Image was reflected vertically. Now find a matching answer!")
elif horizontalReflection(image1, image2):
    print ("Image was reflected horizontally. Now find a matching answer!")
