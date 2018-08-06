
print("Guide to using Create Your Soldier:")
print("")
print("Skill points can increase soldier speed, the range of your equipped gun and the damage of your equipped gun")
print("To start off you have been given 5 extra skill points to assaign on top the of already assaigned 10 after choosing your class")
print("Speed - Soldier Speed, Aim - Increase in distance, Strength - Increase in damage")
print("")
print("To assign skill points type:")
print("Player.ASSIGNSKILLS(Amout of points to Speed, Amount of points to Aim, Amount of points to strength)")
print("")
print("To add a new gun to your collection:")
print("Type: Player.ADDGUN('The name of the weapon', The range of the gun, 'The build of the gun')")
print("The range of the gun is in meters and will affect the damage the gun is capable of, please enter an whole number")
print("Remember that the build of your gun affects the damage, you can choose either 'AR', 'Shotgun' or 'Sniper'")
print("")
print("To check your Storage (Where your guns are guns are stored) or your Loadout (Your active loadout) or your Skills (Your skill points):")
print("Type Player.SHOWSTORAGE() or Player.SHOWLOADOUT() or Player.SHOWSKILLS() and also P.SHOWSTATS() to see the stats of your gun")
print("")
print("To equip your new gun into your primary slot (Which will reveive the buffs from your skills) type: ")
print("Player.EQUIPNEWGUN('The gun name in quotation marks')")
print("")

''' PROBLEMS TO SOLVE:
     - The damage system
     - The skill system needs to be applied

'''

Storage = { }
Loadout = { }
SkillSet = { }
PrimaryStats = { }
playerName = str(input("What is your name soldier? "))
classType = str(input("What type of soldier are you? (Fighter, Scout, Heavy)? "))

secondaryWep = ""
utilWep = ""

skillSpeed = 0
skillAim = 0
skillStren = 0

class P(object):

    # name is name of gun, distance is range bullet can go, build is type of gun
    def ADDGUN(name, distance, build):
        global Storage
        damage = 0

        if build == "Sniper":
            damage = distance / 100 * 120
        elif build == "AR":
            if distance <= 40:
                damage = distance * 1.6
            elif distance > 40 and distance <= 70:
                damage = distance * 1.2
            else:
                damage = distance * 0.5
        elif build == "Shotgun":
            if distance <= 15:
                damage = distance * 8
            elif distance > 15 and distance <= 25:
                damage = distance * 3
            else:
                damage = distance * 0.5
        else:
            damage = 0

        print("")
        print("Your new weapon is the " + name + ", it is a " + build + " with a range of " + str(distance) + "m and has a base damage of " + str(damage))
        print("")
        gunStats = (build, distance, damage)
        Storage[name] = gunStats

    #Creating a base loadout
    def weapon(self):
        global Loadout
        global secondaryWep
        global utilWep
        global PrimaryStats

        if classType == "Fighter":
            primary = "Basic Assault Rifle"
            assaultGunStats = ("AR", 30, 45)
            PrimaryStats["Basic Assault Rifle"] = assaultGunStats
            secondary = str(input("P250 or USP-S? "))
            util = str(input("Grenade or Flash? "))
        elif classType == "Scout":
            primary = "Basic Sniper Rifle"
            scoutGunStats = ("Sniper", 100, 90)
            PrimaryStats["Basic Sniper Rifle"] = scoutGunStats
            secondary = str(input("Deagle or Revolver? "))
            util = str(input("Claymore or Flash? "))
        elif classType == "Heavy":
            primary = "Basic Shotgun"
            heavyGunStats = ("Shotgun", 15, 40)
            PrimaryStats["Basic Shotgun"] = heavyGunStats
            secondary = str(input("P2000 or Revolver? "))
            util = str(input("Grenade or C4? "))
        else:
            primary = "None"
            secondary = "None"
            util = "None"
        secondaryWep = secondary
        utilWep = util

        gunLoad = (primary, secondary, util)
        Loadout["Base Loadout"] = gunLoad

    #Creating a description
    def createDesc(self, secondary, util):
        global PrimaryStats
    
        primaryName = ""
        
        for key in PrimaryStats:
            primaryName = key

        print("")
        print("Your basic primary weapon is: " + primaryName + ", your secondary weapon is: " + secondary + " and your utility is: " + util)
        print("")

    #Setting base skills
    def setBaseStats(self):
        global SkillSet
        global skillSpeed
        global skillAim
        global skillStren
        speed = 0
        aim = 0
        strength = 0

        if classType == "Scout":
            #Sniper Stuff
            speed = 4
            aim = 4
            strength = 2
        elif classType == "Fighter":
            #AR stuff
            speed = 4
            aim = 2
            strength = 4
        elif classType == "Heavy":
            #Shotgun stuff
            speed = 5
            aim = 0
            strength = 5
        else:
            speed = 0
            aim = 0
            strength = 0

        skillSpeed = speed
        skillAim = aim
        skillStren = strength

        skillSet = (speed, aim, strength)
        SkillSet["Skills"] = skillSet

    #Adding Skill points
    def ASSIGNSKILLS(speed, aim, strength):

        global skillSpeed
        global skillAim
        global skillStren
        global SkillSet
        if(speed + aim + strength) <= 5:
            newSpeed = (speed + skillSpeed)
            skillSpeed = newSpeed

            newAim = (aim + skillAim)
            skillAim = newAim

            newStren = (strength + skillStren)
            skillStren = newStren

            #Updating Skills Dictionary
            SkillSet.pop("Skills", None)
            skillSet = (skillSpeed, skillAim, skillStren)
            SkillSet["Skills"] = skillSet
        else:
            print("Your total amount of points assigned was higher than 5")

    #Equipping a new gun
    def EQUIPNEWGUN(gunName):

        global Loadout
        global Storage
        global PrimaryStats

        if gunName in Storage:
            print(gunName + " is in your storage")
            x = input("Are you sure you want to equip the " + gunName + " as your primary weapon? (YES or NO): ")
            if x == "YES":

                #Remove old Primary and put old gun in storage (also remove old one)
                for key in PrimaryStats:
                    oldGunName = key
                for valuess in PrimaryStats.values():
                    oldStats = valuess
                newGunStats = Storage.get(gunName)
                Storage[oldGunName] = oldStats
                Storage.pop(gunName, None)
                PrimaryStats.pop(oldGunName, None)
                #Set new PrimaryStats
                PrimaryStats[gunName] = newGunStats
                #Remove everything from loadout
                for key in Loadout:
                    oldLoadout = key
                Loadout.pop(oldLoadout, None)
                #Assign new values to Loadout
                newLoadout = (gunName, secondaryWep, utilWep)
                Loadout["Loadout"] = newLoadout

                print(gunName + " has been equipped as your primary weapon and is now being buffed by your skills")
            else:
                print("You have said not said 'Yes' meaning that you will not be equipping the " + gunName)
        else:
            print("You dont have a gun named " + gunName + " in your storage")



    #Checking stuff
    def SHOWLOADOUT():
        print(str(Loadout))

    def SHOWSTORAGE():
        print(str(Storage))

    def SHOWSKILLS():
        print(str(SkillSet))
    def SHOWSTATS():
        print(str(PrimaryStats))

Soldier = P()
Soldier.weapon()
Soldier.setBaseStats()
Soldier.createDesc(secondaryWep, utilWep)

