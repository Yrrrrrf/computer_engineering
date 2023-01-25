import cv2  # Import the OpenCV library


img_path = "project/resources/img/"
save_path = "project/resources/img/archive/"

# Open the image
img = cv2.imread(img_path + "waterfall.jpg")
# Using the number 1 as parameter, the image is converted to grayscale
print(img.shape)  # (width, height, channels)
print(type(img))  # <class 'numpy.ndarray'>
print(img.size)  #image size (width, height)    
print(img.dtype)  # image format (.jpg, .png, .gif, etc.)

# Look individual pixels
# In open-cv the color channels are in BGR order, not RGB
print("Pixel at (0,0): ", img[127,127])  # Pixel at (0,0): [B G R]

# Separate color channels
# blue = img[:, :, 0]  # Get the Blue channel
# green= img[:, :, 1]  # Get the Green channel
# red  = img[:, :, 2]  # Get the Red channel
blue, green, red = cv2.split(img)  # These can be done in a single line using the split() method
# cv2.imshow("Blue pixels", blue)
# cv2.imshow("Green pixels", green)
# cv2.imshow("Red pixels", red)

merged_image = cv2.merge((blue, green, red))  # Merge the channels
# cv2.imshow("Merged image", merged_image)


# Resize img
# img = cv2.resize(img, (512, 512))  # Resize the image to 512x512
# resized_img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  # Resize the image to 50% of its original size
# cv2.imshow("Original image", img)
# print("Original image size: ", img.shape)
# cv2.imshow("Resized image", resized_img)
# print("Resized image size: ", resized_img.shape)



cv2.waitKey(0)  # Wait for a key to be pressed
# Using any other number as parameter, will be the time in milliseconds to wait
cv2.destroyAllWindows()  # Close all windows



