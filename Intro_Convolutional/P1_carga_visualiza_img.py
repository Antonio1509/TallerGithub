from keras.utils import load_img, img_to_array

largo, alto = 500, 500
file = 'CeresChiquita.jpg'

img = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

print(img.size)
print(img.mode)

#opcion 1
img.show()