from flask import Flask
app = Flask(__name__)

@app.route('/')
class serveur():
    return 'Hello, World!'

def nms():

class equipement:
    def __init__(self,hostname,type_device,adresse_ip,communauté):
        self.hostname = hostname
        self.type_device = type_device
        self.adresse_ip = adresse_ip
        self.communauté = communauté










if __name__ == "__main__":
   app.run()