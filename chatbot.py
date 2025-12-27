from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi , TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate

load_dotenv()

# Document Ingestion 

video_id = "etnLX7m2MiA"
api = YouTubeTranscriptApi()
try:
    transcript_list = api.fetch(video_id = video_id, languages = ["hi"])
    transcript = " ".join(chunk.text for chunk in transcript_list)
    print(transcript)

except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")
