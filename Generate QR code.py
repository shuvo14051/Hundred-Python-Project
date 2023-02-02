import pyqrcode
import png

link = "https://sites.google.com/view/younusahamed"

qr_code = pyqrcode.create(link)

qr_code.png("portfolio.png", scale=5)