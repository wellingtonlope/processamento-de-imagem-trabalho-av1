# Usando a imagem da “lena_gray_512.tif” como entrada, gere como saída uma imagem
# em formato de tabuleiro de xadrez (como exemplificado na imagem abaixo) processando
# a imagem de entrada, sendo, um quadrado parte da imagem de entrada e o outro é um
# quadrado preto. A área do quadrado do tabuleiro é de (ou seja, 64 pixels).

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