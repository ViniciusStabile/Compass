"""
Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, 
e retorne a soma dos dois. Nessa mesma classe, 
implemente um método de subtração, que aceita dois parâmetros, X e Y, 
e retorne a subtração dos dois (resultados negativos são permitidos).
"""


class Calculo:

    def soma(self, x, y):
        return x + y

    def subtração(self, x, y):
        return x - y


c = Calculo()

x = 4
y = 5

print(f'Somando: {x} + {y}: {c.soma(x, y)}')
print(f'Subtraindo: {x} - {y}: {c.subtração(x, y)}')
