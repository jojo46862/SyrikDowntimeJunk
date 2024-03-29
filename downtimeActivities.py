import random
import math
from datetime import datetime

#def buildingAndBuyingAStructure():

#def carousing():

#def crafting():

# has days and gold bet as input, name can be taken from sheet, and goldbet can be verified on the sheet
def gambling(name: str, days: int, goldBet: int):
    complicationList = ["You are accused of cheating. You decide whether you actually did cheat or were framed.*",
                        "The town guards raid the gambling hall. See Event Handler to determine if you avoid capture, and thus Jail time. If gambling is legal in your region. This event may be a different organizational raid, such as a rival guild.*",
                        "A noble in town loses badly to you and loudly vows to get revenge.*",
                        "You won a sum from a low-ranking member of a thieves’ guild, and the guild wants its money back.*",
                        "A local crime boss insists you start frequenting the boss’s gambling parlor and no others.",
                        "You accrue a debt with the gambling organization, equal to your original bet.*",
                        "You accrue a debt with the gambling organization, equal to double your original bet.*",
                        "A high-stakes gambler comes to town and insists that you take part in a game."]

    loops = math.floor(days/7)
    incrementor = 0
    gold = goldBet
    bank = 0
    
    while (loops > 0 and gold>9):
        complicationOdds = 5

        insiDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
        deceDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
        intiDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
        
        incrementor += 1
        
        print(name + " has the following DCs for gambling #" + str(incrementor))
        
        print("Insight DC: " + str(insiDC))
        print("Deception DC: " + str(deceDC))
        print("Intimidation DC: " + str(intiDC))
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
                    complicationOdds += 20
                else:
                    print("Bad input. Try again please :3")
                    verification = False
                loops -= 1
                complicationRoll = random.randint(1,100)
                if(complicationRoll < complicationOdds):
                    print(name + " rolled a " + str(complicationRoll) + " on the d100 vs a complication chance of "+ str(complicationOdds) + "% and A complication has occured.")
                    whichComplicationEvent = random.randint(1,8)-1
                    print(complicationList[whichComplicationEvent])
                    if(not (whichComplicationEvent == 4 or whichComplicationEvent == 7)):
                        print("* = (This may involve a rival).")
                else:
                    print(name + " rolled a " + str(complicationRoll) + " on the d100 vs a complication chance of "+ str(complicationOdds) + "% and avoided a complication.")
        if(gold > 1000):
            bank += gold-1000
            gold = 1000
        
        print(name + "'s initial bet of " + str(goldBet) + " has returned them " + str(gold+bank) + " gold from their " + str(incrementor) + " gambling(s) for a net total change of " + str(gold+bank-goldBet) + " gold.")


#def gatherInformation():

#def harvesting():

#def mercantilism():

#def practicingAProfession():

#takes days as input, name and chaMod can be taken from sheet
def recuperating(name: str, days: int, chaMod: int):
    weekly = ""
    if(days > 6):
        weekly = " and recovers week long refreash features"
    print(name + " recovers expended Long Rest features" + weekly + ".")
    if(days > 2):
        print(name + " gains advantage on saving throws to recover from long-acting diseases and poisions for one week, including the days spend relaxing. They can also end one effect that keeps them from regaining hit points, or can restore one ability score that has been reduce to less than its normal value. This does not work on magical effects that have ongoing durations or have a specific listed means to recover.")
        print(name + " reduces any moderate or lover corruption they are suffering from by 1.") #if the intention is to have 6 days reduce it by more, change 1 to [" + math.floor(days/3) + "]
    if(days > 5):
        print(name + " reduces sanity damage by " + str(chaMod) + ".")


#def researchingLore():

#This one seems to be missing a good amount of information from the DTD page. Should be updated.
def revelry(name: str, days: int, lifeSytleCost: int, chaMod: int, conMod: int):
    goldCost = days*lifeSytleCost
    inspirationGain = min(3, math.floor(days/2))
    sanityReduction = math.floor(days/7)*chaMod
    conCheckDC = 8 + math.floor(days/2)

    conCheckRoll = random.randint(1,20)
    if(conCheckRoll+conMod < conCheckDC):
        print(name + " rolled a " + str(conCheckRoll+conMod) + "=" + str(conCheckRoll) + "+" +str(conMod) + " against a DC" + str(conCheckDC) + " and [ROLL ON REVELRY TABLE].")
    else:
        print(name + " rolled a " + str(conCheckRoll+conMod) + "=" + str(conCheckRoll) + "+" +str(conMod) + " against a DC" + str(conCheckDC) + " and is chilling after their revelry.")
    print(name + " must spend " +  str(goldCost) + " gold to gain " + str(inspirationGain) + " inspiration(s) upto their cap and recudes any sanity damage they are suffering from by " + str(sanityReduction) + ".")

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
    tierOfPlay = 0
    textOutput = ""

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
        textOutput = textOutput + ("Influence roll #" + str(incrementor) + ": " + str(influenceRoll)) + "\n"
        influenceGain += influenceRoll
        influenceCycles -= 1
    
    textOutput = textOutput + "-------------------\n"
    
    textOutput = textOutput + (name + " spent " + str(days) + " days adventuring in " + settlement + ", " + region + " and has gained " + str(tickGain) + " xp ticks, " + str(goldGain) + " gold, and " + str(influenceGain) + " influence in both locations.")
    return textOutput

