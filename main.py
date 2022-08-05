def encode_image(encoding_text, filename="image.png"):
    import numpy as np
    from math import sqrt, ceil
    from PIL import Image
    a = bytearray(encoding_text, 'ISO-8859-1')
    image_list = []
    color_values = ()
    for i in range(len(a)):
        if len(color_values) < 3:
            color_values += (a[i],)
        else:
            image_list.append(color_values)
            color_values = (a[i],)
    rest = [0,0,0]
    rest[:len(color_values)] = color_values
    image_list.append((*rest,))
    resolution = ceil(sqrt(len(image_list)))
    im = Image.new('RGB', (resolution,resolution))
    data = [(0,0,0) for y in range(im.size[1]) for x in range(im.size[0])]
    data[:len(image_list)] = image_list
    im.putdata(data)
    im.save(filename)

def decode_image(image_title):
    from PIL import Image
    from numpy import asarray
    img = Image.open(image_title)
    image_list = asarray(img).tolist()
    num_array = [item for subl in image_list for subsubl in subl for item in subsubl]
    return bytearray(num_array).decode('ISO-8859-1', errors='ignore')

if __name__ == '__main__': # checks if the code is ran as a file
    encode_image("ÿÿÿ")
