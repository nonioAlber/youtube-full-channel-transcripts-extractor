thonimport requests
from bs4 import BeautifulSoup

def extract_transcripts(channel_url, settings):
    """
    Extract transcripts from all videos in a YouTube channel.
    """
    # Request channel page
    response = requests.get(channel_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Dummy logic to simulate video extraction and transcript collection
    transcripts = []
    video_data = soup.find_all('script', {'type': 'application/json'})
    
    for video in video_data:
        transcript = {
            "channelHandle": "@Apify",
            "channelName": "Apify",
            "channelID": "UCTgwcoeGGKmZ3zzCXN2qo_A",
            "isShorts": False,
            "videoId": "MlChwZKMrQI",
            "title": "Can proxies be ethical? 🛡",
            "captions": [
                "we try to use ethical proxies which",
                "means proxies that are sourced ethically",
                "from people who actually know that their",
                "computers are being used as proxies I"
            ]
        }
        transcripts.append(transcript)
    
    return transcripts