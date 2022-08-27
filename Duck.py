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


    def set_direction(self, direction):
        if direction == "left":
            self.x -= self.vel
            self.left = True
            self.right = False
            self.standing = False
            self.up = False
            self.down = False
        elif direction == "right":
            self.x += self.vel
            self.right = True
            self.left = False
            self.standing = False
            self.up = False
            self.down = False
        elif direction == "up":
            self.y -= self.vel
            self.up = True
            self.standing = False
            self.right = False
            self.left = False
            self.down = False
        elif direction == "down":
            self.y += self.vel
            self.down = True
            self.standing = False
            self.up = False
            self.right = False
            self.left = False
        elif direction == "standing":
            self.standing = True
            self.up = False
            self.right = False
            self.left = False
            self.donw = False


    def get_direction(self):
        if self.standing == True: return "standing"
        if self.left == True: return "left"
        if self.right == True: return "right"
        if self.up == True: return "up"
        if self.down == True: return "down"
        

    def __repr__(self):
        return "id: " + str(self.id)