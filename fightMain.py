from pygame.locals import *
import pygame
import pylab as pl

### Implementation of Classes and Functions : Location, Ring, Fighter, Fight

class Location():

    """ Location object in a 2d array.
        Assumes x and y numbers and turn them into floats. """

    def __init__(self, x, y):
        self.coord = pl.array([ float(x), float(y) ])   ### instantiation of 2d position array object

    def __str__(self):
        return '< Location: ' + str(round(self.coord[0],2)) + ' : ' + str(round(self.coord[1],2)) + ' >'  ### for printing the array object easily

    def move(self, dx, dy):

        """ Assumes dx and dy numbers and turn them to floats.
            Moves location dx in the x direction and dy in the y direction. """        

        self.coord[0] = self.coord[0] + dx
        self.coord[1] = self.coord[1] + dy
            
class Ring():

    """ Base Class for 2d Rings. Only supports 2 fighters.
        Assumes fighterRed and fighterBlue are fighters. Size of ring defaults to 10 x 10 """

    def __init__(self, name = None, x_size = 10 , y_size = 10, fighterRed = None, fighterBlue = None):
        self.name = name
        self.x_size = x_size
        self.y_size = y_size
        self.fightersInRing = []
        self.fightersLocations = []
        if fighterRed != None:                                   ### if fighters are given as arguments
            self.addFighter(fighterRed, x_size*0.5, y_size*0.25) ### they are automatically placed in the ring
        if fighterBlue != None:
            self.addFighter(fighterBlue, x_size*0.5, y_size*0.75)
            

    def __str__(self):   ### for printing ring's variables easily
        return ('<'+ self.name + ' : ' + str(self.x_size) + 'm x ' + str(self.y_size) + 'm \n' +
                '  Fighter Red  : ' + str(self.fightersLocations[0]) + ' : ' + str(self.fightersInRing[0].firstName) + '\n' +
                '  Fighter Blue : ' + str(self.fightersLocations[1]) + ' : ' + str(self.fightersInRing[1].firstName) + '\n' + 
                '< ---------------- >')
                                                

    def addFighter(self, fighter, pos_x = 0, pos_y = 0):

        """ Assumes fighter a fighter.
            Adds the fighter to the ring with default position [ 0, 0]"""

        if len(self.fightersInRing) == 2:   ### ensures no more than 2 fighters are added
            raise ValueError('This ring already has 2 fighters in it.')   
        else:
            self.fightersInRing.append(fighter)
            fighterLocation = Location(pos_x, pos_y)
            self.fightersLocations.append(fighterLocation)

    def moveFighter(self, fighter, dx, dy):

        """ Assumes fighter a fighter and dx, dy numbers.
            Moves fighter dx in the x direction and dy in the y direction within the ring's size """
        
        if fighter not in self.fightersInRing:
            raise ValueError('Fighter not in ring') ### can't move a fighter that's not in the ring
        else:
            index = self.fightersInRing.index(fighter)
            fighterLocation = self.fightersLocations[index]  

            ### moving x within boundaries

            if fighterLocation.coord[0] + dx > self.x_size:
                fighterLocation.coord[0] = self.x_size
            elif fighterLocation.coord[0] + dx < 0 :
                fighterLocation.coord[0] = 0
            else:
                fighterLocation.coord[0] += dx

            ### moving y within boundaries

            if fighterLocation.coord[1] + dy > self.y_size:
                fighterLocation.coord[1] = self.y_size
            elif fighterLocation.coord[1] + dy < 0 :
                fighterLocation.coord[1] = 0
            else:
                fighterLocation.coord[1] += dy
                
                        
    def removeFighter(self, fighter):
        
        """ Assumes fighter a fighter.
            Removes fighter from the ring. """
        
        if fighter not in ring:
            raise ValueError('{} is not in this ring'.format(fighter))   ### can't remove if not in ring
        elif fightersInRing[0] == fighter:        ### removes fighter and respective location from lists
            self.fightersInRing.remove(fighter)
            del self.fightersLocations[0]
        else:
            self.fightersInRing.remove(fighter)
            del self.fightersLocations[1]

