import pyttsx3
import PyPDF2
import random
from textblob import TextBlob

class EnhancedAudiobookGenerator:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.speaker = pyttsx3.init()

    def extract_text_from_pdf(self, start_page=7):
        with open(self.pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ''
            for page_num in range(start_page, len(pdf_reader.pages)):
                text += pdf_reader.pages[page_num].extract_text()
            return text

    def analyze_text_sentiment(self, text):
        blob = TextBlob(text)
        return blob.sentiment.polarity

    def convert_text_to_speech(self, text):
        sentiment = self.analyze_text_sentiment(text)
        # Introduce variation based on sentiment
        rate = random.uniform(0.8, 1.2)
        volume = random.uniform(0.8, 1.2)
        self.speaker.setProperty('rate', rate * 100)  # Adjusting rate range
        self.speaker.setProperty('volume', volume)

        self.speaker.say(text)
        self.speaker.runAndWait()

if __name__ == "__main__":
    pdf_path = "your_sample.pdf"
    enhanced_audiobook_generator = EnhancedAudiobookGenerator(pdf_path)
    text_content = enhanced_audiobook_generator.extract_text_from_pdf()
    enhanced_audiobook_generator.convert_text_to_speech(text_content)
