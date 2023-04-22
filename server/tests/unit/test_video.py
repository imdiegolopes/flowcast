# from src.domain.entity.video import Video
import pytest
from src.domain.entity.video import Video


def test_video_init():
    video = Video(
        id="test_id",
        title="test_title",
        description="test_description",
        url="http://mock.com",
        thumbnail_url="http://mock.com/image.jpg",
        duration=100,
        published_at="test_published_at",
        channel_id="test_channel_id",
    )
    assert video.id == "test_id"
    assert video.title == "test_title"
    assert video.description == "test_description"
    assert video.url == "http://mock.com"
    assert video.duration == 100
    assert video.thumbnail_url == "http://mock.com/image.jpg"
    assert video.published_at == "test_published_at"
    assert video.channel_id == "test_channel_id"


def test_video_get_value():
    video = Video(
        id="test_id",
        title="test_title",
        description="test_description",
        url="http://mock.com",
        thumbnail_url="http://mock.com/image.jpg",
        duration=100,
        published_at="test_published_at",
        channel_id="test_channel_id",
    )
    assert video.get_value() == {
        "id": "test_id",
        "title": "test_title",
        "description": "test_description",
        "url": "http://mock.com",
        "thumbnail_url": "http://mock.com/image.jpg",
        "duration": 100,
        "published_at": "test_published_at",
        "channel_id": "test_channel_id",
    }


def test_video_should_raise_error_when_title_is_none():
    with pytest.raises(ValueError) as Error:
        Video(
            id="test_id",
            title=None,
            description="test_description",
            url="http://mock.com",
            thumbnail_url="http://mock.com/image.jpg",
            duration=100,
            published_at="test_published_at",
            channel_id="test_channel_id",
        )

    assert str(Error.value) == "title is required"


def test_video_should_raise_error_when_description_is_none():
    with pytest.raises(ValueError) as Error:
        Video(
            id="test_id",
            title="test_title",
            description=None,
            url="http://mock.com",
            thumbnail_url="http://mock.com/image.jpg",
            duration=100,
            published_at="test_published_at",
            channel_id="test_channel_id",
        )

    assert str(Error.value) == "description is required"

def test_video_should_raise_error_when_url_is_none():
    with pytest.raises(ValueError) as Error:
        Video(
            id="test_id",
            title="test_title",
            description="test_description",
            url=None,
            thumbnail_url="http://mock.com/image.jpg",
            duration=100,
            published_at="test_published_at",
            channel_id="test_channel_id",
        )

    assert str(Error.value) == "url is required"

def test_video_should_raise_error_when_thumbnail_url_is_none():
    with pytest.raises(ValueError) as Error:
        Video(
            id="test_id",
            title="test_title",
            description="test_description",
            url="http://mock.com",
            thumbnail_url=None,
            duration=100,
            published_at="test_published_at",
            channel_id="test_channel_id",
        )

    assert str(Error.value) == "thumbnail_url is required"

def test_video_should_raise_error_when_duration_is_none():
    with pytest.raises(ValueError) as Error:
        Video(
            id="test_id",
            title="test_title",
            description="test_description",
            url="http://mock.com",
            thumbnail_url="http://mock/image.jpg",
            duration=None,
            published_at="test_published_at",
            channel_id="test_channel_id",
        )

    assert str(Error.value) == "duration is required"

def test_video_should_raise_error_when_duration_is_less_than_zero():
    with pytest.raises(ValueError) as Error:
        Video(
            id="test_id",
            title="test_title",
            description="test_description",
            url="http://mock.com",
            thumbnail_url="http://mock.com/image.jpg",
            duration=-1,
            published_at="test_published_at",
            channel_id="test_channel_id",
        )

    assert str(Error.value) == "duration should be greater than zero"

def test_video_should_raise_error_when_published_at_is_none():
    with pytest.raises(ValueError) as Error:
        Video(
            id="test_id",
            title="test_title",
            description="test_description",
            url="http://mock.com",
            thumbnail_url="http://mock.com/image.jpg",
            duration=100,
            published_at=None,
            channel_id="test_channel_id",
        )

    assert str(Error.value) == "published_at is required"

