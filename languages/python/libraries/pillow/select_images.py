# Here is a way to automate image processing for multiple images.
import os, sys  # For the path
from PIL import Image
import glob  # Extract the file names of all the images in a folder

# sys.path.append(os.path.abspath(os.path.join('..', 'config')))

path = "project/resources/img/*.jpg"  # Path of the directory that containing the images
# Loop that will go through all the images in the directory
for file in glob.glob(path):
    print(file)  # Just stop here to see all file names printed
    # Now, we can read each file since we have the full path
    Image.open(file).rotate(45, expand=True).save(file+"_rotated45.png", "PNG")   
    # Rotate each image 45 degrees and save it with the same name but with "_rotated45" added to it
