from utils.utils import PLVideo

def test_str():
    plvideo = PLVideo("BBotskuyw_M", "PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD")
    assert plvideo.__str__() == "Название видео: Пушкин: наше все? Название плейлиста: Литература"