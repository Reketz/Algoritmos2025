contador = 0

while(contador < 10):
    contador += 1
    if(contador % 2 == 0):
        continue
    
    print(f'O contador é impar {contador}')