class Wallet:
    def __init__(self, id: int):
        self.id = id
        self.money: float
        self.password: str


class Duck:
    def __init__(self, id, vel, x , y):
        self.id = id
        self.x = x
        self.y = y
        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.walkCount = 0
        self.standing = False
        self.vel = vel
        self.width = 32 
        self.height = 32

    def __repr__(self):
        return "id: " + str(self.id)