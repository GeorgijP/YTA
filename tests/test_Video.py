import pytest
from utils.utils import Video


def test_str():
    video_1 = Video("-y_5drHpY1A")
    assert video_1.__str__() == f"Название видео: {video_1.video_name}"

def test_except_Video():
    with pytest.raises(Exception):
        video = Video("-y_5drHp**")
        assert video.video_name == "None"
