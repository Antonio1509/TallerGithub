from keras.utils import load_img, img_to_array

largo, alto = 500, 500
file = 'CeresChiquita.jpg'

img = load_img(file, target_size = (largo, alto)
             ,color_mode = "grayscale"
             )

print(img.size)
print(img.mode)

#opcion 2
import matplotlib.pyplot as plt
plt.imshow(img, cmap="gray")
plt.imshow(img)
plt.xticks([])
plt.yticks([])
plt.show()

