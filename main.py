def encode(encoding_text):
    import numpy as np
    from math import sqrt, ceil
    from PIL import Image
    letters = list("屈\n abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_=+,./?;:'\\\"[]{}<>\|Þßàáâãäåæçèéêëìíîïñòóôõö÷øùúûüýþ")
    image_list = []
    color_values = ()
    for i in list(encoding_text):
        if len(color_values) == 3:
            image_list.append(color_values)
            color_values = ()
        color_values += (letters.index(i)*2,)
    rest = [0,0,0]
    rest[:len(color_values)] = color_values
    image_list.append((*rest,))
    resolution = ceil(sqrt(len(image_list)))
    im = Image.new('RGB', (resolution,resolution))
    data = [(0,0,0) for y in range(im.size[1]) for x in range(im.size[0])]
    data[:len(image_list)] = image_list
    im.putdata(data)
    im.save("image.png")

def decode(image_title):
    from PIL import Image
    from numpy import asarray
    img = Image.open(image_title)
    image_list = asarray(img).tolist()
    letters = list("屈\n abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_=+,./?;:'\\\"[]{}<>\|Þßàáâãäåæçèéêëìíîïñòóôõö÷øùúûüýþ")
    decode = []
    for row in image_list:
        for rgb in row:
            for i in rgb:
                if not letters[i//2] == '屈':
                    decode.append(letters[i//2])
    return "".join(decode)







if __name__ == '__main__': # checks if the code is ran as a file
    encode("Among us.")
    print(decode("image.png"))
