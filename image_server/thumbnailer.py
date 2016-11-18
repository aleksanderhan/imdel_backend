from PIL import Image
import traceback

from django.conf import settings


def makeThumbnail(filename, size=(90, 160)):
    try:
        im = Image.open(settings.MEDIA_ROOT + filename)
        im.thumbnail(size)
        im.save(settings.MEDIA_ROOT + 'thumbs/' + filename, "JPEG")
    except:
        traceback.print_exc()

