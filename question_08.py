import matplotlib.pyplot as plt
from skimage import io


def imgHist(img):
	"""
	Gera dois vetores representando o histograma da imagem
	um absoluto e um normalizado

	:param img:
	:return im_h, im_hn:
	"""
	rows, cols = img.shape
	im_h = [0] * 256
	im_hn = im_h.copy()
	MN = rows * cols

	for i in range(rows):
		for j in range(cols):
			im_h[img[i, j]] += 1
			im_hn[img[i, j]] += 1 / MN

	return im_h, im_hn


def h():
	im_hen = [0] * 256

	for i in range(256):
		if 129 <= i <= 149:
			im_hen[i] = 0.002
		if 150 <= i <= 170:
			im_hen[i] = 0.007
		if 171 <= i <= 191:
			im_hen[i] = 0.009
		if 192 == i:
			im_hen[i] = 0.224
		if 193 <= i <= 213:
			im_hen[i] = 0.009
		if 214 <= i <= 234:
			im_hen[i] = 0.007
		if 235 <= i <= 255:
			im_hen[i] = 0.002

	return im_hen


def Tr_xk(im_hn):
	im_hn_ac = im_hn.copy()

	x_k = [0] * len(im_hn)

	x_k[0] = round(255 * im_hn_ac[0])

	for k in range(1, len(im_hn_ac)):
		im_hn_ac[k] = im_hn_ac[k - 1] + im_hn_ac[k]
		x_k[k] = round(255 * im_hn_ac[k])

	return x_k


def imEspHist(img, s_k, v_t):
	"""
	realiza especificacao do histograma
	em uma imagem (8 bits) em escala de cinza

	:param img:  imagem de entrada
	:param s_k:  mapeamento dos pixels s_k
	:param v_t:  mapeamento dos pixels v_t
	:return:
	"""
	rows, cols = img.shape
	imgEsp = img.copy()
	imgEq = img.copy()
	s_q = s_k.copy()
	j = 0

	for i in range(len(s_k)):
		while (True):
			if v_t[j] == s_k[i]:
				s_q[i] = j
				break
			elif v_t[j] > s_k[i]:
				j -= 1
				s_q[i] = j
				break
			else:
				if j < 255:
					j += 1
				else:
					break

	for i in range(rows):
		for j in range(cols):
			imgEq[i, j] = s_k[imgEq[i, j]]
			imgEsp[i, j] = s_q[imgEsp[i, j]]

	return imgEsp, imgEq


# Inicio do programa
path = 'img/'
filename = 'lena_gray_512.tif'

img = io.imread(path + filename)
im_h, im_hn = imgHist(img)
im_hen = h()
s_k = Tr_xk(im_hn)
v_t = Tr_xk(im_hen)
imgEsp, imgEq = imEspHist(img, s_k, v_t)

im_hEq, im_hnEq = imgHist(imgEq)
im_hEsp, im_hnEsp = imgHist(imgEsp)

plt.figure('Imagem de Entrada')
io.imshow(img)

plt.figure('Imagem Equalizada')
io.imshow(imgEq)

plt.figure('Imagem Especializada')
io.imshow(imgEsp)

plt.figure('Histograma da imagem')
plt.bar(range(256), im_hn)

plt.figure('Histograma Especializado')
plt.bar(range(256), im_hen)

plt.figure('Histograma da imagem equalizada')
plt.bar(range(256), im_hnEq)

plt.figure('Histograma da imagem especializada')
plt.bar(range(256), im_hnEsp)

io.show()

io.imsave('out/question_08.jpg', imgEsp)
