import random
import math
from datetime import datetime

#def buildingAndBuyingAStructure():

#def carousing():

#def crafting():

#copy pit fighting and rework it
#def gambling():

#def gatherInformation():

#def harvesting():

#def mercantilism():

#def practicingAProfession():

#def recuperating():

#def researchingLore():

#def revelry():

#def shopping():


def therapy(name: str, days: int, therapistContact: bool, lifestyleTravelCost: int, medicineModifier: int):
    sanityReduction = max(4, medicineModifier)
    therapyCost = 0
    goldCost = days*lifestyleTravelCost    

    if(days > 3):
        if( therapistContact):
            print(name + " has conducted therapy and been healed " + str(sanityReduction) + " sanity damage.")
        else:
            print(name + " has conducted therapy and been healed " + str(sanityReduction) + " sanity damage and has costed them " + str(goldCost) + " gold.")


#def travel(name: str, days: int, ):

#def volunteering():


# region, settlement, and days need to be inputs, the rest can be grabbed from their character sheet.
def adventure(name: str, days: int, level: int, region :str, settlement: str):
    goldGain = 0
    influenceGain = 0
    tickGain = 6*days
    hirelingTier = 0
    tierOfPlay = 0

    if (level>16):
        hirelingTier = 5
        goldGain = 55*days
    elif (level>12):
        hirelingTier = 4
        goldGain = 35*days
    elif (level>8):
        hirelingTier = 3
        goldGain = 20*days
    elif (level>4):
        hirelingTier = 2
        goldGain = 5*days
    else: 
        hirelingTier = 1
        goldGain = 1*days

    if (level>17):
        tierOfPlay = 6
    elif (level>15):
        tierOfPlay = 4
    elif (level>12):
        tierOfPlay = 3
    elif (level>8):
        tierOfPlay = 2
    elif (level>4):
        tierOfPlay = 2
    else: 
        tierOfPlay = 1

    influenceCycles = (math.floor(days/7))*(tierOfPlay)
    incrementor = 0
    while(influenceCycles >0):
        influenceRoll = random.randint(1,4)
        incrementor += 1
        print("Influence roll #" + str(incrementor) + ": " + str(influenceRoll))
        influenceGain += influenceRoll
        influenceCycles -= 1
    
    print(name + " spent " + str(days) + " days adventuring in " + settlement + ", " + region + " and has gained " + str(tickGain) + " xp ticks, " + str(goldGain) + " gold, and " + str(influenceGain) + " influence in both locations.")

# days needs to be an input, rest can be grabbed from sheet
# this is one of the ones that we are going to want to maybe not let it infinitely scale with days DC 23 with 10 days and a really basic deception is quite a lot
def alibi(name: str, days: int, deception: int):
    investigationDC = 10 + deception + (4*math.floor(days/5))
    additionalCreatures = 5+days

    print(name + " creates an alibi for themselves and upto " + str(additionalCreatures) + " additional creatures. The DC to see through this alibi is " + str(investigationDC) + ".")

# has too much staff stuff to be automated full, will return to see how much can be manually input
#def blackmail(name: str, target: str, days: int, targetInfluenceSpending: int, playerInfluenceSpending: int):
#def coerce

# days and baseDC need to be inputed. name, passiveTotal, and profBonus can be grabbed from sheet. For prof bonus, find the max of the Acro Athl Invest Perc or Tact and get the prof bonus, becomes 0 if doesnt have any.
def guarding(name: str, days: int, level: int, passiveTotal: int, baseDC: int, profBonus: int):
    tickGain = 3*days
    goldGain = 0
    totalGuardDC = baseDC

    if (level>16):
        hirelingTier = 5
        goldGain = 55*days
    elif (level>12):
        hirelingTier = 4
        goldGain = 35*days
    elif (level>8):
        hirelingTier = 3
        goldGain = 20*days
    elif (level>4):
        hirelingTier = 2
        goldGain = 5*days
    else: 
        hirelingTier = 1
        goldGain = 1*days

    if(days > 6):
        if(passiveTotal > baseDC):
            totalGuardDC = passiveTotal
        else: 
            totalGuardDC = baseDC + profBonus

    print(name + " guards the location for " + str(days) + " days and gains " + str(tickGain) + " xp ticks and " + str(goldGain) + " gold. The DC to preform nefarious deeds is now " + str(totalGuardDC))

#Needs an event handler
#def infiltrate()

#instert my pit fighting calculator here
def loseALimb():
    random.seed(datetime.now().timestamp())
    limbRoll = random.randint(1,6)
    limbList = ["Fingers", "Hand", "Arm", "Toes", "Foot", "Leg"]
    if (limbRoll == 1 or limbRoll == 4):
        limbType = limbList[limbRoll-1] + "with a quantity roll of " + str(random.randint(1,3)) + "(1d3) "
    else:
        limbType = limbList[limbRoll-1]
    
    limbType = "Limb roll of " + str(limbRoll) + "(1d6) losing: " + limbType
    theLostLimb = "You are maimed in your fight, your Event Handler will roll randomly to determine what limb or appendage of yours is lost during your fight. It can only be restored through magical means or through means such as regeneration. \n" + limbType

    return(theLostLimb)

