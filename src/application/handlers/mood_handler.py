from flask import (
    jsonify,
    request
)
from src.infrastructure.db.repositories.mood_repository import MoodRepository
from src.domain.entity.mood import Mood
import uuid
from datetime import datetime


class MoodHandler:
    def __init__():
        pass

    def handle_get_moods():
        mood_repository = MoodRepository()
        moods = mood_repository.get_all()

        if moods is None:
            return jsonify({
                "error": "Moods not found"
            }), 404

        output = []

        for mood in moods:
            output.append(Mood(mood[0], mood[1], mood[2], mood[3],
                               mood[4], mood[5]).get_value())

        return jsonify(output), 200

    def handle_get_mood(mood_id: str):
        mood_repository = MoodRepository()
        output = mood_repository.get_by_id(str(mood_id))

        if output is None:
            return jsonify({
                "error": "Mood not found"
            }), 404

        mood = Mood(output[0], output[1], output[2], output[3],
                    output[4], output[5], output[6], output[7])

        output = mood.get_value()

        return jsonify(output), 200

    def handle_create_mood():
        data = request.get_json()

        if data is None:
            return jsonify({
                "error": "invalid data"
            }), 400

        try:
            id = uuid.uuid4()
            input = Mood(id, data.get('date'), data.get('feeling'), data.get('intensity'),
                         data.get('comments'), data.get('activity'), datetime.now().strftime("%Y-%m-%d %H:%M:%S"), None)

            output = input.get_value()

            mood_repository = MoodRepository()
            result = mood_repository.create(input)

            if result is None:
                return jsonify({
                    "error": "Mood not created"
                }), 500

        except ValueError as e:
            return jsonify({
                "error": str(e)
            }), 400

        return jsonify(output), 201

    def handle_update_mood(mood_id: str):
        data = request.get_json()

        if data is None:
            return jsonify({
                "error": "invalid data"
            }), 400

        try:
            mood_id = str(mood_id)
            input = Mood(mood_id, data.get('date'), data.get('feeling'), data.get('intensity'),
                         data.get('comments'), data.get('activity'))

            output = input.get_value()
            output['updated_on'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            del output['created_on']

            mood_repository = MoodRepository()
            result = mood_repository.update(input, mood_id)

            output['id'] = mood_id

            if result is None:
                return jsonify({
                    "error": "Mood not updated"
                }), 500

        except ValueError as e:
            return jsonify({
                "error": str(e)
            }), 400

        return jsonify(output), 200

    def handle_delete_mood(mood_id: str):
        if mood_id is None:
            return jsonify({
                "error": "invalid data"
            }), 400

        try:
            mood_id = str(mood_id)
            mood_repository = MoodRepository()

            mood = mood_repository.get_by_id(mood_id)

            if mood is None:
                return jsonify({
                    "error": "Mood not found"
                }), 404

            result = mood_repository.delete(mood_id)

            if result is None:
                return jsonify({
                    "error": "Mood not deleted"
                }), 500

        except ValueError as e:
            return jsonify({
                "error": str(e)
            }), 400

        return jsonify({
            "message": "Mood deleted successfully"
        }), 200
