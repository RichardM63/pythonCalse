class Productos:
    def __init__(self, product):
        self.product=product
        self.stock= True
    def __str__(self) -> str:
        return 'Producto: %s' %(self.product)
class catalogo:
    ListaCatalogo = []

    def __init__(self,listaCatalogo:list=[]):
        self.ListaCatalogo=listaCatalogo

    def agregar(self, pr):
        self.ListaCatalogo.append(pr)

    def morstraragregado(self):
        for i,pr in enumerate(self.ListaCatalogo):
            i=i+1
            print(i,pr)


p1=Productos('Jabon')
print(p1)
producto=catalogo
producto.agregar(p1)
producto.morstraragregado()



