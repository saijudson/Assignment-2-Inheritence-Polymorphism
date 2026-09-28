class Media:
    def __init__(self,title):
        self.title = title
    def play(self):
        print(f"Playing media: {self.title}")
class Audio(Media):
    def __init__(self,title,duration):
        super().__init__(title)
        self.duration = duration
    def play(self):
        print(f"Playing audio: {self.title} - {self.duration}")
class Podcast(Audio):
    def __init__(self,title,duration,host):
        super().__init__(title,duration)
        self.host = host
    def play(self):
        print(f"Playing podcast: {self.title} hosted by {self.host}")
Media1 = Media("Python Basics")
Audio1 = Audio("Relaxing Music","4 minutes")
Podcast1 = Podcast("AI Today","30 minutes","John")
List = [Media1,Audio1,Podcast1]
for list in List:
    list.play()
