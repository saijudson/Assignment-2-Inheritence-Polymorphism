class FileProcessor:
    def __init__(self,filename):
        self.filename = filename
    def process(self):
        print(f"FileProcessor → Processing file: {self.filename}")
class TextFile(FileProcessor):
    def process(self):
        print(f"TextFile → Processing text file: {self.filename}")
class ImageFile(FileProcessor):
    def process(self):
        print(f"ImageFile → Processing image file: {self.filename}")
class AudioFile(FileProcessor):
    def process(self):
        print(f"AudioFile → Processing audio file: {self.filename}")
Text = TextFile("notes.txt")
Image = ImageFile("photo.jpg")
Audio = AudioFile("song.mp3")
files=[Text,Image,Audio]
for file in files:
    file.process()