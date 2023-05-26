import matplotlib.pyplot as plt
from scipy.optimize import linprog

            
#min -> deixa igual. max -> inverte sinal
objetivo = [1, 2]
coefs = [[1, 0],[1, 0],[1, 1]]
results = [8,5,10]
#        minX maxX minY maxY
limites = ((5, 8), (0, None))
    

resultado  = linprog(objetivo,A_ub = coefs,b_ub = results,bounds = limites, method = 'simplex')

if resultado.success:
    x_obj, y_obj = resultado.x



print("x =", x_obj, "\ny =", y_obj)
plt.scatter(x_obj, y_obj)

plt.show()
