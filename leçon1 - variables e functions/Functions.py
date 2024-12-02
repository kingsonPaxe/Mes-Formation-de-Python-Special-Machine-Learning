f = lambda x, y: x**2 + y
# print(f(3, 4))
# print(f(4, 1))
# print(f(5,4))

# Usando o def
# Caluler le energie potencielle
def e_potentielle(masse, hauteur, g):
    E = masse * hauteur * g
    print('E = ',E, 'Joules')

def e_elestique(x, k= 500):
    Epe = (k * (x**2))/2
    print(f"Epe = {Epe} Joles")

e_elestique(12)
e_potentielle(80, 5, 9.81)