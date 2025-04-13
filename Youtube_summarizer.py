from transformers import pipeline
import sys
import time
from fetch_video_transcript import get_transcript

summarizer = pipeline('summarization') 


def split_text(text, chunk_size=1000):
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    return chunks

def summarize_long_text(text):
    chunks = split_text(text)
    summarized_chunks = [summarizer(chunk, max_length=150, min_length=50, do_sample=False)[0]['summary_text'] for chunk in chunks]
    return " ".join(summarized_chunks)


transcript = get_transcript('https://www.youtube.com/watch?v=AUozVp78dhk')
summary = summarize_long_text(transcript) 
print("Summary:\n", summary)
print("\n")