# days needs to be an input, rest can be grabbed from sheet
# this is one of the ones that we are going to want to maybe not let it infinitely scale with days DC 23 with 10 days and a really basic deception is quite a lot
def alibi(name: str, days: int, deception: int):
    investigationDC = 10 + deception + (4*math.floor(days/5))
    additionalCreatures = 5+days

    return(name + " creates an alibi for themselves and upto " + str(additionalCreatures) + " additional creatures. The DC to see through this alibi is " + str(investigationDC) + ".")

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

#goldBet and days are inputs, name can be taken from sheet. Goldbet can be verified to make sure they do have that gold. Lose a limb a sub function of Pit Fighting for the hopefully rare limb loss
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

def pitFighting():

    
    acroDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
    athlDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
    tactDC = random.randint(1,10) + random.randint(1,10) + random.randint(1,10) + 5
        
    '''
    while (loops > 0 and gold>99):
        whatLostLimb = loseALimb()
        

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
                
    '''
    return acroDC, athlDC, tactDC

def pitFightingResults(name: str, days: int, goldBet: int, sucesses: int):
    
    complicationOdds = 5
    whatLostLimb = loseALimb()
    complicationList = ["You are accused of cheating. You decide whether you actually did cheat or were framed.*",
                        "The town guards raid the fighting den. See Event Handler to determine if you avoid capture, and thus Jail time. If pit fighting is legal in your region. This event may be a different organizational raid, such as a rival guild, or is simply a reroll.*",
                        "A noble in town loses badly to you and loudly vows to get revenge.*",
                        "You won a sum from a low-ranking member of a thieves’ guild, and the guild wants its money back.*",
                        "A local crime boss insists you start frequenting the boss’s fighting pits and no others.",
                        "You accrue a debt with the pit fighting organization, equal to your original bet.*",
                        "You accrue a debt with the pit fighting organization, equal to double your original bet.*",
                        "A high-stakes pitmaster comes to town and insists that you take part in a game.",
                        "The crowd loses favor with you. You lose " + str((random.randint(1,6))*5) + " (1d6x5)Influence with the Pit Fighting organization and the city it took place in.*",
                        "You are injured in your fight, and lose 3 DTDs as you must recover from your injuries. These DTDs are lost as soon as you are able to lose them.",
                        "You are injured in your fight, and suffer a level of Exhaustion until you spend 6 DTDs Recuperating. You must do this for every level of Exhaustion gained in this way.",
                        whatLostLimb]

    loops = math.floor(days/7)
    textOutput = ""
    incrementor = 0
    gold = goldBet

    xpTicks = 6*days
    influenceRolls = 0
    if(sucesses == 3):
        gold = gold*2
        influenceRolls += 3
    elif(sucesses == 2):
        gold = gold*1.5
        complicationOdds += 5
        influenceRolls += 2
    elif(sucesses == 1):
        gold = gold*0.5
        complicationOdds += 10
        influenceRolls += 1
    elif(sucesses == 0):
        gold = 0
        complicationOdds += 20
    complicationRoll = random.randint(1,100)
    if(complicationRoll < complicationOdds):
        #print(name + " rolled a " + str(complicationRoll) + " on the d100 vs a complication chance of "+ str(complicationOdds) + "% and A complication has occured.")
        textOutput = textOutput + (name + " rolled a " + str(complicationRoll) + " on the d100 vs a complication chance of "+ str(complicationOdds) + "% and a complication has occured.") + "\n"
        whichComplicationEvent = random.randint(1,12)-1
        textOutput = textOutput + (complicationList[whichComplicationEvent]) + "\n"
        if(whichComplicationEvent < 7 or whichComplicationEvent == 8):
            textOutput = textOutput + ("\* = (This may involve a rival).") + "\n"
    else:
        textOutput = textOutput + (name + " rolled a " + str(complicationRoll) + " on the d100 vs a complication chance of "+ str(complicationOdds) + "% and avoided a complication.") + "\n"
        

        
        
    textOutput = textOutput + (name + "'s initial bet of " + str(goldBet) + " has returned them " + str(gold) + " gold from their pit fight for a net total change of " + str(gold-goldBet) + " gold.") + "\n"
    incrementor = 0
    influenceGainTotal = 0
    textOutput = textOutput + "-------------------\n"
    if(influenceRolls == 0):
        textOutput = textOutput + "No influence gain.\n"
    while (incrementor < influenceRolls):
        influenceGain = random.randint(1,4)
        influenceGainTotal += influenceGain
        textOutput = textOutput + ("Influence roll #" + str(incrementor+1) + ": " + str(influenceGain)) + "\n"
        incrementor += 1
    textOutput = textOutput + "-------------------\n"
    
    textOutput = textOutput + (name + " has also earned " + str(xpTicks) + " xp ticks and " + str(influenceGainTotal) + " (" + str(influenceRolls)+"d4) influence in the pit fighting organization and the city") + "\n"
    
    return textOutput


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
    
