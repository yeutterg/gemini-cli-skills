import sys
import json
from youtube_transcript_api import YouTubeTranscriptApi
import re
import urllib.request

def get_video_id(url):
    pattern = r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else url

def get_video_info(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        with urllib.request.urlopen(url) as response:
            html = response.read().decode()
            title_match = re.search(r'<title>(.*?)</title>', html)
            title = "YouTube Video"
            if title_match:
                title = title_match.group(1).replace(" - YouTube", "")
            
            # Simple regex to find description in initial player response
            # Note: This is a bit fragile but often works for extracting description text
            desc_match = re.search(r'"shortDescription":"(.*?)"', html)
            description = ""
            if desc_match:
                description = desc_match.group(1).replace('\\n', '\n').replace('\\"', '"')
                
            return title, description
    except:
        pass
    return "YouTube Video", ""

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No URL or Video ID provided"}))
        sys.exit(1)

    input_val = sys.argv[1]
    video_id = get_video_id(input_val)
    url = f"https://www.youtube.com/watch?v={video_id}"
    title, description = get_video_info(video_id)

    try:
        transcript_list = YouTubeTranscriptApi().list(video_id)
        
        # Try to find an English transcript (manual or auto-generated)
        try:
            transcript = transcript_list.find_transcript(['en', 'en-US'])
        except:
            # Fallback: get the first available transcript
            transcript = next(iter(transcript_list))
            
        data = transcript.fetch()
        
        # Return segments and full text
        segments = []
        formatted_transcript = []
        last_timestamp_check = -120 # Force first segment to have timestamp
        
        for entry in data:
            segments.append({
                "text": entry.text,
                "start": entry.start,
                "duration": entry.duration
            })
            
            # Format timestamp: HH:MM:SS or MM:SS
            h = int(entry.start // 3600)
            m = int((entry.start % 3600) // 60)
            s = int(entry.start % 60)
            ts = f"{h:02}:{m:02}:{s:02}" if h > 0 else f"{m:02}:{s:02}"
            
            text = entry.text.strip()
            
            # Add timestamp if it's a speaker change (>>) or if 2 minutes have passed
            if text.startswith('>>') or (entry.start - last_timestamp_check >= 120):
                formatted_transcript.append(f"\n[{ts}] {text}")
                last_timestamp_check = entry.start
            else:
                formatted_transcript.append(text)
            
        print(json.dumps({
            "video_id": video_id,
            "title": title,
            "description": description,
            "url": url,
            "segments": segments,
            "full_text": " ".join(formatted_transcript).strip()
        }))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)

if __name__ == "__main__":
    main()
