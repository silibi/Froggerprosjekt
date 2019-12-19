#Imports
import random
import pygame
import time


#Initialiseringen
pygame.init()


#Spillinformasjon
runde = 1
livmistet = 0
tid = 0

vinnrute1 = False
vinnrute2 = False
vinnrute3 = False
vinnrute4 = False
vinnrute5 = False

run = True
startskjerm = True

#Bokstaver startskjerm
Fbokstav = pygame.transform.scale(pygame.image.load("./Sprites/Lettersandnumbers/F.png"), (32, 37))
Rbokstav = pygame.transform.scale(pygame.image.load("./Sprites/Lettersandnumbers/R.png"), (32, 37))
Obokstav = pygame.transform.scale(pygame.image.load("./Sprites/Lettersandnumbers/O.png"), (32, 37))
Gbokstav = pygame.transform.scale(pygame.image.load("./Sprites/Lettersandnumbers/G.png"), (32, 37))
Ebokstav = pygame.transform.scale(pygame.image.load("./Sprites/Lettersandnumbers/E.png"), (32, 37))


#spillvinduet
vindux = 448
vinduy = 512
delbit = 32
spillvindu = pygame.display.set_mode((vindux, vinduy))
pygame.display.set_caption("Frogger")
bg = pygame.image.load("./Sprites/sprites1.png")
bg_tilpasset = pygame.transform.scale(bg, (vindux, vinduy))



#Frogger spilleren
frogger = pygame.image.load("./Sprites/Frog/Froggerstanding.png")
froggerx = 224
froggery = 448
dx = dy = 10
frogger_tilpasset = pygame.transform.scale(frogger, (delbit, delbit))
froggerhome = pygame.transform.scale(pygame.image.load("./Sprites/Frog/HomeFrogger1.png"), (delbit, delbit))


#Tall, score osv.
class tall:
    
    def __init__(self):
        pass
'''
Hadde tenkt til å Lage poengsystem her som illustreres på skjermen, 
men fikk ikke tid
'''





#Bilene
class cars:
    def __init__(self, image, speed, direction, size, startx, starty, acceleration):
        self.image = image
        self.speed = speed
        self.direction = direction
        self.size = size
        self.startx = startx
        self.starty = starty
        self.acceleration = acceleration
        
    def loadcar(self):
        car = pygame.transform.scale(pygame.image.load(self.image), (self.size * delbit, delbit))
        spillvindu.blit(car, (self.startx, self.starty))
        
        
    def drivecar(self):
        
        global froggerx
        global froggery
        
        for i in range(int(round((runde * self.acceleration + self.speed)/2, 0))):
            if (self.startx >= froggerx) and (self.startx <= froggerx + delbit) and (froggery == self.starty): 
                drap()  
            
            if self.direction == "left":
                if self.startx < -64:
                    self.startx = 480
                else:
                    self.startx -= 1
                
            elif self.direction == "right":
                if self.startx > 480:
                    self.startx = -64
                else:
                    self.startx += 1

          
'''
Dersom du ikke liker når folk hardcoder masse greier istedenfor
å finne en mer gjenbrukbar måte å gjøre det på,
bare bla ned sånn 100 linjer.
Ikke tenk for mye på det rett og slett
'''  
              
car11 = cars("./Sprites/Carsprites/Car1.png", 1, "left", 1, 416, 416, 1.4)
car12 = cars("./Sprites/Carsprites/Car1.png", 1, "left", 1, 536, 416, 1.4)
car13 = cars("./Sprites/Carsprites/Car1.png", 1, "left", 1, 656, 416, 1.4)
car14 = cars("./Sprites/Carsprites/Car1.png", 1, "left", 1, 776, 4161, 1.4)

car21 = cars("./Sprites/Carsprites/Car2.png", 0.5, "right", 1, 0, 384, 1)
car22 = cars("./Sprites/Carsprites/Car2.png", 0.5, "right", 1, -120, 384, 1) 
car23 = cars("./Sprites/Carsprites/Car2.png", 0.5, "right", 1, -240, 384, 1) 
car24 = cars("./Sprites/Carsprites/Car2.png", 0.5, "right", 1, -360, 384, 1) 

