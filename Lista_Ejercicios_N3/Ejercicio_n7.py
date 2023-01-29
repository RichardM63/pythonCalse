class Producto:
    def __init__(self, nombre, codigo):
        self.nombre=nombre
        self.codigo=codigo
    def __str__(self) -> str:
        return 'El codigo de %s es de %s y esta ubicado en %s con lote de %s' %(self.nombre,self.codigo,C1[0],C1[1]) 

p1 =Producto('Jose','Peru-0004-2023')
C1=p1.codigo.split(sep='-')
print(p1)