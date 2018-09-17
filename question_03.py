# Usando a imagem da “lena_color_512.tif” como entrada, faça o seu processamento com
# objetivo de gerar uma imagem com o efeito de tabuleiro na qual cada quadrado representa
# um canal da imagem de entrada, ou seja, um quadrado que demonstra o canal vermelho
# (red), o canal verde (green) e o canal azul (blue) como exemplificado na imagem abaixo. Os
# quadrados devem ter seus canais de cores alternados, seus vizinhos não podem ter os
# mesmos canais de cores, e o tamanho do quadrado deve ser 4 × 4 (16 pixels).

def next_color(img, i, j, aux):
	if aux == 0:
		if img[i - 1, j, 0] != 0:
			return 1
		if img[i - 1, j, 1] != 0:
			return 2
		if img[i - 1, j, 2] != 0:
			return 0
	if aux == 1:
		if img[i, j - 1, 0] != 0:
			return 1
		if img[i, j - 1, 1] != 0:
			return 2
		if img[i, j - 1, 2] != 0:
			return 0

def same_color(img, i, j, aux):
	if aux == 0:
		if img[i - 1, j, 0] != 0:
			return 0
		if img[i - 1, j, 1] != 0:
			return 1
		if img[i - 1, j, 2] != 0:
			return 2
	if aux == 1:
		if img[i, j - 1, 0] != 0:
			return 0
		if img[i, j - 1, 1] != 0:
			return 1
		if img[i, j - 1, 2] != 0:
			return 2

import matplotlib.pyplot as plt
from skimage import io

path = 'img/'
filename = 'lena_color_512.tif'

img = io.imread(path + filename)

rows, cols, dim = img.shape

img_out = img.copy()

h = 4
color = 0
r = 0
c = 0
for i in range(rows):
	if r == h:
		r = 0
		if i > 0:
			color = next_color(img_out, i, 0, 0)
	else:
		if i > 0:
			color = same_color(img_out, i, 0, 0)
	for j in range(cols):
		if c == h:
			c = 0
			if j > 0:
				color = next_color(img_out, i, j, 1)
		if color != 0:
			img_out[i, j, 0] = 0
		if color != 1:
			img_out[i, j, 1] = 0
		if color != 2:
			img_out[i, j, 2] = 0
		c += 1
	r += 1

plt.figure('In')
io.imshow(img)

plt.figure('Out')
io.imshow(img_out)

io.show()

io.imsave('out/chess_rgb_lena_color.png', img_out)
