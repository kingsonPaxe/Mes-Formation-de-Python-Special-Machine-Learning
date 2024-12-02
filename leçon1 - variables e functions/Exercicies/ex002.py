# Calcular a energia potencial g"
"""
    formula:
    Eep = masse * hauteur * g
    si la energie calculé est superieure ou inferieure à l'energie limite
"""

def ep_g(masse, hauteur, g = 10, e_limite = None):
    e = masse * hauteur * g
    
    print(f"Ep_g = {float(e)} joles")
    print(e_limite > e)
    print(e_limite < e)


ep_g(200, 5, e_limite=50)

def ep_e(x:float, k = 5000):
    epe = (k * (float(x)**2))/2
    print(f"\nEp_e = {float(epe)} joles")

ep_e(0.1)
