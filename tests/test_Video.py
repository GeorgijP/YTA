from utils.utils import Video


def test_str():
    video = Video("-y_5drHpY1A")
    assert video.__str__() == "Название видео: ЦАРЬ в ралли - КАРЕЛИЯ"

