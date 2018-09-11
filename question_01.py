# Usando a imagem da “lena_gray_512.tif” como entrada, gere como saída uma imagem
# em formato de tabuleiro de xadrez (como exemplificado na imagem abaixo) processando
# a imagem de entrada, sendo, um quadrado parte da imagem de entrada e o outro é um
# quadrado preto. A área do quadrado do tabuleiro é de (ou seja, 64 pixels).

import matplotlib.pyplot as plt
from skimage import io

path = 'img/'
filename = 'lena_gray_512.tif'

img = io.imread(path + filename)

rows, cols = img.shape

img_out = img.copy()

h = 64
r = 0
c = 0
for i in range(rows):
	if(r == h * 2):
		r = 0
	for j in range(cols):
		if(c == h * 2):
			c = 0
		if((c < h and r < h) or (c >= h and r >= h)):
			img_out[i, j] = 0
		c += 1
	r += 1

plt.figure('In')
io.imshow(img)

plt.figure('Out')
io.imshow(img_out)

io.show()