import project as pj
import math, statistics,os,glob,random

q = pj.quadrado(3)
print(f"Resultado: [{q}]")
print("soma = ",pj.soma(3,5))
print(pj.fibonacci(32 ))


#================================================================================================
# Statistics
#================================================================================================

lst = [3, 2, 4, 0]
# 3 + 2 + 4 =  9/3 = 3.
print("\nMedia = ",statistics.mean(lst))
print("Mediana = ",statistics.median(lst)) # mediana

#================================================================================================
# random
#================================================================================================

lis_nome = ["Ghost", "Tariq", "Thomie"]
print(f"Eu escolho: {random.choice(lis_nome)}")

#================================================================================================
# math
#================================================================================================

n = 4
print(f"Raiz({n}) = ",math.sqrt(n))
print(f"valor de pi = ", math.pi)

#================================================================================================
# os - operating system
#================================================================================================

print('Directorio: ',os.getcwd())

#================================================================================================
# glob - usados para retornar os nomes dos nossos ficheiros
#================================================================================================
archirves_name = glob.glob('*')
print(archirves_name) # Vai moostrar todas sa pastas que eu criei no "Formation de machine learning"

# filtrar
archirves_name = glob.glob('*.ini') # Mostra-me tudo com o nome ini 
print(archirves_name)
