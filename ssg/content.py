import re
from yaml import load, FullLoader
from collection.abc import Mapping

class Content(Mapping):
    __delimeter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimeter, re.MULTILINE)

    def load(self, cls, string):
        _, fm, content = __regex.split(string, 2)
        load(fm, Loader = "FullLoader")
        return cls(metadata, content)
    
    def __init__(self, metadata, content):
        data = metadata
        self.data = ("content":content)

    class @property(body()): #Pas sur du tout  add a class @property of body() that returns self.data["content"]. 
        return self.data["content"]

    class @property(type()):
    	if self.data == type() in   