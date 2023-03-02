from utils.utils import Youtube_anal


# не понимаю как решить проблему с тем, что "hiddenSubscriberCount": false, а не False
# def test_print_info():
#     assert item.print_info() == {"kind": "youtube#channelListResponse", "etag": "dZkh-ks2iVjMNBgZ-m8yY4i-1GM", "pageInfo": {"totalResults": 1, "resultsPerPage": 5}, "items": [{"kind": "youtube#channel", "etag": "I5ySzB13Adbjyg8HMLl9cq-yURU", "id": "UClI9aidW3X044NeB4QS-yxw", "snippet": {"title": "\u0410\u043d\u0442\u043e\u043d \u041f\u0442\u0443\u0448\u043a\u0438\u043d", "description": "", "customUrl": "@ptuxermann", "publishedAt": "2008-04-01T20:42:14Z", "thumbnails": {"default": {"url": "https://yt3.ggpht.com/ytc/AL5GRJU4OZNH6V5aLmYRUtX4DjrDt8bLtujX01M5wJlF4A=s88-c-k-c0x00ffffff-no-rj", "width": 88, "height": 88}, "medium": {"url": "https://yt3.ggpht.com/ytc/AL5GRJU4OZNH6V5aLmYRUtX4DjrDt8bLtujX01M5wJlF4A=s240-c-k-c0x00ffffff-no-rj", "width": 240, "height": 240}, "high": {"url": "https://yt3.ggpht.com/ytc/AL5GRJU4OZNH6V5aLmYRUtX4DjrDt8bLtujX01M5wJlF4A=s800-c-k-c0x00ffffff-no-rj", "width": 800, "height": 800}}, "localized": {"title": "\u0410\u043d\u0442\u043e\u043d \u041f\u0442\u0443\u0448\u043a\u0438\u043d", "description": ""}, "country": "UA"}, "statistics": {"viewCount": "596156368", "subscriberCount": "5630000", "hiddenSubscriberCount": false, "videoCount": "95"}}]}

def test_str():
    item_1 = Youtube_anal("UClI9aidW3X044NeB4QS-yxw", "YT_API_KEY")
    assert item_1.__str__() == "Youtube-канал: Антон Птушкин"

def test_lt():
    item_1 = Youtube_anal("UClI9aidW3X044NeB4QS-yxw", "YT_API_KEY")
    item_2 = Youtube_anal("UCEVNTzTFSGkZGTjVE9ipXpg", "YT_API_KEY")
    assert item_2.__lt__(item_1) is True

def test_add():
    item_1 = Youtube_anal("UClI9aidW3X044NeB4QS-yxw", "YT_API_KEY")
    item_2 = Youtube_anal("UCEVNTzTFSGkZGTjVE9ipXpg", "YT_API_KEY")
    assert item_1 + item_2 == 7230000
