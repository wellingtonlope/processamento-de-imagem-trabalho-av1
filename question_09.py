# Equalização local em imagens coloridas. Aplique a equalização local sobre imagem
# “lago.jpg” usando uma janela deslizante de tamanho 3 × 3.

import matplotlib.pyplot as plt
from skimage import io


def imEqHist(img, img_out, rows_i, rows_f, cols_i, cols_f):
	"""
	realiza equalizacao de histograma
	em uma imagem (8 bits) em escala de cinza
	:return: imagem em escala de cinza(vetor) e seus vetores de histogramas
	"""
	# rows, cols = img.shape

	im_hn_r = [0] * 256
	im_hn_g = [0] * 256
	im_hn_b = [0] * 256
	s_k_r = [0] * 256
	s_k_g = [0] * 256
	s_k_b = [0] * 256

	MN = 3 * 3

	for i in range(rows_i, rows_f):
		for j in range(cols_i, cols_f):
			im_hn_r[img[i, j, 0]] += 1 / MN
			im_hn_g[img[i, j, 0]] += 1 / MN
			im_hn_b[img[i, j, 0]] += 1 / MN

	s_k_r[0] = round(255 * im_hn_r[0])
	s_k_g[0] = round(255 * im_hn_g[0])
	s_k_b[0] = round(255 * im_hn_b[0])

	for k in range(1, 256):
		im_hn_r[k] = im_hn_r[k - 1] + im_hn_r[k]
		s_k_r[k] = round(255 * im_hn_r[k])
		im_hn_g[k] = im_hn_g[k - 1] + im_hn_g[k]
		s_k_g[k] = round(255 * im_hn_g[k])
		im_hn_b[k] = im_hn_b[k - 1] + im_hn_b[k]
		s_k_b[k] = round(255 * im_hn_b[k])

	img_out[rows_i + 1, cols_i + 1, 0] = s_k_r[img[rows_i + 1, cols_i + 1, 0]]
	img_out[rows_i + 1, cols_i + 1, 1] = s_k_g[img[rows_i + 1, cols_i + 1, 1]]
	img_out[rows_i + 1, cols_i + 1, 2] = s_k_b[img[rows_i + 1, cols_i + 1, 2]]

	return img_out


path = 'img/'
filename = 'lago.jpg'

img = io.imread(path + filename)

rows, cols, dim = img.shape

img_out = img.copy()

for i in range(1, rows - 1):
	for j in range(1, cols - 1):
		imEqHist(img, img_out, i - 1, i + 1, j - 1, j + 1)

plt.figure('In')
io.imshow(img)

plt.figure('Out')
io.imshow(img_out)

io.show()

io.imsave('out/question_09.png', img_out)
