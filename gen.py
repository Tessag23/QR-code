import pyqrcode
import png
from pyqrcode import QRCode

link='www.wikipedia.com'
url=pyqrcode.create(link)
url.png('wikipediaqrcode.png',scale=6)