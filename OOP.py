
import maya.cmds as cmds

class Models:
    createdmodels=0
    def __init__(self, name, subdivisionsX, subdivisionsy, subdivisionsz):
        self.name = name
        self.X = subdivisionsX
        self.Y = subdivisionsy
        self.Z = subdivisionsz
    def __str__(self):
        return f"Name: {self.name}, vertexes: {self.vertexes}, edges: {self.edges}, faces: {self.faces}"
    
    def create(self):
        if self.name == "Cube":
            cmds.polyCube(subdivisionsX=self.X, subdivisionsY=self.Y, subdivisionsZ=self.Z)
            self.createdmodels+=1
        elif self.name == "Sphere":
            cmds.polySphere(r=self.Y, n=self.name)
            self.createdmodels+=1
        elif self.name == "Cylinder":
            cmds.polyCylinder(h=self.X, r=self.Y, n=self.name)
            self.createdmodels+=1
        else:
            cmds.warning("Model not found")
    pass
    

number_of_models = 3
name=input("Enter the name of the model: ")
while number_of_models > 0:
    name = input("Enter the name of the model: ")
    Model= Models(name, 8, 12, 6)
    Model.create()
    print("Model created")
    number_of_models -= 1

