import os
import cv2

#caminho para as imagens
path = "Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    #verificar se a extensão do arquivo corresponde à extensão da imagem
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #certificar-se de que os nomes dos arquivos sejam formados corretamente
        print(file_name)

        images.append(file_name)

count = len(images)
print(len(images))
frame = cv2.imread(images[0])
height, whith, channels = frame.shape
#Crie uma variável de tupla usando width, height
size = (whith, height)
print(size)
out = cv2.VideoWriter('amigos.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for i in range(0, count-1):
    frame = cv2.imread(images[i])
    #Adicione a imagem ao vídeo usando
    out.write(frame)
#Imprima uma mensagem para saber que o vídeo está completo
print('concluido')

