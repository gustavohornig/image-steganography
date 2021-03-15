from PIL import Image

def create_binary_message(decrypted_message):
  decrypted_message += '#'
  binary_msg = []
  for i in decrypted_message:
    char_to_integer = ord(i)
    byte = bin(char_to_integer)
    if(len(byte) < 9):
      zeros_to_add = 9 - len(byte)
      for _ in range(zeros_to_add):
        binary_msg.append('0')
    for j in range(2,len(byte)):
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

  image_name = input('Digite o nome da imagem:')
  image = Image.open(image_name, 'r')

  width, height = image.size

  decrypted_message = input('Digite a mensagem a ser criptografada: ')

  if(len(decrypted_message)*8 > width*height*3):
    print('Tamanho de imagem inválido')
    exit()
  
  new_image = pixel_encode(decrypted_message, image)

  image_save_path = input('Digite o nome da imagem criptografada: ')

  new_image.save(image_save_path)

def pixel_decode(image):
  
  aux = 0
  k = 0
  binary_char = ''
  decrypted_message = ''
  pixels = image.load()
  

  for i in range(image.size[0]):
    for j in range(image.size[1]):
      k = 0
      while (k < 3):
        if (aux < 7):
          if (pixels[i,j][k] % 2 == 0):
            binary_char += '0'
          else:
            binary_char += '1'
          aux += 1
        else:
          char = chr(int(binary_char, 2))
          if(char == '#'):
            return decrypted_message
          decrypted_message += char
          binary_char =''
          aux = 0
          k -= 1
        k += 1

  
def decode():

  image_to_decode = input('Digite a imagem a ser descriptografada: ')

  image = Image.open(image_to_decode)

  decoded_message = pixel_decode(image)

  print('A mensagem descriptografada é:')
  print(decoded_message)

def main():

  print('#########################')
  print('#     Steganography     #')
  print('#    Gustavo Hornig     #')
  print('#     GRR20163065       #')
  print('#  Trabalho 2 - Cripto  #')
  print('#########################')

  option = int(input("1.Criptografar \n2.Descriptografar\nR: "))

  if (option == 1):
    encode()
  
  elif (option == 2):
    decode()
  
  else:
    print("Entrada inválida")

if __name__ == '__main__' :
 
    # Calling main function
    main()