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
    def __init__(self,hostname,type_device,adresse_ip,communauté):
        self.hostname = hostname
        self.type_device = type_device
        self.adresse_ip = adresse_ip
        self.communauté = communauté

    def add_oids():





if __name__ == "__main__":
   app.run()