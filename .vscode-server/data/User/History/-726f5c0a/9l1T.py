from flask import Flask
from pysnmp.hlapi import *

app = Flask(__name__)


liste_equipements = []
@app.route('/')
def start():
    ####################################################################
    #SNMP WALK
    ####################################################################
    item = 0

    data = (
    ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifOutOctets')),
    ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed')),
    )
    size_oids = len(data)

    for errorIndication, \
        errorStatus, \
        errorIndex, \
        varBinds in nextCmd(SnmpEngine(),
                            CommunityData('snmp_kas', mpModel=0),
                            UdpTransportTarget(('pc1', 161)),
                            ContextData(),
                            *data,
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
        for i in range(size_oids-1):
            print("This is the oid value " + str(varBinds[i][1]))

#########################################################################################################
# SNMP GET LISTE
############################################################################################ 
    data1 = (
    ObjectType(ObjectIdentity('DISMAN-EVENT-MIB', 'sysUpTimeInstance')),
    ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0))
    )

    g = getCmd(SnmpEngine()
            , CommunityData('snmp_kas', mpModel=0)
            , UdpTransportTarget(('pc1', 161))
            , ContextData()
            , *data1)

    errorIndication, errorStatus, errorIndex, varBinds = next(g)

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (
                            errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'
                        )

            )
    else:
        for varBind in varBinds:
            test = varBind
            print(' = '.join([x.prettyPrint() for x in varBind]))
            print("This is x " + str(varBinds[0][1]))
#
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