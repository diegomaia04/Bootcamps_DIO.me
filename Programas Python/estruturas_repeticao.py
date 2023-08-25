# estrutura de repetição for

texto = input("informe um texto: ")
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
 # print() # adiciona uma quebra de linha texto
  print("Executa no final do laço")

  # for exemplo utilizando a função buily-in range

  for numero in range(0, 51, 5):
     print(numero)

for numeor_3 in range(100):
   if numeor_3 % 2 == 0:
      continue
   
   print(numeor_3)
 
     




 


