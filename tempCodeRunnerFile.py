import math 
class vector3D:
    def __init__(self, x, y, z):
       createdvector=0
       self.x = x       
       self.y = y
       self.z = z
       vector3D.createdvector+=1
    @classmethod
    def get_created_vector(cls):
         return cls.createdvector
    def distance(V1,v2):
        return math.sqrt((V1.x - v2.x)**2 + (V1.y - v2.y)**2 + (V1.z - v2.z)**2)
        
v=vector3D(1,2,3)
v2=vector3D(4,5,6)
distance = vector3D.distance(v,v2)
print(f"Distance between v1 and v2 is: {distance}")