car31 = cars("./Sprites/Carsprites/Car4.png", 0.8, "left", 1, 416, 352, 1.0)
car32 = cars("./Sprites/Carsprites/Car4.png", 0.8, "left", 1, 536, 352, 1.0)
car33 = cars("./Sprites/Carsprites/Car4.png", 0.8, "left", 1, 656, 352, 1.0)
car34 = cars("./Sprites/Carsprites/Car4.png", 0.8, "left", 1, 776, 352, 1.0)

car41 = cars("./Sprites/Carsprites/Car5.png", 1.4, "right", 1, 0, 320, 2.0)
car42 = cars("./Sprites/Carsprites/Car5.png", 1.4, "right", 1, -120, 320, 2.0) 
car43 = cars("./Sprites/Carsprites/Car5.png", 1.4, "right", 1, -240, 320, 2.0) 
car44 = cars("./Sprites/Carsprites/Car5.png", 1.4, "right", 1, -360, 320, 2.0)

car51 = cars("./Sprites/Carsprites/Car3.png", 1, "left", 2, 416, 288, 0.3)
car52 = cars("./Sprites/Carsprites/Car3.png", 1, "left", 2, 536, 288, 0.3)
car53 = cars("./Sprites/Carsprites/Car3.png", 1, "left", 2, 656, 288, 0.3)
car54 = cars("./Sprites/Carsprites/Car3.png", 1, "left", 2, 776, 288, 0.3)

bilene = [
      car11,
      car12,
      car13,
      car14,
      car21, 
      car22, 
      car23, 
      car24, 
      car31,
      car32, 
      car33, 
      car34, 
      car41, 
      car42, 
      car43, 
      car44,
      car51,
      car52, 
      car53,
      car54
      ]

for i in bilene:
    if random.getrandbits(1) == False or random.getrandbits(1) == False:
        bilene.remove(i)

#Funksjoner for å laste inn og kjøre bilene
def cardriver():
    for i in bilene:
        i.drivecar()
    
def carloader():
    for i in bilene:
        i.loadcar()

#I vannet
"""
Er egentlig meningen at det skal være stokker og skilpadder i vannet også, men jeg fikk litt lite
tid, så det blir en improvisasjon hvor vi har ottere og krokkodiller i vannet. Og egentlig kan ikke
frosken gå på vannet, men nå kan han det. Her har jeg også gjenbrukt bilklassen.
"""

fish11 = cars("./Sprites/Enemies/Otter1.png", 0.8, "right", 1, 0, 224, 1.3)
fish12 = cars("./Sprites/Enemies/Otter1.png", 0.8, "right", 1, -120, 224, 1.3)
fish13 = cars("./Sprites/Enemies/Otter1.png", 0.8, "right", 1, -240, 224, 1.3)
fish14 = cars("./Sprites/Enemies/Otter1.png", 0.8, "right", 1, -360, 224, 1.3)
fish15 = cars("./Sprites/Enemies/Otter1.png", 0.8, "right", 1, -480, 224, 1.3)

fish21 = cars("./Sprites/Enemies/CrocHead1.png", 0.7, "right", 1, 0, 192, 1)
fish22 = cars("./Sprites/Enemies/CrocHead1.png", 0.7, "right", 1, -120, 192, 1)
fish23 = cars("./Sprites/Enemies/CrocHead1.png", 0.7, "right", 1, -240, 192, 1)
fish24 = cars("./Sprites/Enemies/CrocHead1.png", 0.7, "right", 1, -360, 192, 1)
fish25 = cars("./Sprites/Enemies/CrocHead1.png", 0.7, "right", 1, -480, 192, 1)

fish31 = cars("./Sprites/Enemies/snake3.png", 1.4, "left", 2, 416, 160, 1.1)
fish32 = cars("./Sprites/Enemies/snake3.png", 1.4, "left", 2, 536, 160, 1.1)
fish33 = cars("./Sprites/Enemies/snake3.png", 1.4, "left", 2, 656, 160, 1.1)
fish34 = cars("./Sprites/Enemies/snake3.png", 1.4, "left", 2, 776, 160, 1.1)
fish35 = cars("./Sprites/Enemies/snake3.png", 1.4, "left", 2, 896, 160, 1.1)