#Technically only the taming side, still needs tork on the training stuff in a different function
# Need to be input: days, creatureHDQuanitity, creatureStrScore, creatureIntScore, creatureChaScore, creatureAlignment, creatureCR, docile, advanced
# Can be grabbed from the sheet: name, playerAlignment, tamerToolLevel, tamersToolMod, playerAnimalHandling
def tameACreature(name: str, days: int, creatureHDQuanitity: int, creatureStrScore: int, creatureIntScore: int, creatureChaScore: int, 
                  creatureAlignment: str, creatureCR: int, docile: bool, advanced: bool, playerAlignment: str, tamerToolLevel: str, tamersToolMod: int, playerAnimalHandling: int):
    
    # Having a while(True) lets it break at different points if the player cannot do something for a reason.
    while(True):
        # Taming DC Calcuation
        chaAdd = 0.0
        intAdd = 0.0
        strAdd = 0.0
        alignmentSteps = 0
        verification = True
        if(creatureAlignment[0] != 'L' or creatureAlignment[0] != 'N' or creatureAlignment[0] != 'C'):
            verification = False
        if(creatureAlignment[1] != 'G' or creatureAlignment[1] != 'N' or creatureAlignment[1] != 'E'):
            verification = False
        

        if(creatureAlignment != "TN" and verification):
            if(playerAlignment[0] == 'L'):
                if(creatureAlignment[0] == 'N'):
                    alignmentSteps += 1
                elif(creatureAlignment[0] == 'C'):
                    alignmentSteps += 2
            elif(playerAlignment[0] == 'N'):
                if(creatureAlignment[0] != 'N'):
                    alignmentSteps += 1
            else:
                if(creatureAlignment[1] == 'N'):
                    alignmentSteps += 1
                elif(creatureAlignment[1] == 'L'):
                    alignmentSteps += 2

            if(playerAlignment[1] == 'G'):
                if(creatureAlignment[1] == 'N'):
                    alignmentSteps += 1
                elif(creatureAlignment[1] == 'E'):
                    alignmentSteps += 2
            elif(playerAlignment[1] == 'N'):
                if(creatureAlignment[1] != 'N'):
                    alignmentSteps += 1
            else:
                if(creatureAlignment[1] == 'N'):
                    alignmentSteps += 1
                elif(creatureAlignment[1] == 'G'):
                    alignmentSteps += 2
            

        if(docile):
            chaAdd = creatureChaScore*0.5
        else:
            chaAdd = creatureChaScore*1.5


        if(creatureIntScore < 6):
            intAdd = (6-creatureIntScore)*2
        else:
            intAdd = (math.floor((creatureIntScore-10)/2))


        strAdd = creatureStrScore/5


        if(advanced):
            bonusAdd = 4 + float(alignmentSteps)*2
        else:
            bonusAdd = float(alignmentSteps)*2

        trainingDC = math.floor(10 + float(creatureCR) + chaAdd + intAdd + strAdd + bonusAdd)

        # Can they tame it
        maxTamersOrAH = max(tamersToolMod, playerAnimalHandling)
        tamingScore = 10 + tamersToolMod + playerAnimalHandling
        canTheyTameIt = False
        
        if(tamingScore+1>trainingDC):
            canTheyTameIt = True
        else:
            print(name + " has a taming score of " + str(tamingScore) + " but they need a taming score of " + str(trainingDC) + " to tame this creature.")
            break
     
        
        #Dowmtime Days Needed
        daysNeededMod = 10
        
        if(tamerToolLevel == "P"):
            daysNeededMod = 9
        elif(tamerToolLevel == "E"):
            daysNeededMod = 8
        elif(tamerToolLevel == "M"):
            daysNeededMod = 6

        daysNeeded = creatureHDQuanitity*daysNeededMod
        if(daysNeeded > days):
            print(name + " needs to spend " + str(daysNeeded) + " days to tame this creature. They have only spent " + str(days) + " days.")
            break
        else:
            print(name + " sucessfully tames the creature.")
            break

#def trainACreature()
        

        



#def training():


#Test cases
# adventure("Quinn", 14, 5, "Dolider", "Angullous")
# alibi("Quinn", 10, 5)
# guarding("Quinn", 7, 5, 10, 4, 6)
# performingSacredRites("Quinn", 21)
# schemeForAnAdventure("Kei", 15, "The Blight Bargain", True)
# therapy("Gagun", 4, False, 4, 2)   
# pitFighting("Quinn", 7, 2500)
# gambling("Quinn", 28, 1000)
# revelry("Quinn", 14, 3, 1, 3)
# recuperating("Quinn", 6, 2)
# tameACreature("Quinn", 72, 12, 26, 17, 12, "NE", 15, False, True, "NE", "M", 22, 23)