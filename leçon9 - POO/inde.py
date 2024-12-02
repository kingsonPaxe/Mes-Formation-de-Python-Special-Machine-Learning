class cao:
    # funcoes:
    def __init__(self) -> None:
        pass
    def andar (self):
        print('Andando')
        
    def comer(self):
        print('comendo')
    
    def dormir(self):
        print('dormindo')
animal1 = cao()
animal1.andar()

import numpy as np

list = np.arange(1,4)
print(list)

list2 = [1, 2, 3]
list2 = np.array(list2)
print(list2)
print(list2.mean())
# print(dir(list2))

print(f'list = type({type(list)})')
print(f'list = type({type(list2)})')
