import json
from utils.utils import Youtube_anal

item = Youtube_anal("UClI9aidW3X044NeB4QS-yxw", "YT_API_KEY")

data = item.channel_info

def get_save(data):
    data = json.dumps(data)
    data = json.loads(str(data))
    with open('Youtube_analitics.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)




get_save(data)