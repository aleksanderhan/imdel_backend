from PIL import Image
import traceback
import os

image_directory_path = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir)) + '/uploaded_images/'


def makeThumbnail(filename, size=(160, 90)):
    try:
        im = Image.open(image_directory_path + filename)
        im.thumbnail(size)
        im.save(image_directory_path + 'thumbs/' + filename, "JPEG")
    except:
        traceback.print_exc()