class Fighter():

    """Base class for Fighters. Attributes are set to None if arguments are not given. """

    numIndexes = 0  ## keeping track of number of Id's created
                    ## and assures every fighter has a different Id

    ### setting up parameters

    styles = ['Striking','Wrestling','BJJ','Boxing','Muay Thai',
              'Boxing / BJJ']

    weightClasses = ['Lightweight','Welterweith','Bantamweight','Middleweight',
                     'Featherweight','Light Heavyweight','Heavyweight']
    maxLife = 10
    minLife = 0

    maxEnergy = 10    
    minEnergy = 0

    tiredThreshold = 5 ### for future implementation
    
    
    def __init__(self,firstName = None, lastName = None, age = None,
                 height = None, weight = None, reach = None, weightClass = None, strenght = None,
                 dexterity = None, style = None, wins = None, losses = None,
                 draws = None, knockdowns = None, winsKoTko = None,
                 winsDecision = None, winsSubmission = None):

        self._index = Fighter.numIndexes   ### gives fighter his unique id 
        Fighter.numIndexes += 1            ### updating class variable

        ### fighters attributes
        self._firstName = firstName
        self._lastName = lastName
        self._age = age
        self._height = height
        self._weight = weight
        self._reach = reach
        self._weightClass = weightClass
        self._strenght = strenght
        self._dexterity = dexterity
        self._style = style
        self._wins = wins
        self._losses = losses
        self._draws = draws
        self._knockdowns = knockdowns
        self._winsKoTko = winsKoTko
        self._winsDecision = winsDecision
        self._winsSubmission = winsSubmission
        self._life = Fighter.maxLife
        self._energy = Fighter.maxEnergy

    def __str__(self):                                 ### print(fighter) prints fighter's attributes
        return ('< Fighter{}:'.format(self.index) +
                '\n -- Full Name: ' + self.firstName + ' ' + self.lastName +
                '\n -- Age: ' + str(self.age) +
                '\n -- Weightclass: ' + self.weightClass +
                '\n -- Height: ' + str(self.height) +
                '\n -- Weight: ' + str(self.weight) +
                '\n -- Reach: ' + str(self.reach) +
                '\n -- Wins: ' + str(self.wins) +
                '\n -- Losses: ' + str(self.losses) +
                '\n ->')

    ## setters and getters using python's property function -- to be reviwed
    ## getters:

    @property
    def index(self):
        return self._index                
    @property
    def firstName(self):
        return self._firstName
    @property
    def lastName(self):
        return self._lastName
    @property
    def age(self):
        return self._age
    @property
    def height(self):
        return self._height
    @property
    def weight(self):
        return self._weight
    @property
    def reach(self):
        return self._reach
    @property
    def weightClass(self):
        return self._weightClass
    @property
    def strenght(self):
        return self._strenght
    @property
    def dexterity(self):
        return self._dexterity
    @property
    def style(self):
        return self._style
    @property
    def wins(self):
        return self._wins
    @property
    def losses(self):
        return self._losses
    @property
    def draws(self):
        return self._draws
    @property
    def winsKoTko(self):
        return self._winsKoTko
    @property
    def winsDecision(self):
        return self._winsDecision
    @property
    def winsSubmission(self):
        return self._winsSubmission
    @property
    def life(self):
        return self._life
    @property
    def energy(self):
        return self._energy

    ##setters -- ensures bounds of each variable

    @firstName.setter
    def firstName(self,firstName):
        self._firstName = str(firstName)
    @lastName.setter
    def lastName(self,lastName):
        self._lastName = str(lastName)
    @height.setter
    def height(self, height):
        self._height = abs(height)
    @weight.setter
    def weight(self, weight):
        self._weight = abs(weight)
    @reach.setter
    def reach(self, reach):
        self._reach = abs(reach)
    @strenght.setter
    def strenght(self,strenght):
        self._strenght = abs(strenght)
    @dexterity.setter
    def dexterity(self, dexterity):
        self._dexterity = abs(dexterity)
    @style.setter
    def style(self, style):
        if style in styles:
            self._style = style
        else:
            raise ValueError('Style not in styles')  ### only previously hardcoded styles are allowed
    @wins.setter                                     ### this is just to filter bad data
    def wins(self, wins):
        self._wins = wins
    @losses.setter
    def losses(self, losses):        
        self._losses = losses
    @draws.setter
    def draws(self, draws):
        self._draws = draws
    @winsKoTko.setter
    def winsKoTko(self, winsKoTko):
        self._winsKoTko = winsKoTko
    @winsDecision.setter
    def winsDecision(self, winsDecision):
        self._winsDecision = winsDecision
    @winsSubmission.setter
    def winsSubmission(self, winsSubmission):
        self._winsSubmission = winsSubmission
    @life.setter
    def life(self, life):            ### life and energy must respect bounds
        if life > Fighter.maxLife:
            self_life = Fighter.maxLife
        elif life < Fighter.minLife:
            self_life = Fighter.minLife
        else:
            self._life = life
    @energy.setter
    def energy(self, energy):
        if energy > Fighter.maxEnergy:
            self_energy = Fighter.maxEnergy
        elif energy < Fighter.minEnergy:
            self_energy = Fighter.minEnergy
        else:
            self._energy = energy
            
    ## event, fight and fighter conditions functions:

    def isInEvent(self,event):
        """Returns true if fighter is in the event"""
        return (self in event)
    def isInFight(self,fight):
        """Returns true if fighter is in the fight"""
        return (self in fight)
    def isTired(self):
        """Returns true if fighter is tired"""
        return (self._energy < tiredThreshold)   ### actually it is implemented !
    def isKO(self):
        """Returns true if fighter is K.O."""
        return (self._life == 0)

    ## strikes -- no implementation yet

    ## defenses / moves -- no implementation yet


