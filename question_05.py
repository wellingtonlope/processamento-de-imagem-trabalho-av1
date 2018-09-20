# Fusão de imagens. Insira a imagem da “lena_gray_512.tif” no canto inferior da imagem dos
# “vingadores.jpg”.

import matplotlib.pyplot as plt
from skimage import io

path = 'img/'
filename_lena = 'lena_gray_512.tif'
filename_vingadores = 'vingadores.jpg'

img_lena = io.imread(path + filename_lena)
img_vingadores = io.imread(path + filename_vingadores)

rows, cols, dim = img_vingadores.shape


img_out = img_vingadores.copy()
print(rows - rows//2)
print(cols//2 - 0)

for i in range(rows//2,rows):
	for j in range(0, cols//2):
		img_out[i,j] = img_lena[i,j]


plt.figure('In')
io.imshow(img_vingadores)

plt.figure('Out')
io.imshow(img_out)

io.show()

io.imsave('out/question_05.png', img_out)