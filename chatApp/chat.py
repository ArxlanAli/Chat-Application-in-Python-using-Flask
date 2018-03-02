from flask import Flask,render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)
app.config['secret_key'] = "absahsghasg1212"
socketio = SocketIO( app )
clients = []


@app.route('/')

def index():
	return render_template( './ChatLayout.html' )


@socketio.on('request')
def handle_event(json):
	socketio.emit('response',json) 





if __name__ == '__main__':
	socketio.run(app,debug = True)