def generateRandomFighter(size = 1.0, i = 0):

    """Assumes size a float and i an integer.
       Generates and returns a fighter with random plausible (normal) attributes proportional to size."""

    size = size*pl.normal(loc = 1.0, scale = 0.05)               ### a lot of variables and weights here are arbitrary..
    print("Generating fighter size... ".format(i),size)          ### i tried reasoning, like weight and strenght go with
    fighter = Fighter(firstName = 'John{}'.format(i),            ### size***3 because they grow with the volume...
                      lastName = 'Cage{}'.format(i),             ### on the other hand, height grows linearly with size
                      age = pl.randint(18,40), 
                      height = round(pl.normal(loc = 175*size, scale = 3)),
                      weight = round(pl.normal(loc = 75.0*(size**3), scale = 2.0),1),
                      reach = round(pl.normal(loc = 175*size, scale = 1)),
                      weightClass = pl.choice(Fighter.weightClasses),  ## this is just silly.. just to get a value
                      strenght = round(pl.normal(loc = 7.0*(size**3), scale = 2.0),1),
                      dexterity = round(pl.normal(loc = 7.0*(1/(size**4)), scale = 1.0),1),
                      )
    return fighter


class Fight():  ### in progress... 

    """ Simulates a fight between fighters Red and Blue.
        Generates fighters if none are passed as arguments."""

    def __init__(self, fighterRed = generateRandomFighter(i=1), fighterBlue = generateRandomFighter(i=2)):
        ring1 = Ring('Square Ring 1',20,20, fighterRed = fighterRed , fighterBlue = fighterBlue)
        fighterRed = ring1.fightersInRing[0]
        fighterBlue = ring1.fightersInRing[1]
        redLocation = ring1.fightersLocations[0]
        blueLocation = ring1.fightersLocations[1]
        print(ring1)
        pygame.init()
        pygame.display.set_caption('FA MMA Simulation')
        screen_size_x = 400
        screen_size_y = 400
        screen = pygame.display.set_mode((screen_size_x,screen_size_y))
        redPixPosition = ( redLocation.coord[0]*screen_size_x/ring1.x_size,
                           redLocation.coord[1]*screen_size_y/ring1.y_size )
        bluePixPosition = ( blueLocation.coord[0]*screen_size_x/ring1.x_size,
                            blueLocation.coord[1]*screen_size_y/ring1.y_size )
        redSkin = pygame.Surface((20,20))
        pygame.draw.circle(redSkin, (255,0,0), (10,10), 10)
        blueSkin = pygame.Surface((20,20))
        pygame.draw.circle(blueSkin, (0,0,255), (10,10), 10)
        clock = pygame.time.Clock()
        while True:
            clock.tick(20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            ring1.moveFighter(fighterRed,pl.uniform(-1,1),pl.uniform(-1,1))
            ring1.moveFighter(fighterBlue,pl.uniform(-1,1),pl.uniform(-1,1))
            redPixPosition = ( redLocation.coord[0]*screen_size_x/ring1.x_size,
                               redLocation.coord[1]*screen_size_y/ring1.y_size )
            bluePixPosition = ( blueLocation.coord[0]*screen_size_x/ring1.x_size,
                                blueLocation.coord[1]*screen_size_y/ring1.y_size )
            screen.fill((0,0,0))
            screen.blit(redSkin,redPixPosition)
            screen.blit(blueSkin,bluePixPosition)
            pygame.display.update()
            



if __name__ == "__main__":  ## test program starts here

    Fight()
        
    print("Base class Fighters index is ",Fighter.numIndexes) ## print total number of fighters created, just for debugging

