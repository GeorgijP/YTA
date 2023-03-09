# Импортируем нужные библиотеки
import datetime
import json
import isodate
from decouple import config
from googleapiclient.discovery import build
from abc import ABC, abstractmethod


class MixinService(ABC):

    def __init__(self):
        self.api_key = config("YT_API_KEY")

    def service(self):
        self.service = build('youtube', 'v3', developerKey=self.api_key)
        return self.service

    @abstractmethod
    def __repr__(self):
        pass

class Youtube_anal(MixinService):
    """Анализирует канал ютуб"""

    def __init__(self, id_channel):
        super().__init__()
        self.__id_channel = id_channel
        self.channel_info = self.service().channels().list(id=id_channel, part='snippet, statistics').execute()
        self.link = f"https://www.youtube.com/channel/{self.__id_channel}"
        self.title = self.channel_info['items'][0]['snippet']['title']
        self.description = self.channel_info['items'][0]['snippet']['description']
        self.subscribers = self.channel_info['items'][0]['statistics']['subscriberCount']
        self.video_count = self.channel_info['items'][0]['statistics']['videoCount']
        self.view_count = self.channel_info['items'][0]['statistics']['viewCount']

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        self.info = json.dumps(self.channel_info, indent=4)
        return self.info

    def info_save(self, name_file):
        """Сохраняет информацию о канале в файл"""
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

    def __repr__(self):
        return f"Youtube_anal({self.__id_channel}, {self.api_key})"


class Video(MixinService):
    """Класс для обработки статистики видео"""
    def __init__(self, id_video):
        super().__init__()
        self.id_video = id_video
        self.video_data = self.service().videos().list(id=self.id_video, part='snippet, statistics').execute()
        self.video_info = json.dumps(self.video_data, indent=4)
        self.video_name = self.video_data['items'][0]['snippet']['title']
        self.video_view_count = self.video_data['items'][0]['statistics']['viewCount']
        self.video_like_count = self.video_data['items'][0]['statistics']['likeCount']

    def __str__(self):
        return f"Название видео: {self.video_name}"

    def __repr__(self):
        return f"Video({self.id_video})"


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

    def __repr__(self):
        return f"PLVideo({self.id_video}, {self.id_playlist})"


class PlayList(MixinService):
    """Обработка данных плейлиста"""
    def __init__(self, id_playlist):
        super().__init__()
        self.id_playlist = id_playlist
        self.playlist_data = self.service().playlists().list(id=self.id_playlist, part='snippet, contentDetails', maxResults=50).execute()
        self.playlist_info = json.dumps(self.playlist_data, indent=4)
        self.playlist_name = self.playlist_data['items'][0]['snippet']['title']
        self.url = f"https://www.youtube.com/playlist?list={self.id_playlist}"
        self.playlist_video = self.service.playlistItems().list(playlistId=self.id_playlist, part='contentDetails').execute()
        self.playlist_video_info = json.dumps(self.playlist_video, indent=4)
        self.video_ids: list[str] = [video['contentDetails']['videoId'] for video in self.playlist_video['items']]
        self.video_response = self.service.videos().list(part='contentDetails,statistics', id=','.join(self.video_ids)).execute()

    @property
    def total_duration(self):
        duration = datetime.timedelta(0)

        for video in self.video_response['items']:
            # Длительности YouTube-видео представлены в ISO 8601 формате
            iso_8601_duration = video['contentDetails']['duration']
            duration += isodate.parse_duration(iso_8601_duration)

        return duration

    def show_best_video(self):

        videos = {}
        for i in range(len(self.video_ids)):
            videos[int(self.video_response['items'][i]['statistics']['likeCount'])] = self.video_ids[i]

        return f"https://www.youtube.com/watch?v={videos[max(videos)]}"

    def __repr__(self):
        return f"PlayList({self.id_playlist})"


pl = PlayList("PLguYHBi01DWr4bRWc4uaguASmo7lW4GCb")
print(pl.show_best_video())
print(type(pl.total_duration))
