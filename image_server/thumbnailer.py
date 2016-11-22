from PIL import Image
import traceback

from django.conf import settings


def makeThumbnail(publisher, filename, size=(90, 160)):
    try:
    	root = settings.MEDIA_ROOT + '/' + publisher + '/'
        im = Image.open(root + filename)
        im.thumbnail(size)
        im.save(root + 'thumb_' + filename, "JPEG")
    except:
        traceback.print_exc()

