# Импортируем нужные библиотеки
import json
from decouple import config
from googleapiclient.discovery import build

class Youtube_anal:
    """
    Анализирует канал ютуба
    """
    def __init__(self, id_channel, api_key):
        self.api_key = config(api_key)
        self.id_channel = id_channel
        self.service = build('youtube', 'v3', developerKey=self.api_key)

    def print_info(self):
        """
        Выводит в консоль информацию о канале.
        """
        self.info = json.dumps(self.service.channels().list(id=self.id_channel, part='snippet,statistics').execute())
        return self.info
