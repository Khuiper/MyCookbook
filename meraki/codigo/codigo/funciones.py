
import meraki
from Constantes import *


class Funciones:
    _ORG = ORGJUNJI
    dashboard = meraki.DashboardAPI(API,output_log=False,print_console=False)

 
   # Metodo retorna una lista de los id en una Organizacion
   
    @classmethod
    def obtenetTodo(cls):
         response = cls.dashboard.organizations.getOrganizationNetworks(cls._ORG, total_pages='all',per_page=1300)
         print (response)
         
         
         
    @classmethod
    def obtenerListaNerworks(cls):
        response = cls.dashboard.organizations.getOrganizationNetworks(cls._ORG)
        lista = []
        for datos in response:
            datos2 = datos["id"]
            lista.append(datos2)
        return lista 
      
    # Metodo obtiene el nombre de la network pasando por parametro el id 
    @classmethod
    def obtenerNombrePorId(cls, id_net):
        response = cls.dashboard.organizations.getOrganizationNetworks(cls._ORG)
        for datos in response:
            if id_net in datos["id"]:
                nombre = datos["name"]
        return nombre 
      
        
        
    # Metodo retorna la busqueda por nombre y retornna el id de la network
    @classmethod
    def obtenerIdPorNombre(cls, nombre):
        response = cls.dashboard.organizations.getOrganizationNetworks(cls._ORG)
        for datos in response:
            if nombre in datos["name"]:
                id = datos["id"]
        return id    
    
    # Actuealiza vlan en 1 network
    @classmethod
    def actualizarVlan(cls, id_network):
        vlan30='30'
        vlan40='40'
        response= cls.dashboard.appliance.updateNetworkApplianceVlan(id_network,vlan30, dnsNameservers='192.168.100.239\n8.8.8.8')
        response1= cls.dashboard.appliance.updateNetworkApplianceVlan(id_network,vlan40, dnsNameservers='192.168.100.239\n8.8.8.8')
        print(response,response1)
    
    
    # Actualiza  vlans de lista  de networks    
    @classmethod
    def actualizarListaVlan(cls, listaNetworks):
    
        for lista in listaNetworks:
            try:
                vlan30='30'
                vlan40='40'
                cls.dashboard.appliance.updateNetworkApplianceVlan(lista,vlan30, dnsNameservers='192.168.100.239\n8.8.8.8')
                cls.dashboard.appliance.updateNetworkApplianceVlan(lista,vlan40, dnsNameservers='192.168.100.239\n8.8.8.8')
                print(f'Actualizado : {lista}')
            except Exception as e:
                print(f'Vlan no existe: {lista}   {e} ')            
           
       
    # devuelve un los usuarios creados
    @classmethod
    def obtenerUsuarios(cls, network_id):   
        response = cls.dashboard.networks.getNetworkMerakiAuthUsers(network_id)
        print(response)
    
    
    
    # Crea usuarios en la red TEST y entrega permisos de GUEST
    @classmethod
    def crearUsuario(cls,network, email, name, password):         
        response = cls.dashboard.networks.createNetworkMerakiAuthUser(
            network, 
            email,
            name,
            password,
            authorizations=[{'ssidNumber': 0, 'authorizedZone': 'TEST', 'expiresAt': 'Never'}] ,
            accountType='Guest', 
            emailPasswordToUser=False
        )
            
        print(response)
        
    # Recupera los datos de los hub
    @classmethod
    def obtenetSiteToSite(cls, network_id):
        response = cls.dashboard.appliance.getNetworkApplianceVpnSiteToSiteVpn(network_id)
        
        for localSubnet, useVpn in response["subnets"]:
            print (f'subnet {localSubnet}, useVpn {useVpn}')
        
    
    @classmethod
    def obtenerNombreNetwork(cls,network_id):
         response = cls.dashboard.networks.getNetwork(network_id)
         return response['name']
     
    @classmethod
    def obtenerModeloSerial(cls,network_id):
        response = cls.dashboard.networks.getNetworkDevices(network_id)
        listaModelo= []
        listaSerial= []
        for t in list(response):
            modelo = t['model']
            serial = t['serial']
            listaModelo.append(modelo)
            listaSerial.append(serial)
            
        resultado = zip(listaModelo, listaSerial)  
        datos = list(resultado)  
        return datos  

        
    @classmethod
    def actualizarFW(cls):
        networks = cls.dashboard.organizations.getOrganizationNetworks(cls._ORG, total_pages='all')
        product = 'Appliance'
        tag = "prueba"
        try:
            for net in networks:
                if tag in net["tags"]: 
                    if product in net["productTypes"] :
                        print(f'\nAnalyzing network {net["name"]}:')
                        network_id = net['id']
                        response = cls.dashboard.appliance.updateOrganizationApplianceVpnVpnFirewallRules(cls._ORG, rules=[{'comment': 'telefonia.', 'policy': 'allow', 'protocol': 'Any', 'destPort': 'any', 'destCidr': '10.201.24.36/32', 'srcPort': 'Any', 'srcCidr': '10.113.36.192/26', 'syslogEnabled': False}]
                    
                        )
                        print(response)
                    
        except Exception as e:
            print(f'some other error: {e}')
            
    # Metodo ovtiene lista de vlans en network con su subnet
    @classmethod
    def ObtenerVlans(cls, serial):
        try:
            response = cls.dashboard.appliance.getDeviceApplianceDhcpSubnets(serial)
            ListavlanId = []
            Listasubnet= []
            for t in list(response):
                    vlan = t['vlanId']
                    subnet = t['subnet']
                    ListavlanId.append(vlan)
                    Listasubnet.append(subnet)
            resultado = zip(ListavlanId, Listasubnet)  
            datos = list(resultado)  
            return datos               
        except Exception as e:
            print(f'some other error: {e}') 

     
    
    @classmethod
    def obtenerStatus(cls, id_net):
        response =cls.dashboard.organizations.getOrganizationUplinksStatuses(cls._ORG, total_pages='all')
                
        for datos in response:
            if id_net in datos['networkId']:
                interface=[]
                statuses=[]
                status = datos['uplinks']
                for d in status:
                    du=d['status']
                    a=d['interface']
                    interface.append(a)
                    statuses.append(du)
                result =  zip(interface, statuses)  
                lista = list(result)                    
        return lista
    
    
    @classmethod
    def obtenerProvider(cls):
        response = cls.dashboard.cellularGateway.getOrganizationCellularGatewayUplinkStatuses(cls._ORG)
        print(response)
        
    
    @classmethod
    def obtenerPrueba(cls):
        response =cls.dashboard.organizations.getOrganizationUplinksStatuses(cls._ORG, total_pages='all',per_page=1300)
        for datos in response:
            id = datos['networkId']
            nombre=cls.obtenerNombreNetwork(id)
            for up in datos['uplinks']:
                try:    
                    if up['interface']=='cellular': 
                        interface= up['interface']
                        status=up['status']
                        
                        provider=up['provider']
                        if provider:
                            provider=up['provider']
                        else:
                            provider='sin datos'    
                        dic=up['signalStat']
                        if dic:
                            rp=dic['rsrp']
                            rq=dic['rsrq']
                        else:
                            rp='sin datos'
                            rq='sin datos'
                        print(f'{nombre}, {interface}, {status},{rp}, {rq}, {provider}')
                except Exception as e:
                    print(f'3G {nombre}:   {e} ') 
                
     
     # Lista todas las Networks, imprime datos de señal
    @classmethod
    def obtenerListaCellular(cls):
        response =cls.dashboard.organizations.getOrganizationUplinksStatuses(cls._ORG, total_pages='all',per_page=1300)
        filtro=[]
        for datos in response:
            id = datos['networkId']
            nombre=cls.obtenerNombreNetwork(id)
            for up in datos['uplinks']:
                try:    
                    if up['interface']=='cellular': 
                        interface= up['interface']
                        status=up['status']
                        
                        provider=up['provider']
                        if provider:
                            provider=up['provider']
                        else:
                            provider='sin datos'    
                        dic=up['signalStat']
                        if dic:
                            rp=dic['rsrp']
                            rq=dic['rsrq']
                        else:
                            rp='sin datos'
                            rq='sin datos'
                        filtro.append([nombre,interface,status,rp ,rq, provider])    
                except Exception as e:
                    print(f'3G {nombre}:   {e} ') 
        return filtro           
   
    @classmethod
    def obtenerVlaNetwork(cls, id_network):
        try:
            nombre=cls.obtenerNombrePorId(id_network)
            response =cls.dashboard.appliance.getNetworkApplianceVlans(id_network)
            for datos in response:
                vlan = datos['id']
                dns = datos['dnsNameservers']
                if dns != '192.168.100.239\n8.8.8.8':
                    if vlan == 30 or vlan == 40:
                        print(f'{nombre}, vlan: {vlan}')
        except Exception as e:
                 print(f' no existe la vlan:   {e} ')         
                     