from flask import (
    jsonify,
    request
)
from src.infrastructure.db.repositories.video_repository import VideoRepository
from src.domain.entity.video import Video


class VideoHandler:
    def __init__():
        pass

    def handle_get_videos():
        video_repository = VideoRepository()
        videos = video_repository.get_all()

        if videos is None:
            return jsonify({
                "error": "Videos not found"
            }), 404

        output = []

        for video in videos:
            output.append(Video(video[0], video[1], video[2], video[3],
                                video[4], video[5], video[6], video[7]).get_value())

        return jsonify(output), 200

    def handle_get_video(video_id: str):
        video_repository = VideoRepository()
        output = video_repository.get_by_id(video_id)
        video = Video(output[0], output[1], output[2], output[3],
                      output[4], output[5], output[6], output[7])

        if output is None or video is None:
            return jsonify({
                "error": "Video not found"
            }), 404

        output = video.get_value()

        return jsonify(output), 200

    def handle_create_video():
        data = request.get_json()

        if data is None:
            return jsonify({
                "error": "invalid data"
            }), 400

        try:
            input = Video(None, data.get('title'), data.get('description'), data.get('url'),
                          data.get('duration'), data.get('thumbnail_url'), data.get('published_at'), data.get('channel_id'))

            output = input.get_value()

            video_repository = VideoRepository()
            result = video_repository.create(input)

            if result is None:
                return jsonify({
                    "error": "video not created"
                }), 500

            output['id'] = result

        except ValueError as e:
            return jsonify({
                "error": str(e)
            }), 400

        return jsonify(output), 201

    def handle_update_video(video_id: str):
        data = request.get_json()

        if data is None:
            return jsonify({
                "error": "invalid data"
            }), 400

        try:
            input = Video(None, data.get('title'), data.get('description'), data.get('url'),
                          data.get('duration'), data.get('thumbnail_url'), data.get('published_at'), data.get('channel_id'))

            output = input.get_value()

            video_repository = VideoRepository()
            result = video_repository.update(input, video_id)

            output['id'] = video_id

            if result is None:
                return jsonify({
                    "error": "video not updated"
                }), 500

        except ValueError as e:
            return jsonify({
                "error": str(e)
            }), 400

        return jsonify(output), 200

    def handle_delete_video(video_id: str):
        if video_id is None:
            return jsonify({
                "error": "invalid data"
            }), 400

        try:
            video_id = int(video_id)

            video_repository = VideoRepository()
            result = video_repository.delete(video_id)

            if result is None:
                return jsonify({
                    "error": "video not deleted"
                }), 500

        except ValueError as e:
            return jsonify({
                "error": str(e)
            }), 400

        return jsonify({}), 200