fish41 = cars("./Sprites/Enemies/Otter1.png", 1, "right", 1, 0, 128, 1.1)
fish42 = cars("./Sprites/Enemies/Otter1.png", 1, "right", 1, -120, 128, 1.1)
fish43 = cars("./Sprites/Enemies/Otter1.png", 1, "right", 1, -240, 128, 1.1)
fish44 = cars("./Sprites/Enemies/Otter1.png", 1, "right", 1, -360, 128, 1.1)
fish45 = cars("./Sprites/Enemies/Otter1.png", 1, "right", 1, -480, 128, 1.1)

fish51 = cars("./Sprites/Enemies/CrocHead1.png", 0.4, "right", 1, 0, 96, 0.7)
fish52 = cars("./Sprites/Enemies/CrocHead1.png", 0.4, "right", 1, -120, 96, 0.7)
fish53 = cars("./Sprites/Enemies/CrocHead1.png", 0.4, "right", 1, -240, 96, 0.7)
fish54 = cars("./Sprites/Enemies/CrocHead1.png", 0.4, "right", 1, -360, 96, 0.7)
fish55 = cars("./Sprites/Enemies/CrocHead1.png", 0.4, "right", 1, -480, 96, 0.7)


fiskene = [
        fish11,
        fish12,
        fish13,
        fish14,
        fish15,
        fish21,
        fish22,
        fish23,
        fish24, 
        fish25,
        fish31,
        fish32,
        fish33,
        fish34,
        fish35,
        fish41,
        fish42,
        fish43,
        fish44,
        fish45,
        fish51,
        fish52,
        fish53,
        fish54,
        fish55
        ]

for i in fiskene:
    if random.random() >= 0.2:
        fiskene.remove(i)

def fishmover():
    for i in fiskene:
        i.drivecar()
    
    
def fishloader():
    for i in fiskene:
        i.loadcar()


#Rundesymbolet
"""
Det er et symbol nede i høyre hjørne som viser hvilken runde du er på
ettersom hvor mange av den som er på skjermen
"""
def numberrounds():
    global runde
    
    for i in range(runde):
        bilde = pygame.transform.scale(pygame.image.load("./Sprites/Lettersandnumbers/round.png"),(12, 12))
        spillvindu.blit(bilde, (436 - 12*i, 480))
        




#Det som kommer opp når du dør
"""
En liten dødsanimasjon
"""
death1 = pygame.transform.scale(pygame.image.load("./Sprites/Death/RunOver1.png"), (delbit, delbit))
death2 = pygame.transform.scale(pygame.image.load("./Sprites/Death/RunOver2.png"), (delbit, delbit))
death3 = pygame.transform.scale(pygame.image.load("./Sprites/Death/RunOver3.png"), (delbit, delbit))
death4 = pygame.transform.scale(pygame.image.load("./Sprites/Death/Death.png"), (delbit, delbit))
deaths = [death1, death2, death3, death4]

def drap():
    global tid
    global livmistet
    global froggerx
    global froggery
    global run
    
    livmistet += 1
    tid = 0
    
    if livmistet >= 3:
        run = False
    
    for i in deaths:
        spillvindu.blit(bg_tilpasset, (0, 0))
        spillvindu.blit(i, (froggerx, froggery))
        pygame.draw.rect(spillvindu, (0, 0, 0), (0, 480, livmistet * 16, 32))
        pygame.display.update()
        time.sleep(0.5)
        
    froggerx = 224
    froggery = 448


#Funksjon som styrer timeren     
def tidspress():
    global tid
    tid += 0.16
    if tid < 256:
        pygame.draw.rect(spillvindu, (0, 0, 0), (128, 480, int(round(tid, 0)), 32))
    else:
        drap()


#Seiersfunksjoner for når frosken kommer seg over       
def Vinn():
    global tid
    global froggerx
    global froggery
    
    tid = 0
    froggerx = 224
    froggery = 448  

#Funksjon som kjøres når ale froskene er i mål
def nyrunde():
    global tid
    global froggerx
    global froggery
    global runde
    global vinnrute1
    global vinnrute2
    global vinnrute3
    global vinnrute4
    global vinnrute5
    
    tid = 0
    froggerx = 224
    froggery = 448
    runde += 1
    vinnrute1 = False
    vinnrute2 = False
    vinnrute3 = False
    vinnrute4 = False
    vinnrute5 = False 
      
    
    

