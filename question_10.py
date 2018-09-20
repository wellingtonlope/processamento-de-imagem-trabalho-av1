# Equalização local em imagens preto e branco. Aplique a equalização local sobre imagem
# “pout.tif” usando uma janela deslizante de tamanho 3 × 3.

import matplotlib.pyplot as plt
from skimage import io


def imEqHist(img, rows_i, rows_f, cols_i, cols_f):
	"""
	realiza equalizacao de histograma
	em uma imagem (8 bits) em escala de cinza
	:return: imagem em escala de cinza(vetor) e seus vetores de histogramas
	"""
	# rows, cols = img.shape

	im_h = [0] * 256
	im_hn = im_h.copy()
	s_k = im_h.copy()

	MN = 3 * 3

	for i in range(rows_i, rows_f):
		for j in range(cols_i, cols_f):
			im_h[img[i, j]] += 1
			im_hn[img[i, j]] += 1 / MN

	im_hn_ac = im_hn.copy()
	s_k[0] = round(255 * im_hn_ac[0])

	for k in range(1, len(im_hn_ac)):
		im_hn_ac[k] = im_hn_ac[k - 1] + im_hn_ac[k]
		s_k[k] = round(255 * im_hn_ac[k])

	# for i in range(rows_i, rows_f):
	# 	for j in range(cols_i, cols_f):
	# 		img[i, j] = s_k[img[i, j]]
	img[rows_i + 1, cols_i + 1] = s_k[img[rows_i + 1, cols_i + 1]]

	im_hEq = [0] * 256
	im_hnEq = im_hEq.copy()

	for i in range(rows_i, rows_f):
		for j in range(cols_i, cols_f):
			im_hEq[img[i, j]] += 1
			im_hnEq[img[i, j]] += 1 / MN

	# return [im_h, im_hn, im_hEq, im_hnEq, img]
	return img


path = 'img/'
filename = 'pout.tif'

img = io.imread(path + filename)

rows, cols = img.shape

img_out = img.copy()

for i in range(1, rows - 1):
	for j in range(1, cols - 1):
		imEqHist(img_out, i - 1, i + 1, j - 1, j + 1)

plt.figure('In')
io.imshow(img)

plt.figure('Out')
io.imshow(img_out)

io.show()

io.imsave('out/question_10.png', img_out)
