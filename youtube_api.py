from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from config import config
from utils import setup_logger

logger = setup_logger('youtube_api', 'youtube_api.log')

DEVELOPER_KEY = config.get('')
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(query, max_results=10):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    ).execute()

    videos = []
    for search_result in search_response.get('items', []):
        if search_result['id']['kind'] == 'youtube#video':
            videos.append(search_result['id']['videoId'])
    
    return videos

def add_comment(video_id, comment_text):
    # Placeholder for adding a comment
    print(f"Adding comment '{comment_text}' to video {video_id}")
    pass

if __name__ == '__main__':
    # Example usage
    query = 'Visa Preparation'
    video_ids = youtube_search(query)
    print(f"Found videos: {video_ids}")
    
    if video_ids:
        add_comment(video_ids[0], 'This is an automated comment.')