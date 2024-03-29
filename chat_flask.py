from flask import Flask, render_template
from flask_socketio import SocketIO, send
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

# getenv coge el archivo .env y lo carga como variables de entorno
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# cuando el cliente escriba un mensaje hara trigger a funcion de abajo, nombre del evento
# la funcion tiene que estar debajo del @ para saber que funcion activa
@socketio.on('message') #esta escuchando a ver que recibe, espera el evento message
def handleMessage(msg):
    print("Message:", msg)
    send(msg, broadcast = True)
    

if __name__ == '__main__':
    socketio.run(app, port=3000, debug=True)
    # para que sea visible y accesible en la red desde cualquier punto (0.0.0.0)
    # socketio.run(app, port=3000, debug=True, host="0.0.0.0")