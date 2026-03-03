import sys
import json
from youtube_transcript_api import YouTubeTranscriptApi
import re
import urllib.request

def get_video_id(url):
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else url

def get_video_title(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        with urllib.request.urlopen(url) as response:
            html = response.read().decode()
            title_match = re.search(r'<title>(.*?)</title>', html)
            if title_match:
                title = title_match.group(1).replace(" - YouTube", "")
                return title
    except:
        pass
    return "YouTube Video"

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL or Video ID provided"}))
        sys.exit(1)

    input_val = sys.argv[1]
    video_id = get_video_id(input_val)
    url = f"https://www.youtube.com/watch?v={video_id}"
    title = get_video_title(video_id)

    try:
        transcript_list = YouTubeTranscriptApi().list(video_id)
        transcript = transcript_list.find_transcript(['en', 'en-US'])
        data = transcript.fetch()
        
        # Return segments for timestamp processing
        segments = []
        for entry in data:
            segments.append({
                "text": entry.text,
                "start": entry.start,
                "duration": entry.duration
            })
            
        print(json.dumps({
            "video_id": video_id,
            "title": title,
            "url": url,
            "segments": segments
        }))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
