import matplotlib.pyplot as plt
from scipy.optimize import linprog

            
#min -> deixa igual. max -> inverte sinal
#para calcular o max o sinal da função objetivo tem que ser negativo 
objetivo = [-3000, -5000]
#lado esquerdo das equações
coefs = [[2, 3],[4, 8]]
#lado direito das equações
results = [30,70]
# minX maxX minY maxY
#define os limites (min,max)
limites = ((0, None))
    
resultado = linprog(objetivo,A_ub = coefs,b_ub = results,bounds = limites, method = 'simplex')

if resultado.success:
    x_obj, y_obj = resultado.x

print("x =", x_obj, "\ny =", y_obj)
#plota os pontos x e y no grafico
plt.scatter(x_obj, y_obj)

plt.show()
