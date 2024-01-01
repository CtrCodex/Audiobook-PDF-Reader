# Audiobook-PDF-Reader
Transform your PDFs into audiobooks effortlessly with this simple Python script. Using PyPDF2 and pyttsx3, this audiobook generator reads the text content from your PDF file and converts it into an MP3 file. A straightforward solution for those looking to quickly enjoy their written content in audio format.

## Features
- Extracts text content from a PDF file
- Enhances text accuracy through spell checking and random word variations
- Converts the enhanced text to speech and saves it as an MP3 file

## Prerequisites
- Python 3.x
- Install required libraries: `pip install PyPDF2 pyttsx3 textblob`

## Usage
1. Replace `"your_sample.pdf"` with the path to your PDF file.
2. Run the script: `python audiobook_generator.py`
3. Find the generated audiobook as `output.mp3`.

## Enhancements
Feel free to customize the code for your specific needs. Possible enhancements include:
- Adjusting the probability threshold for word variations
- Adding more advanced text processing features
- Incorporating multithreading for faster processing of large PDFs

## Credits
- [PyPDF2](https://pythonhosted.org/PyPDF2/)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [TextBlob](https://textblob.readthedocs.io/en/dev/)

## License
This project is licensed under the [MIT License](LICENSE).

---

*"In the world of code, let your creations resonate like a symphony, creating an experience that transcends mere functionality."*
