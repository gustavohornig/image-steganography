from PIL import Image

def create_binary_message(decrypted_message):
  binary_msg = []
  for i in decrypted_message:
    char_to_integer = ord(i)
    byte = bin(char_to_integer)
    print(byte)
    if(len(byte) < 9):
      zeros_to_add = 9 - len(byte)
      for _ in range(zeros_to_add):
        binary_msg.append('0')
    for j in range(2,len(byte)):
      print(byte[j])
      binary_msg.append(byte[j])

  return binary_msg

def pixel_encode(decrypted_message, image):

  pixels = image.load()

  print(pixels[0,0][1])

  #for i in range(image.size[0]):
  #  for j in rprint(i)ange(image.size[1]):
  #    for k in (0,2):
  #      print(pixels[i,j][k])
  
  binary_msg = create_binary_message(decrypted_message)
  print(binary_msg)


def encode():
  print('Entering encode function')

  image_name = input('Digite o nome da imagem:')
  image = Image.open(image_name, 'r')
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
  
  pixel_encode(decrypted_message, image)

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