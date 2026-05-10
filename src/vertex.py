class Vertex:
    def __init__(self, vertex_id):
        self.__id = vertex_id
    def get_id(self):
        return self.__id
    def __str__(self):
        return f"Vertex({self.__id})"