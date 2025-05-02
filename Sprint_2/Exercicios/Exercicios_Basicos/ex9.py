"""
Implemente a classe Lampada. 
A classe Lâmpada recebe um booleano no seu construtor, 
True se a lâmpada estiver ligada, False caso esteja desligada. 
A classe Lampada possuí os seguintes métodos:

liga(): muda o estado da lâmpada para ligada

desliga(): muda o estado da lâmpada para desligada

esta_ligada(): retorna verdadeiro se a lâmpada estiver ligada, falso caso contrário
"""


class Lampada:
    def __init__(self, ligada):
        self.ligada = ligada

    def liga(self):
        self.ligada = True

    def desliga(self):
        self.ligada = False

    def esta_ligada(self):
        return self.ligada


l1 = Lampada(False)

l1.liga()
print(f'A lâmpada está ligada? {l1.esta_ligada()}')

l1.desliga()
print(f'A lâmpada ainda está ligada? {l1.esta_ligada()}')
