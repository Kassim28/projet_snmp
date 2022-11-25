from flask import Flask, render_template, redirect, request
from pysnmp.hlapi import *
import time
import pygal
import mysql.connector as database
import datetime
import json
import os


app = Flask(__name__)


liste_equipements = []
liste_oids = []

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

        

        def construct_object_types(self,liste_oids):
        object_types = []
        for oid in list_of_oids:
            object_types.append(hlapi.ObjectType(hlapi.ObjectIdentity(oid)))
        return object_types

    def construct_value_pairs(self, list_of_pairs):
        pairs = []
        for key, value in list_of_pairs.items():
            pairs.append(hlapi.ObjectType(hlapi.ObjectIdentity(key), value))
        return pairs

    def cast(self, value):
        try:
            return int(value)
        except (ValueError, TypeError):
            try:
                return float(value)
            except (ValueError, TypeError):
                try:
                    return str(value)
                except (ValueError, TypeError):
                    pass
        return value

    def fetch(self, handler, count):
        result = []
        for i in range(count):
            try:
                error_indication, error_status, error_index, var_binds = next(handler)
                if not error_indication and not error_status:
                    items = {}
                    for var_bind in var_binds:
                        items[str(var_bind[0])] = self.cast(var_bind[1])
                    result.append(items)
                else:
                    raise RuntimeError('Got SNMP error: {0}'.format(error_indication))
            except StopIteration:
                break
        return result

    def get(self, target, oids, port=161, engine=hlapi.SnmpEngine(), context=hlapi.ContextData()):
        handler = hlapi.nextCmd(
            engine,
            hlapi.CommunityData('snmp_kas'),
            hlapi.UdpTransportTarget((target, port)),
            context,
            *self.construct_object_types(oids)
        )
        return self.fetch(handler, 1)[0]

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
            time.sleep(60)   
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

"""



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/equipement', methods=['GET', 'POST'])
def equipements():
    cur.execute("select * from equipements")
    sqldata = cur.fetchall()
    return render_template('equipements.html',sqldata=list(sqldata))


#show add_equipements form
@app.route('/equipement/add-equipement', methods=['GET', 'POST'])
def add_equipements():
    def add(nom,type_equipement,ip):
        try:
            statement = "INSERT INTO equipements (nom,type,ip) VALUES (%s,%s,%s)"
            data = (nom,type_equipement,ip)
            cur.execute(statement, data)
            connection.commit()
            print("Successfully added entry to database")
        except database.Error as e:
            print(f"Error adding entry to database: {e}")

    if request.method == "POST":
        nom = request.form.get("name")
        adresse_ip = request.form.get("ip")
        type_equipement = request.form.get("type")
        add_data(nom,type_equipement,adresse_ip)
        liste_equipements.append([nom,adresse_ip,type_equipement])
        
    return render_template('add_equipement.html')


@app.route('/equipement/edit-equipement', methods=['GET', 'POST'])
def edit_equipemnts():
    def edit():
        try:
            statement = "update equipements set  VALUES (%s)"
            data = (id)
            cur.execute(statement, data)
            connection.commit()
            print("Successfully deleted entry from database")
        except database.Error as e:
            print(f"Error deleting entry from database: {e}")

        if request.method == "POST":
            nom = request.form.get("name")
            adresse_ip = request.form.get("ip")
            type_equipement = request.form.get("type")
            add_data(nom,type_equipement,adresse_ip)
            liste_equipements.append([nom,adresse_ip,type_equipement])
    return redirect('/equipement')

@app.route('/equipement/<id>/delete-equipement', methods=['GET', 'POST'])
def delete_equipemnt(id):
    try:
        statement = "DELETE FROM equipements WHERE id=" + id
        cur.execute(statement)
        connection.commit()
        print("Successfully deleted entry from database")
    except database.Error as e:
        print(f"Error deleting entry from database: {e}")
    return redirect('/equipement')

@app.route('/oid', methods=['GET', 'POST'])
def oids():
    cur.execute("select * from oids")
    sqldata = cur.fetchall()
    return render_template('oids.html',sqldata=list(sqldata))

@app.route('/equipement/add-oid', methods=['GET', 'POST'])
def add_oids():
    def add(desc,oid):
        try:
            statement = "INSERT INTO oids (description,oid) VALUES (%s,%s)"
            data = (desc,oid)
            cur.execute(statement, data)
            connection.commit()
            print("Successfully added entry to database")
        except database.Error as e:
            print(f"Error adding entry to database: {e}")

    if request.method == "POST":
        desc = request.form.get("desc")
        oid = request.form.get("oid")
        add(desc,oid)
        liste_oids.append([desc,oid])
        
    return render_template('add_oid.html')

@app.route('/equipement/<id>/delete-oid', methods=['GET', 'POST'])
def delete_oid(id):
    try:
        statement = "DELETE FROM oids WHERE id=" + id
        cur.execute(statement)
        connection.commit()
        print("Successfully deleted entry from database")
    except database.Error as e:
        print(f"Error deleting entry from database: {e}")
    return redirect('/oid')
"""
class nms:
    def start_supervision():    
        

    def stop_supervision():

class gestion_configuration:
    def ajouter_equipement(equipement):
        liste_equipements.append(equipement)
    
    def supprimer_equipement(equipement):
        liste_equipements.append(equipement)



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