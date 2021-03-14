from PIL import Image

def encode():
  print('Entering encode function')

  image_name = input('Digite o nome da imagem:')
  image = Image.open(image_name)
  #image.show()

  pixel_values = image.getpixel((0,0))
  print(pixel_values)

  width, height = image.size

  decrypted_message = input('Digite a mensagem a ser criptografada: ')

  if(len(decrypted_message)*8 > width*height*3):
    print('Tamanho de imagem inválido')
    exit()
  else:
    print('Tamanho de imagem suficiente')

def decode():
  print('Entering decode function')

def main():
  print('Entering main')

  option = int(input("1.Criptografar \n2.Descriptografar"))

  if (option == 1):
    encode()
  
  elif (option == 2):
    decode()
  
  else:
    print("Entrada inválida")

if __name__ == '__main__' :
 
    # Calling main function
    main()