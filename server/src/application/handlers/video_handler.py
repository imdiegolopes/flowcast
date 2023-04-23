from flask import (
    jsonify
)
import json

from src.infrastructure.db.repositories.video_repository import VideoRepository


class VideoHandler:
    def __init__():
        pass

    def handle_create_video():
        pass

    def handle_get_videos():
        video_repository = VideoRepository()
        output = video_repository.get_all()

        if output is None:
            return jsonify({
                "error": "Videos not found"
            }), 404
        output = json.dumps(output)

        return jsonify(output)

    def handle_get_video(video_id: str):
        video_repository = VideoRepository()
        output = video_repository.get_by_id(video_id)

        if output is None:
            return jsonify({
                "error": "Video not found"
            }), 404
        output = json.dumps(output)

        return jsonify(output)