def lerp(a, b, t):
    return (t * (b - a)) + a

class vec2:
    def __init__(self, x=0, y=0):
        self.x=x
        self.y=y

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def lerp(self, b, t):
        return vec2(lerp(self.x, b.x, t), lerp(self.y, b.y, t))
    
    def print(self):
        print("x: ", self.x, " y: ", self.y)