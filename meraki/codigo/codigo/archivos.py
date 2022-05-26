import openpyxl
from Funciones import *  
from operator import itemgetter 
import random as rd

lista =Funciones.obtenerListaNerworks()

for id_network in lista:
    print(id_network)
    
    nombreNetwork=Funciones.obtenerNombreNetwork(id_network)
    modelo=Funciones.obtenerModeloSerial(id_network)
    try:
        modeloMX = modelo[0][0]
        serie = modelo[0][1]
   
    except Exception as e:
        print(f'Vlan no existe: {lista}   {e} ')  

    try:
    
        vlans = Funciones.ObtenerVlans(serie)
        orden=sorted(vlans, key=itemgetter(0))
        if orden[0][0]==1:
            del(orden[0])
    
        vlan777=''
        vlan30=''
        vlan40=''    
    
        vlan30=orden[0][1]
        vlan40=orden[1][1]
        vlan777=orden[2][1]
        
    except Exception as e:
            print(f'Vlan no existe:   {e} ')  
            

    book = openpyxl.load_workbook('a.xlsx')
    sheet = book.active
    
    nombreLista=['Franco Rojas','Reinaldo Gonzales','Nisledys Elian','Ignacio Velasques','Sebastian Ortega']
    cantidad= len(nombreLista)
    aletorio=rd.randrange(cantidad)       
    try:
        sheet['B4']=nombreLista[aletorio]
        sheet['B7']=nombreNetwork
        sheet['B8']=nombreNetwork
        sheet['B13']=modeloMX
        sheet['B14']=vlan777
        sheet['B15']=vlan40
        sheet['B16']=vlan30
    except Exception as e:
        print(f'Vlan no existe:   {e} ')     
    book.save(nombreNetwork +'.xlsx')