def pitFighting(name: str, days: int, goldBet: int):

    whatLostLimb = loseALimb()
    complicationList = ["You are accused of cheating. You decide whether you actually did cheat or were framed.*",
                        "The town guards raid the fighting den. See Event Handler to determine if you avoid capture, and thus Jail time. If pit fighting is legal in your region. This event may be a different organizational raid, such as a rival guild, or is simply a reroll.*",
                        "A noble in town loses badly to you and loudly vows to get revenge.*",
                        "You won a sum from a low-ranking member of a thieves’ guild, and the guild wants its money back.*",
                        "A local crime boss insists you start frequenting the boss’s fighting pits and no others.",
                        "You accrue a debt with the pit fighting organization, equal to your original bet.*",
                        "You accrue a debt with the pit fighting organization, equal to double your original bet.*",
                        "A high-stakes pitmaster comes to town and insists that you take part in a game.",
                        "The crowd loses favor with you. You lose " + str((random.randint(1,6))*5) + "(1d6x5)Influence with the Pit Fighting organization and the city it took place in.*",
                        "You are injured in your fight, and lose 3 DTDs as you must recover from your injuries. These DTDs are lost as soon as you are able to lose them.",
                        "You are injured in your fight, and suffer a level of Exhaustion until you spend 6 DTDs Recuperating. You must do this for every level of Exhaustion gained in this way.",
                        whatLostLimb]

    loops = math.floor(days/7)
    incrementor = 0
    gold = goldBet
    bank = 0
    
    while (loops > 0 or gold>100):
        whatLostLimb = loseALimb()
        complicationOdds = 5

        acroDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
        athlDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
        tactDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
        
        incrementor += 1
        
        print(name + " has the following DCs for pit fighting #" + str(incrementor))
        

        print("Acrobatics DC: " + str(acroDC))
        print("Athletics DC: " + str(athlDC))
        print("Tactics DC: " + str(tactDC))
        verification = False
        while(not verification):
            verification = True
            sucesses = input("How many of the DCs did " + name + " meet or beat? ")
            
            try:
                int(sucesses)
            except:
                print("Bad input. Try again please :3")
                verification = False
            else:
                sucesses = int(sucesses)
                if(sucesses == 3):
                    gold = gold*2
                elif(sucesses == 2):
                    gold = gold*1.5
                    complicationOdds += 5
                elif(sucesses == 1):
                    gold = gold*0.5
                    complicationOdds += 10
                elif(sucesses == 0):
                    gold = 0
                    complicationOdds += 200
                else:
                    print("Bad input. Try again please :3")
                    verification = False
                loops -= 1
                complicationRoll = random.randint(1,100)
                if(complicationRoll < complicationOdds):
                    print(name + " rolled a " + str(complicationRoll) + " on the d100 vs a complication chance of "+ str(complicationOdds) + "% and A complication has occured.")
                    print(complicationList[random.randint(12,12)-1])
                else:
                    print(name + " rolled a " + str(complicationRoll) + " on the d100 vs a complication chance of "+ str(complicationOdds) + "% and avoided a complication.")
                if(gold > 5000):
                    bank = gold-5000
                    gold = 5000
        gold = gold+bank
        print(name + "'s initial bet of " + str(goldBet) + " has returned them " + str(gold) + " gold from their " + str(incrementor) + " pit fight(s) for a net total change of " + str(gold-goldBet) + " gold.")
            





        



# days is the only input, name can be taken from sheet. Inspiration cap might be also grabbable along with lifestyle reduction stuff
def performingSacredRites(name: str, days: int):
    tickGain = 2*days
    lifeStyleReduction = min(50, 25*(math.floor(days/3)))
    inspirationGain = math.floor(days/7)

    print(name + " performes sacred rites for " + str(days) + " days gaining " + str(tickGain) + " xp ticks, " + str(inspirationGain)+ " inpiration up to their cap, and reduced their lifestyle expenses by " + str(lifeStyleReduction) + "%.")

#def researchingSpells():

# days, missionName are inputs, researcher and name can be grabbed from sheet.
def schemeForAnAdventure(name: str, days: int, missionName: str, researcher: bool):
    level = "None"
    if(researcher and days>14):
        level = "Detailed"
    elif(days>9):
        level = "Studied"
    elif(days>4):
        level = "Informed"
    else:
        level = "Basic"
    
    print(name + " schemed for " + missionName + " for a total of " + str(days) + " days and has gained a " + level + " level of information about the mission.")


# another one on the docket to reduce the effects of
#def sowingRumors():
    

#def tameACreature():
    

#def training():


#Test cases
# adventure("Quinn", 14, 5, "Dolider", "Angullous")
# alibi("Quinn", 10, 5)
# guarding("Quinn", 7, 5, 10, 4, 6)
# performingSacredRites("Quinn", 21)
# schemeForAnAdventure("Kei", 15, "The Blight Bargain", True)
# therapy("Gagun", 4, False, 4, 2)
    
pitFighting("Quinn", 77, 100)