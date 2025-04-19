class Rig ():
    def __init__(self, name, description, location, owner):
        self.name = input
        self.description = description
        self.location = location
        self.owner = owner

    def __str__(self):
        return f"Rig(name={self.name}, description={self.description}, location={self.location}, owner={self.owner})"
 