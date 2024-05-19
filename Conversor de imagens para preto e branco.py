# pip install pillow
from PIL import Image

imagem = Image.open(input('Selecione a imagem: ').replace('"', ''))
imagem = imagem.convert('L')
imagem.save('foto_preto_branco.jpg')

input('\nImagem convertida com sucesso!\nAperte ENTER para sair...')