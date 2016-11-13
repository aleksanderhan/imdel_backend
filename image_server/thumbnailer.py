from PIL import Image
import traceback
import os

save_directory_path = os.path.abspath(os.path.join(os.path.abspath(__file__), os.pardir, os.pardir)) + '/uploaded_images/thumbs/'


def makeThumbnail(filename, size=(160, 90)):
    try:
        im = Image.open(filename)
        im.thumbnail(size)
        im.save(save_directory_path + filename, "JPEG")
    except:
        traceback.print_exc()
