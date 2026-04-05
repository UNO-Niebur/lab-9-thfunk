# Lab 9 – Image Processing
# Name: Taran Funk
# Date: 4/2/2026
# Assignment: Lab 9

from PIL import Image


def swapGreenBlue(img):
    """Swap the green and blue values for every pixel in the image."""

    pixels = img.load()
    width, height = img.size

    if len(pixels[0,0]) == 3: #no alpha channel
        for x in range(width):
            for y in range(height):
                red, green, blue = pixels[x, y]
                pixels[x, y] = (red, blue, green)
    
    if len(pixels[0,0]) == 4: #has alpha channel
        for x in range(width):
            for y in range(height):
                red, green, blue, alpha = pixels[x, y]
                pixels[x, y] = (red, blue, green, alpha)

    img.save("swapGB.png")


def darken(img, amount):
    """Darken the image by reducing RGB values by the given amount."""
    
    pixels = img.load()
    width, height = img.size

    if len(pixels[0,0]) == 3: #no alpha channel
        for x in range(width):
            for y in range(height):
                red, green, blue = pixels[x, y]
                pixels[x, y] = (max(0, red - amount), max(0, green - amount), max(0, blue - amount))

    if len(pixels[0,0]) == 4: #has alpha channel
        for x in range(width):
            for y in range(height):
                red, green, blue, alpha = pixels[x, y]
                pixels[x, y] = (max(0, red - amount), max(0, green - amount), max(0, blue - amount), alpha)

    img.save("darkImg.png")


def bwFilter(img):
    """Example function: converts image to grayscale."""
    
    pixels = img.load()
    width, height = img.size

    if len(pixels[0,0]) == 3: #no alpha channel
        for x in range(width):
            for y in range(height):
                red, green, blue = pixels[x, y]
                avg = (red + green + blue) // 3
                pixels[x, y] = (avg, avg, avg)

    if len(pixels[0,0]) == 4: #has alpha channel
        for x in range(width):
            for y in range(height):
                red, green, blue, alpha = pixels[x, y]
                avg = (red + green + blue) // 3
                pixels[x, y] = (avg, avg, avg, alpha)

    img.save("bwImg.png")


def main():
    # Open the image file
    #myImg = Image.open("durango.png")
    myImg = Image.open("pki.png")

    # Example (already completed)
    #bwFilter(myImg)

    # Uncomment each function as you complete it
    #swapGreenBlue(myImg)
    darken(myImg, 20)


if __name__ == "__main__":
    main()
