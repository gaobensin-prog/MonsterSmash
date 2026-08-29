#get the library that get the Path so that main.py or any other
#.py files can also get the picture
from pathlib import Path

class Picture():
    def __init__(self, name):
        self.name = name
    def get_picture(self):
        #get the directory of the file that calls this class
        current_dir = Path(__file__).resolve().parent
        #path to image
        return current_dir / "pictures" / self.name
