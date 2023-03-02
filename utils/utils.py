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


class Video:
    """Класс для обработки статистики видео"""
    def __init__(self, id_video):
        self.id_video = id_video
        self.api_key = config("YT_API_KEY")
        self.video_data = self.service().videos().list(id=self.id_video, part='snippet, statistics').execute()
        self.video_info = json.dumps(self.video_data, indent=4)
        self.video_name = self.video_data['items'][0]['snippet']['title']
        self.video_view_count = self.video_data['items'][0]['statistics']['viewCount']
        self.video_like_count = self.video_data['items'][0]['statistics']['likeCount']

    def service(self):
        self.service = build('youtube', 'v3', developerKey=self.api_key)
        return self.service

    def __str__(self):
        return f"Название видео: {self.video_name}"


class PLVideo(Video):
    """Класс для обработки статистики видео из плейлиста"""
    def __init__(self,id_video, id_playlist):
        super().__init__(id_video)
        self.id_playlist = id_playlist
        self.playlist_data = self.service.playlists().list(id=self.id_playlist, part='snippet, contentDetails').execute()
        self.playlist_info = json.dumps(self.playlist_data, indent=4)
        self.playlist_name = self.playlist_data['items'][0]['snippet']['title']

    def __str__(self):
        return f"Название видео: {self.video_name} Название плейлиста: {self.playlist_name}"
