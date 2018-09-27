# Equalização local por regiões não sobrepostas em imagens preto e branco. Aplique a
# equalização local sem sobreposição de regiões (efeito xadrez como exemplificado na
# imagem abaixo) sobre a imagem “pout.tif”. (O tamanho das regiões fica ao seu critério
# sendo que a imagem deve possuir um mínimo de quatro regiões)

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

	MN = (rows_f - rows_i) * (cols_f - cols_i)

	for i in range(rows_i, rows_f):
		for j in range(cols_i, cols_f):
			im_h[img[i, j]] += 1
			im_hn[img[i, j]] += 1 / MN

	im_hn_ac = im_hn.copy()
	s_k[0] = round(255 * im_hn_ac[0])

	for k in range(1, len(im_hn_ac)):
		im_hn_ac[k] = im_hn_ac[k - 1] + im_hn_ac[k]
		s_k[k] = round(255 * im_hn_ac[k])

	for i in range(rows_i, rows_f):
		for j in range(cols_i, cols_f):
			img[i, j] = s_k[img[i, j]]

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

imEqHist(img_out, 0, rows // 2, cols // 2, cols)
imEqHist(img_out, rows // 2, rows, 0, cols // 2)

plt.figure('In')
io.imshow(img)

plt.figure('Out')
io.imshow(img_out)

io.show()

io.imsave('out/question_12.png', img_out)
