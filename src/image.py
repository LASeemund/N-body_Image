from PIL import Image

class Img:
    def __init__(self, name, width, height):
        self.listPixel = []
        self.name = name
        self.img = Image.new('RGB', (width, height))
    
    def addPixel(self, rgb):
        if type(rgb) == type(1):
            self.listPixel.append(rgb)
        elif type(rgb) == type((0,1)):
            for i in rgb:
                if i >= 0 and i <= 255:
                    self.listPixel.append(i)
                else:
                    raise Exception("rgb is less than 0 or greater than 255.")
        else:
            raise Exception("?")
    
    def save(self):
        self.img.putdata(self.listPixel)
        self.img.save(self.name)