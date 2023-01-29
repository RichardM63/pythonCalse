class Productos:
    def __init__(self, product):
        self.product=product
        self.stock= True
    def __str__(self) -> str:
        return 'Producto: %s' %(self.product)
class catalogo:
    ListaCatalogo = []
    def __init__(self,listCatalogo:list=[]):
        self.ListaCatalogo=listCatalogo
    def agregar(self,p):
        self.ListaCatalogo.append(p)
    def morstraragregado(self):
        for p in self.ListaCatalogo:
            print(p)
try:
    p1=Productos('Jabon')
    print(p1)
    producto=catalogo
    producto.agregar(p1)
    producto.morstraragregado()
except Exception as e:
    print('Hay un error')
    print(e)


