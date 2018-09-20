# Faça as mesmas coisas solicitadas no exercício 1, mas, tome com entrada a imagem
# “lena_color_512.tif” que uma imagem colorida.

import matplotlib.pyplot as plt
from skimage import io

path = 'img/'
filename = 'lena_color_512.tif'

img = io.imread(path + filename)

rows, cols, dim = img.shape

img_out = img.copy()

h = 8
r = 0
c = 0
for i in range(rows):
	if(r == h * 2):
		r = 0
	for j in range(cols):
		if(c == h * 2):
			c = 0
		if((c < h and r < h) or (c >= h and r >= h)):
			img_out[i, j, 0] = 0
			img_out[i, j, 1] = 0
			img_out[i, j, 2] = 0
		c += 1
	r += 1

plt.figure('In')
io.imshow(img)

plt.figure('Out')
io.imshow(img_out)

io.show()

io.imsave('out/question_02.png', img_out)