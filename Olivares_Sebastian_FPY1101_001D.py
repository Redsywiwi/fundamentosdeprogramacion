import os
def c():
    os.system('cls')
#           modelo      marca     pantalla   RAM    disco  tamaño disc procesador      video
productos={'8475HD':    ['HP',      15.6,   '8GB',  'HDD', '1T',        'Intel Core i5',    'Nvidia GTX1050'],
            '2175HD':   ['lenovo',  14,     '4GB',  'SSD', '512GB',     'Intel Core i5',    'Nvidia GTX1050'],
            'JjfFHD':   ['Asus',    14,     '16GB', 'SSD', '256GB',     'Intel Core i7',    'Nvidia RTX2080Ti'],
            'fgdxFHD':  ['HP',      15.6,   '8GB',  'HDD', '1T',        'Intel Core i3',    'integrada'],
            'GF75HD':   ['Asus',    15.6,   '8GB',  'HDD', '1T',        'Intel Core i7',    'Nvidia GTX1050'],
            '123FHD':   ['lenovo',  14,     '6GB',  'HDD', '1T',        'AMD Ryzen 5',      'integrada'],
            '342FHD':   ['lenovo',  15.6,   '8GB',  'HDD', '1T',        'AMD Ryzen 7',      'Nvidia GTX1050'],
            'UWU131HD': ['Dell',    15.6,   '8GB',  'HDD', '1T',        'AMD Ryzen 3',      'Nvidia GTX1050']
           }

#   modelo      precio      stock
stock = {
    '8475HD':   [387990,    10], 
    '2175HD':   [327990,    4], 
    'JjfFHD':   [424990,    1],
    'fgdxFHD':  [664990,    21], 
    '123FHD':   [290890,    32], 
    '342FHD':   [444990,    7],
    'GF75HD':   [749990,    2], 
    'UWU131HD': [349990,    1], 
    'FS1230HD': [249990,    0]
}
def stocks(MARCAINPUT):
    stock_suma=0
    for producto in productos:
        m= (productos[producto])[0]
        if MARCAINPUT.lower()==m.lower():
            s=(stock[producto])[1]
            stock_suma+=s
    print(f"{MARCAINPUT.lower()}: {stock_suma}")
    input("")

def busqueda_precio(min,max):
    for C in stock:
        if min<=stock[0] and max>=stock[0]:
            

while True:
    c()
    print("-----MENU-----")
    print("1- Stock marca \n2- Busqueda por precio \n3- Actualizar precio\n4- Salir")
    try: seleccion=int(input("\n"))
    except ValueError: continue
    
    #----- CONSULTA PRECIO -----
    if seleccion==1:
        c()
        MARCAINPUT=input("Que marca desea buscar\n\n")
        stocks(MARCAINPUT)


    #----- BUSQUEDA POR PRECIO -----
    elif seleccion==2:
        c()
        try: 
            min=int(input("ingrese el monto menor\n"))
            max=int(input("ingrese el monto mayor\n"))
            busqueda_precio(min,max)
        except ValueError: print("el numero ingresado no es valido, abortando"); input(""); continue
                                 
    
    #----- ACTUALIZAR PRECIO -----
    elif seleccion==3:
        c()
        modelo=input("Ingrese el modelo a actualizar (debe ser exacto)\n")
        try: nuevoprecio=int(input("Ingrese el nuevo precio\n"))
        except ValueError: print("el numero ingresado no es valido, abortando"); input(""); continue

        print()


    #----- CERRAR -----
    elif seleccion==4:
        c()
        print("Cerrando programa")
        break