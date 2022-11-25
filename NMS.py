from flask import Flask, render_template, redirect, request
from pysnmp.hlapi import *
import time
import pygal
import mysql.connector as database
import datetime
import json


app = Flask(__name__)


liste_equipements = []
liste_oid = []

connection = database.connect(
    user="kas",
    password="password",
    host="localhost",
    database="snmp")

cur = connection.cursor()

def add_data(ip,inoctets,outoctets):
    try:
        statement = "INSERT INTO octects (ip_address,inoctets,outoctets) VALUES (%s,%s,%s)"
        data = (ip,inoctets,outoctets)
        cur.execute(statement, data)
        connection.commit()
        print("Successfully added entry to database")
    except database.Error as e:
        print(f"Error adding entry to database: {e}")


@app.route('/supervision', methods=['GET', 'POST'])
def start():
    ####################################################################
    #SNMP WALK LISTE
    ##############################################################


    while 1==1:
        item = 0
        OutOctets = 0
        InOctets = 0

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
                if item == 3:
                    if i == 1:
                        InOctets = varBinds[i][1]
                    elif i == 2:
                        OutOctets = varBinds[i][1]
            #rrdtool.update("myrouter.rrd", "N:" + str(InOctets) + ":" + str(OutOctets))
            
            add_data("192.168.56.4",int(InOctets) ,int(OutOctets))
            time.sleep(10)   
            print("In Octets are: " + str(InOctets))
            print("Out Octets are: " + str(OutOctets))                 

                
    #########################################################################################################
    # SNMP GET LISTE
    ############################################################################################ 
        
        data1 = (
        ObjectType(ObjectIdentity('DISMAN-EXPRESSION-MIB', 'sysUpTimeInstance')),
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
                print("This is the uptime " + str(round(varBinds[0][1]/100/60)) + " minutes.")
    #





@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/equipement', methods=['GET', 'POST'])
def equipements():
    return render_template('equipements.html')


#show add_equipements form
@app.route('/equipement/add-equipement', methods=['GET', 'POST'])
def add_equipements():
    if request.method == "POST":
        nom = request.form.get("name")
        adresse_ip = request.form.get("ip")
        type_equipement = request.form.get("type")
        liste_equipements.append([nom,adresse_ip,type_equipement])
        print(liste_equipements)
    return render_template('add_equipement.html')



@app.route('/equipement/edit-equipement', methods=['GET', 'POST'])
def edit_equipemnts():
    return render_template('edit_equipement.html')

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