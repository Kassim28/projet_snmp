from flask import Flask
app = Flask(__name__)


list_equipements = []
@app.route('/')
class nms():
    def start_supervision():

    def stop_supervision():

class equipement:
    def __init__(self,hostname,type_device,adresse_ip,communauté):
        self.hostname = hostname
        self.type_device = type_device
        self.adresse_ip = adresse_ip
        self.communauté = communauté







if __name__ == "__main__":
   app.run()