class Edge:
    def __init__(self, source, destination):
        self.__source = source
        self.__destination = destination
    def get_source(self):
        return self.__source
    def get_destination(self):
        return self.__destination
    def __str__(self):
        return f"Edge({self.__source} -> {self.__destination})"