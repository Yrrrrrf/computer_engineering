# Many other tasks can be performed. Here is full documentation.
# https://pillow.readthedocs.io/en/stable/reference/Image.html
import os, sys  # For the path
from PIL import Image

sys.path.append(os.path.abspath(os.path.join('..', 'config')))
img_path = "project/resources/img/"
save_path = "project/resources/img/archive/"

# Open the image
img = Image.open(img_path+"lena.jpg")  # Not a numpy array
# img.show()  # show Images on external default viewer
print(type(img))  # <class 'PIL.JpegImagePlugin.JpegImageFile'>
print(img. size)  #image size (width, height)
print(img.format)  # image format (.jpg, .png, .gif, etc.)
print(img.mode)  # image mode (P=Pallettised (3*8bits RGB), L=Luminositi (8bit grayscale))

print(img.mode=='L')

print(img.info)  # image info (exif, dpi, etc.)  # what da heck is this? xd

# Resize images
small_img = img.resize((200, 300))  # resizes images to exact value whether it makes sense or not.
# Aspect ratio is not maintained so images are squished
small_img.save(save_path+"smaller_lena.png")  # save image as png
print(small_img.size)  # (200, 300)

img.thumbnail((320, 720))  # resize the image KEEPING the aspect ratio
# This method doesn't blow up the image, only reduces the size if original is larger than the given size
img.save(save_path+"thumbnail_lena.png")  # save image as png
print(img.size)  # (320, 320)
 

# Cropping images
cropped_img = img.crop((0, 0, 100, 200))  # Selects a section of the image from (x0, y0) to (300,300)
# If the given coordinates are outside the image, the image is cropped to the edges of the image.
cropped_img.save(save_path+"cropped_lena.png")
print(cropped_img.size)  # (100, 200)

# We can paste image on another image by copying original image and pasting a second image on it
bg_img = Image.open(img_path+"desert.jpg")
print(bg_img.size)
bg_img.thumbnail((1080, 720))  #Resize in case the image is very large. 
bg_img_copy = bg_img.copy()  # Create a copy of the large image
bg_img_copy.paste(img, (100, 100))  # Pase the smaller imager image at specified location
bg_img_copy.save(save_path+"pasted_lena.png")


# Rotating images
img.rotate(90).save(save_path+"90rotated_lena.jpg")  # keeps original aspect ratio and dimensions
img.rotate(45).save(save_path+"45rotated_lena.jpg")  # keeps original aspect ratio and dimensions
img.rotate(45).save(save_path+"45rotated_lena.jpg", expand=True)  # Dimensions are expanded to fit the entire image

# Flipping or transposing images (like a mirror)
img.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save(save_path+"flippedLR_lena.jpg")  # Flip Left to Right
img.transpose(Image.Transpose.FLIP_TOP_BOTTOM).save(save_path+"flippedTB_lena.jpg")  # Flip Top to Bottom


# Color transforms, convert images between L (greyscale), RGB and CMYK
img.convert('P').save(save_path+"colored_lena.png")  # Convert to Pallettised (3*8bits RGB)
# This is actually the same because the original image is already in grayscale, so in this case it's just a copy
bg_img.convert('L').save(save_path+"greyscale_bg.png")  # Convert to Luminositi (8bit grayscale)

