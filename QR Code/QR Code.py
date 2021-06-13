import pyqrcode
from pyzbar.pyzbar import decode    #for decoding
from PIL import Image

#(encoding)
#now mention the data of the qr code
data= 'Glad you liked my project'
#now lets just encode data into a new qr code
img=pyqrcode.create(data)
#save this qr code as an image file
img.png("myqrcode.png",scale=8)

#(Decoding)
d=decode(Image.open("myqrcode.png"))
print(d[0].data.decode("ascii"))
