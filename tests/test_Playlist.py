import datetime

from utils.utils import PlayList

def test_show_best_video():
    pl = PlayList("PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb")
    assert pl.show_best_video() == "https://www.youtube.com/watch?v=9Bv2zltQKQA"
