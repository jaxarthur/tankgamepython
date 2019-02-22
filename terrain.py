import math, random, pygame

class terrain():
    def __init__(self, sw, sh):
        self.terrainarray = []
        self.minh, self.maxh = 50, 100
        self.maxvar = 2
        self.sw = sw
        self.sh = sh
        for x in range(sw):
            #first node check
            if(x > 1):
                previous = self.terrainarray[x-1]
                rand = 0
                
                while rand > previous + self.maxvar or rand < previous - self.maxvar:
                    rand = random.randint(self.minh, self.maxh)
                
                self.terrainarray.append((x, rand))
            
            else:
                self.terrainarray.append((0, (100-50)/2))
    
    def draw(self, screen):
        temp = self.terrainarray
        temp.insert(0, (0, self.sh))
        temp.insert(-1, (self.sw, self.sh))
        pygame.draw.polygon(screen, (0,0,255), temp)

    def find(x):
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

    
        


            