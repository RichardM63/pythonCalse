texto='Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. \
Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un \
impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos \
y los mezcló de tal manera que logró hacer un libro de textos especimen.'
#############################
print(texto.split(sep=' '))
#############################
a= texto.split(sep=' ')
#-------------------------
print('-'.join(texto))
#-------------------------
print('-'.join(a))
#-------------------------
a =texto.count('Lorem')
print('La cantidad de veces que se repite Lorem es de %s veces' %(a))
#############################
b =texto.find('simplemente')
print('La palabra simplemente se ubica en el lugar %s' %(b))
#############################
print(texto.upper())
#############################
print(texto.lower())
