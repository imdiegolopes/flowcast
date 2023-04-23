from flask import (
    Flask, 
    jsonify
)
from handlers.healthcheck import Healthcheck

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/videos')
def create_video():
    return jsonify({'status': 'ok'})

@app.route('/videos/<video_id>')
def get_video(video_id):
    if not video_id:
        return jsonify({'status': 'error', 'message': 'video_id is required'})
    return jsonify({'status': 'ok'})

@app.route('/videos/<video_id>', methods=['PUT'])
def update_video(video_id):
    return jsonify({'status': 'ok'})

@app.route('/videos/<video_id>', methods=['DELETE'])
def delete_video(video_id):
    return jsonify({'status': 'ok'})

app.add_url_rule('/healthcheck', 'healthcheck', Healthcheck.handle, methods=['GET'])

if __name__ == '__main__':
    app.run(debug = True, use_reloader = True)