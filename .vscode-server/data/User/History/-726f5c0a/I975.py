from flask import Flask

app = Flask(__name__)


liste_equipements = []
@app.route('/')
def start():
    


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


if __name__ == "__main__":
   app.run()