#Kjøring av programmet
spillvindu.blit(bg_tilpasset, (0, 0))
spillvindu.blit(frogger_tilpasset, (froggerx, froggery))
carloader()
pygame.display.update()

clk = pygame.time.Clock()

while run:
    clk.tick_busy_loop(60)
    if startskjerm == True:
        
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN: 
                if e.key == pygame.K_SPACE:
                    startskjerm = False
                    time.sleep(1)
            if e.type == pygame.QUIT:
                run = False
           
        spillvindu.blit(bg_tilpasset, (0, 0))
        
        spillvindu.blit(Fbokstav ,(128, 224))
        spillvindu.blit(Rbokstav ,(160, 224))
        spillvindu.blit(Obokstav ,(192, 224))
        spillvindu.blit(Gbokstav ,(224, 224))
        spillvindu.blit(Gbokstav ,(256, 224))
        spillvindu.blit(Ebokstav ,(288, 224))
        spillvindu.blit(Rbokstav ,(320, 224))
        
        pygame.display.update()
        time.sleep(0.01)
    else:
        #Død ved utsniking fra skjermen
        if froggerx < 0 or froggerx > 416:
            drap()

   
        if froggery < 64 or froggery > 448:
            drap()
        
        #Død ved enden
    
        if froggery == 64 and froggerx < 96 and froggerx >= 64:
            drap()
        
        if froggery == 64 and froggerx < 192 and froggerx >= 160:
            drap()
        
        if froggery == 64 and froggerx < 288 and froggerx >= 256:
            drap()
        
        if froggery == 64 and froggerx < 384 and froggerx >= 352:
            drap()

        #Vinn ved enden
    
        if froggery == 64 and froggerx >= 0 and froggerx < 64:
            if vinnrute1 == True:
                drap()
            else:
                vinnrute1 = True
                Vinn()
        
        if froggery == 64 and froggerx >= 96 and froggerx < 160:
            if vinnrute2 == True:
                drap()
            else:
                vinnrute2 = True
                Vinn()
        
        if froggery == 64 and froggerx >= 192 and froggerx < 256:
            if vinnrute3 == True:
                drap()
            else:
                vinnrute3 = True
                Vinn()
        
        if froggery == 64 and froggerx >= 288 and froggerx < 352:
            if vinnrute4 == True:
                drap()
            else:
                vinnrute4 = True
                Vinn()
        
        if froggery == 64 and froggerx >= 384 and froggerx < 448:
            if vinnrute5 == True:
                drap()
            else:
                vinnrute5 = True
                Vinn()
    
        #Bilene kjører   
        cardriver()
        
        #Fiskene beveger seg:
        fishmover()
    
    
        for e in pygame.event.get():
            if e.type == pygame.KEYDOWN:               
                if e.key == pygame.K_UP:
                    froggery -= delbit
                if e.key == pygame.K_DOWN:
                    froggery += delbit
                if e.key == pygame.K_RIGHT:
                    froggerx += delbit
                if e.key == pygame.K_LEFT:
                    froggerx -= delbit
            if e.type == pygame.QUIT:
                run = False
    
        #Starter ny runde dersom alle froskene har kommet hjem
        if vinnrute1 == True and vinnrute2 == True and vinnrute3 == True and vinnrute4 == True and vinnrute5 == True:
            nyrunde()
        
        #Tegner Spillet på nytt hver eneste gang programmet kjører igjennom løkken
        spillvindu.blit(bg_tilpasset, (0, 0))
        spillvindu.blit(frogger_tilpasset, (froggerx, froggery))
        
        if vinnrute1 == True:
            spillvindu.blit(froggerhome, (16, 64))
        if vinnrute2 == True:
            spillvindu.blit(froggerhome, (112, 64))
        if vinnrute3 == True:
            spillvindu.blit(froggerhome, (208, 64))
        if vinnrute4 == True:
            spillvindu.blit(froggerhome, (304, 64))
        if vinnrute5 == True:
            spillvindu.blit(froggerhome, (400, 64))
        
        fishloader()
        carloader()
        numberrounds()
        pygame.draw.rect(spillvindu, (0, 0, 0), (0, 480, livmistet * 16, 32))
        tidspress()
        pygame.display.update()

#Avslutte
pygame.quit()
