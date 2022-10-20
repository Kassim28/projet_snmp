from flask import Flask
app = Flask(__name__)

@app.route('/')
class serveur():
    return 'Hello, World!'

if __name__ == "__main__":
   app.run()