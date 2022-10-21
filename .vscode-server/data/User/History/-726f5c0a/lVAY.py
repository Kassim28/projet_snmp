from flask import Flask
from pysnmp.hlapi import *

app = Flask(__name__)


liste_equipements = []
@app.route('/')
def start():
    item = 0

    for errorIndication, \
        errorStatus, \
        errorIndex, \
        varBinds in nextCmd(SnmpEngine(),
                            CommunityData('public', mpModel=0),
                            UdpTransportTarget(('demo.snmplabs.com', 161)),
                            ContextData(),
                            ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')),
                            ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
                            ObjectType(ObjectIdentity('IF-MIB', 'ifMtu')),
                            ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed')),
                            ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
                            ObjectType(ObjectIdentity('IF-MIB', 'ifPhysAddress')),
                            lexicographicMode=False):

        print("Item ", item)
        item += 1

        if errorIndication:
            print(errorIndication)
            break
        elif errorStatus:
            print('%s at %s' % (
                    errorStatus.prettyPrint(),
                    errorIndex and varBinds[int(errorIndex)-1][0] or '?'
                )
            )
            break
        else:
            for varBind in varBinds:
                print(' = '.join([ x.prettyPrint() for x in varBind ]))

"""
class nms:
    def start_supervision():    
        

    def stop_supervision():

class gestion_configuration:
    def ajouter_equipement(equipement):
        liste_equipements.append(equipement)
    
    def supprimer_equipement(equipement):
        liste_equipements.append(equipement)

class equipement:
    def __init__(self,nom,type_equipement,adresse_ip):
        self.nom = nom
        self.type_equipement = type_equipement
        self.adresse_ip = adresse_ip

class type_equipement:
    def __init__(self,hostname,cpu,ram,uptime)
        self.hostname = hostname
        self.cpu = cpu
        self.ram = ram
        self.uptime = uptime

    def add_oids():
"""

if __name__ == "__main__":
   app.run()