from PIL import Image

def create_binary_message(decrypted_message):
  decrypted_message += '#'
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

  binary_msg = create_binary_message(decrypted_message)

  binary_msg_size = len(binary_msg)
  aux = 0

  for i in range(image.size[0]):
    for j in range(image.size[1]):
      for k in range(0,3):
        if (aux < binary_msg_size):
          if (pixels[i,j][k] % 2 == 0 and binary_msg[aux] == '1'):
            if(k == 0):
              pixels[i,j] = (pixels[i,j][0]+1, pixels[i,j][1], pixels[i,j][2])
            elif(k == 1):
              pixels[i,j] = (pixels[i,j][0], pixels[i,j][1]+1, pixels[i,j][2])
            else:
              pixels[i,j] = (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]+1)
              
          elif (pixels[i,j][k] % 2 != 0 and binary_msg[aux] == '0'):
            if(k == 0):
              pixels[i,j] = (pixels[i,j][0]-1, pixels[i,j][1], pixels[i,j][2])
            elif(k == 1):
              pixels[i,j] = (pixels[i,j][0], pixels[i,j][1]-1, pixels[i,j][2])
            else:
              pixels[i,j] = (pixels[i,j][0], pixels[i,j][1], pixels[i,j][2]-1)
          aux += 1
        else:
          return image

def encode():
  print('Entering encode function')

  image_name = input('Digite o nome da imagem:')
  image = Image.open(image_name, 'r')

  width, height = image.size

  decrypted_message = input('Digite a mensagem a ser criptografada: ')

  if(len(decrypted_message)*8 > width*height*3):
    print('Tamanho de imagem inválido')
    exit()
  else:
    print('Tamanho de imagem suficiente')
  
  new_image = pixel_encode(decrypted_message, image)

  image_save_path = input('Digite o nome da imagem criptografada: ')

  new_image.save(image_save_path)

def decode():
  print('Entering decode function')

  image_to_decode = input('Digite a imagem a ser descriptografada: ')

  image = Image.open(image_to_decode)

  decoded_message = decode_pixel

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