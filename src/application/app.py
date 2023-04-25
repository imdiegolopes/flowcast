from handlers.video_handler import VideoHandler
from handlers.healthcheck_handler import HealthcheckHandler
from flask import (
    Flask,
    jsonify
)

app = Flask(__name__)

app.add_url_rule('/', 'index', HealthcheckHandler.handle, methods=['GET'])
app.add_url_rule('/healthcheck', 'healthcheck',
                 HealthcheckHandler.handle, methods=['GET'])
app.add_url_rule('/v1/videos', 'get_videos',
                 VideoHandler.handle_get_videos, methods=['GET'])
app.add_url_rule('/v1/videos/<video_id>', 'get_video',
                 VideoHandler.handle_get_video, methods=['GET'])
app.add_url_rule('/v1/videos', 'create_video',
                 VideoHandler.handle_create_video, methods=['POST'])
app.add_url_rule('/v1/videos/<video_id>', 'update_video',
                 VideoHandler.handle_update_video, methods=['PUT'])
app.add_url_rule('/v1/videos/<video_id>', 'delete_video',
                 VideoHandler.handle_delete_video, methods=['DELETE'])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
