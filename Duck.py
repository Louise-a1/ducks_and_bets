import random

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
        self.location = "home"
        self.money = 100
        self.bet_timeout = 200


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
        

    def set_map(self):
        # from home to house
        if self.home_to_house():
            self.location = "house"
            self.x = 240    
            self.y = 400
            self.set_direction("up")
            
        if self.house_to_home():
            self.location = "home"
            self.x = 1187
            self.y = 650
            self.set_direction("down")


    def home_to_house(self):
        if self.location == "home" and 1065 <= self.x <= 1190 and 368 <= self.y <= 534: return True
        
    def house_to_home(self):
        if self.location == "house" and 250 >= self.x <= 300 and 500 >= self.y >= 450: return True 


    def duck_bet(self):
        if self.money >= 10:
            self.bet_timeout -= 40
            if self.bet_timeout <= 0:
                self.bet_timeout = 200
                self.money -= 10
                rand = random.randint(1,10)
                if rand == 1: 
                    self.money += 100

                else: 
                    print("You lost!")
                
                print(f'Your new account is {self.money}')


    def __repr__(self):
        return "id: " + str(self.id)