# Импортируем нужные библиотеки
import json

from decouple import config
from googleapiclient.discovery import build


class Youtube_anal:
    """
    Анализирует канал ютуб
    """
    def __init__(self, id_channel, api_key):
        self.api_key = config(api_key)
        self.__id_channel = id_channel
        self.channel_info = self.service().channels().list(id=id_channel, part='snippet, statistics').execute()
        self.link = f"https://www.youtube.com/channel/{self.__id_channel}"
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.subscribers = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def service(self):
        self.service = build('youtube', 'v3', developerKey=self.api_key)
        return self.service

    def print_info(self):
        """
        Выводит в консоль информацию о канале.
        """
        self.info = json.dumps(self.channel_info, indent=4)
        return self.info

    def info_save(self, name_file):
        """
        Сохраняет информацию о канале в файл
        """
        with open(name_file, 'w', encoding='UTF-8') as file:
            json.dump(self.channel_info, file, indent=4)

    def __str__(self):
        return f"Youtube-канал: {self.title}"

    def __add__(self, other):
        return int(self.subscribers) + int(other.subscribers)

    def __lt__(self, other):
        if isinstance(other, Youtube_anal):
            return self.subscribers < other.subscribers
        else:
            return False
