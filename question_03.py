# Faça as mesmas coisas solicitadas no exercício 1, mas, tome com entrada a imagem
# “lena_color_512.tif” que uma imagem colorida.

import matplotlib.pyplot as plt
from skimage import io

path = 'img/'
filename = 'lena_color_512.tif'

img = io.imread(path + filename)

rows, cols, dim = img.shape

img_out = img.copy()

colors = [[1, 2], [0, 2], [0, 1]]


def next_color(img, i, j, aux):
	if aux == 0:
		# print(img[i - 1, j])
		if img[i - 1, j, 1] == 0 and img[i - 1, j, 2] == 0:
			return 1
		if img[i - 1, j, 0] == 0 and img[i - 1, j, 2] == 0:
			return 2
		if img[i - 1, j, 0] == 0 and img[i - 1, j, 1] == 0:
			return 0
	if aux == 1:
		# print(img[i, j - 1])
		if img[i, j - 1, 1] == 0 and img[i, j - 1, 2] == 0:
			return 1
		if img[i, j - 1, 0] == 0 and img[i, j - 1, 2] == 0:
			return 2
		if img[i, j - 1, 0] == 0 and img[i, j - 1, 1] == 0:
			return 0


def same_color(img, i, j, aux):
	if aux == 0:
		# print(img[i - 1, j])
		if img[i - 1, j, 1] == 0 and img[i - 1, j, 2] == 0:
			return 0
		if img[i - 1, j, 0] == 0 and img[i - 1, j, 2] == 0:
			return 1
		if img[i - 1, j, 0] == 0 and img[i - 1, j, 1] == 0:
			return 2
	if aux == 1:
		# print(img[i, j - 1])
		if img[i, j - 1, 1] == 0 and img[i, j - 1, 2] == 0:
			return 0
		if img[i, j - 1, 0] == 0 and img[i, j - 1, 2] == 0:
			return 1
		if img[i, j - 1, 0] == 0 and img[i, j - 1, 1] == 0:
			return 2


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
