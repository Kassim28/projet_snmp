from flask import Flask
app = Flask(__name__)


liste_equipements = []
@app.route('/')
def 


class nms:
    def start_supervision():    
        
    def stop_supervision():

class gestion_configuration:
    def add_equipement(equipement):
        liste_equipements.append(equipement)

class equipement:
    def __init__(self,nom,type_equipement,adresse_ip,):
        self.nom = nom
        self.type_equipement = type_equipement
        self.adresse_ip = adresse_ip

    def add_oids():


class type_device:
    def __init__(self,hostname,cpu,ram,uptime,)


if __name__ == "__main__":
   app.run()