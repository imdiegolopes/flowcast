from src.application.handlers.mood_handler import MoodHandler
from handlers.healthcheck_handler import HealthcheckHandler
from flask import (
    Flask
)
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

app.add_url_rule('/', 'index', HealthcheckHandler.handle, methods=['GET'])
app.add_url_rule('/healthcheck', 'healthcheck',
                 HealthcheckHandler.handle, methods=['GET'])
app.add_url_rule('/v1/moods', 'get_moods',
                 MoodHandler.handle_get_moods, methods=['GET'])
app.add_url_rule('/v1/moods/<uuid:mood_id>', 'get_mood',
                 MoodHandler.handle_get_mood, methods=['GET'])
app.add_url_rule('/v1/moods', 'create_mood',
                 MoodHandler.handle_create_mood, methods=['POST'])
app.add_url_rule('/v1/moods/<uuid:mood_id>', 'update_mood',
                 MoodHandler.handle_update_mood, methods=['PUT'])
app.add_url_rule('/v1/moods/<uuid:mood_id>', 'delete_mood',
                 MoodHandler.handle_delete_mood, methods=['DELETE'])


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
