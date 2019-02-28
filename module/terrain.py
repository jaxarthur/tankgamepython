import math, random, pygame

window = pygame.display.get_surface()
info = pygame.display.Info()
screenW, screenH = info.current_h, info.current_w

class terrain():
    def __init__(self, ):
        self.terrainarray = []
        self.minh, self.maxh = 50, 100
        self.maxvar = 2
        for x in range(screenW):
            #first node check
            if(x > 1):
                previous = self.terrainarray[x-1]
                rand = 0
                
                while rand > previous + self.maxvar or rand < previous - self.maxvar:
                    rand = random.randint(self.minh, self.maxh)
                
                self.terrainarray.append((x, rand))
            
            else:
                self.terrainarray.append((0, (100-50)/2))
    
    def draw(self):
        temp = self.terrainarray
        temp.insert(0, (0, temp[0][1]))
        temp.insert(-1, (screenW, temp[-1][1]))
        pygame.draw.polygon(window, (0,0,255), temp)

    def find(self, x):
        return self.terrainarray[x]
        
    def colisiondetect(self, cords):
        if self.terrainarray[cords[0]] > cords[1]:
            return True
        else:
            return False

    def deform(self, cords, radius):
        for i in range(radius*2):
            x = i - radius
            bottom = math.sqrt(math.pow(radius, 2) - math.pow(x, 2))
            if self.terrainarray[cords[0] + x] > bottom:
                self.terrainarray[cords[0] + x] = bottom
    
    def slope(self, cords):
        temp = 0
        for i in range(11):
            x = i - 5
            temp = temp + ((self.terrainarray[x+cords[0]] - cords[1]) * x)
        
        return temp

    
land = terrain()       


            
