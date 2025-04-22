class Models:
    def __init__(self, name, vertexes, edges, faces):
        self.name = name
        self.vertexes = vertexes
        self.edges = edges
        self.faces = faces
        pass
    def __str__(self):
        return f"Name: {self.name}, vertexes: {self.vertexes}, edges: {self.edges}, faces: {self.faces}"
    pass

Cube = Models("Cube", 8, 12, 6)
Sphere = Models("Sphere", 140, 40, 50)
Cylinder = Models("Cylinder", 20, 30, 10)
Cone = Models("Cone", 10, 20, 5)
print(Cube)
print(Sphere)

print(Cylinder)
print(Cone) 