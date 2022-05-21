import openpyxl
from Funciones import *  

contador = 1
book = openpyxl.load_workbook('datos.xlsx')
datosList=Funciones.obtenerListaCellular()

for dato in datosList:
    try:  
        contador = contador + 1    
        nombre = dato[0]
        enlace = dato[1]
        estado = dato[2]
        rp = dato[3]
        rq = dato[4]
        proveedor = dato[5]
        
        
        sheet = book.active
        sheet[f'A{contador}']=nombre
        sheet[f'B{contador}']=enlace
        sheet[f'C{contador}']=estado
        sheet[f'D{contador}']=rp
        sheet[f'E{contador}']=rq
        sheet[f'F{contador}']=proveedor

    except Exception as e:
            print(f'Datos con errores:   {e} ')     
book.save(f'datos.xlsx')