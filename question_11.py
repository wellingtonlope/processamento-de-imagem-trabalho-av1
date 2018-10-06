# Equalização local em imagens preto e branco. Aplique a equalização local sobre imagem
# “pout.tif” usando uma janela deslizante de tamanho 3 × 3.

# não funciona

import matplotlib.pyplot as plt
from skimage import io


def medVarG(img):
	im_hn = [0] * 256

	rows, cols = img.shape

	MN = rows * cols

	for i in range(rows):
		for j in range(cols):
			im_hn[img[i, j]] += 1 / MN

	m = 0
	for i in range(256):
		m += i * im_hn[i]

	v = 0
	for i in range(256):
		v += ((i - m) ** 2) * im_hn[i]
		print(v)
	return m, v


def medVarL(img, img_out, mG, vG, rows_i, rows_f, cols_i, cols_f):
	im_hn = [0] * 256
	e = 1.1
	k0 = 0.4
	k1 = 0.02
	k2 = 0.4

	MN = 3 * 3

	for i in range(rows_i, rows_f):
		for j in range(cols_i, cols_f):
			im_hn[img[i, j]] += 1 / MN

	m = 0
	for i in range(256):
		m += i * im_hn[i]

	v = 0
	for i in range(256):
		v += (i - m) ** 2 * im_hn[i]

	# print(m, mG, v, vG)
	if m <= k0 * mG and k1 * vG <= v <= k2 * vG:
		print('here')
		img_out[rows_i + 1, cols_i + 1] = img_out[rows_i + 1, cols_i + 1] * e


path = 'img/'
filename = 'pout.tif'

img = io.imread(path + filename)

rows, cols = img.shape

img_out = img.copy()

mG, vG = medVarG(img)

for i in range(1, rows - 1):
	for j in range(1, cols - 1):
		medVarL(img, img_out, mG, vG, i - 1, i + 2, j - 1, j + 2)

plt.figure('In')
io.imshow(img)

plt.figure('Out')
io.imshow(img_out)

io.show()

io.imsave('out/question_11.png', img_out)
