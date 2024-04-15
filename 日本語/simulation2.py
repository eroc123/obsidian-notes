import math
class vector:
    def __init__(self, x,y,z, magnitude):
        self.x = x
        self.y = y
        self.z = z
        self.magnitude = magnitude

vectorsToDefine = ["AB", "AC", "AD", "BC", "BD", "CD"]
vectors = {
}
def generateShape():
    for i in vectorsToDefine:
        if i == "AB" or "CD" == i:
            vectors[i] = vector(None, None, None, 4)
        elif i =="AC" or "BD" == i:
            vectors[i] == vector(None, None, None, 5)
        elif i =="AD" or "BC" == i:
            vectors[i] == vector(None, None, None, 6)