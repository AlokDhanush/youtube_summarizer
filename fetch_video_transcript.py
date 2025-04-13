from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    v_ind = video_url.index("v=") # Extract video ID
    video_id = video_url[v_ind+2:v_ind+13]
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages = ['en', 'es', 'fr', 'hi'])
    except Exception:
        return ""
        
    return " ".join([t['text'] for t in transcript])
