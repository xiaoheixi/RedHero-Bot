# Importing required libraries.
import pyautogui
import time
import random
# Generic Attack function
def genericAttack() : 
    for attackDuration in range (3) :
        pyautogui.hotkey("5")
        time.sleep(0.3)
        pyautogui.hotkey("3")
        time.sleep(0.3)
        pyautogui.hotkey("4")
        time.sleep(0.3)
        pyautogui.hotkey("2")
        time.sleep(0.3)
        pyautogui.hotkey("1")
def bossIsStillALive() :
    bossStillAlive = 1
    while bossStillAlive == 1 :
        genericAttack()
        try:
            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.9)
            pyautogui.click(yes)
            bossStillAlive = 0
        except pyautogui.ImageNotFoundException:
            print("Boss is still alive!")
        try:
            town = pyautogui.locateOnScreen("town.png", confidence = 0.9)
            bossStillAlive = 0
        except pyautogui.ImageNotFoundException:
            print("Boss is still alive!")
def farmWorldBoss() : 
    join = pyautogui.locateOnScreen("Join.png", confidence = 0.8)
    pyautogui.click(join)
    time.sleep(3)
    try:
        drakath = pyautogui.locateOnScreen("drakath.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Drakath!")
    # try:
    #     firstspeaker = pyautogui.locateOnScreen("firstspeaker.png")
    #     for seconds in range (1) :
    #         genericAttack()
    # except pyautogui.ImageNotFoundException:
    #     print("Not Firstspeaker!")    
    try:
        red = pyautogui.locateOnScreen("red.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Red")
    try:
        paragonboss = pyautogui.locateOnScreen("paragonboss.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Paragon Boss!")    
    try:
        kuroshi = pyautogui.locateOnScreen("kuroshi.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Kuroshi!")  
    try:
        daemon = pyautogui.locateOnScreen("daemon.png", confidence = 0.9)
        try:
            daemonRoom1 = pyautogui.locateOnScreen("daemonRoom1.png", confidence = 0.9)
            pyautogui.click(daemonRoom1)
            time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Not in Daemon Room 0.")
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Daemon!")
    try:
        wesker = pyautogui.locateOnScreen("wesker.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Wesker!")    
    try:
        kongo = pyautogui.locateOnScreen("kongo.png", confidence = 0.9)
        try:
            kongoRoom1 = pyautogui.locateOnScreen("kongoRoom1.png", confidence = 0.9)
            pyautogui.click(kongoRoom1)
            time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Not in kongo Room 0.")
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Kongo!")  
    try:
        deathrealm = pyautogui.locateOnScreen("deathrealm.png", confidence = 0.8)
        try:
            deathrealmRoom1Click1 = pyautogui.locateOnScreen("deathrealmRoom1Click1.png", confidence = 0.8)
            pyautogui.click(deathrealmRoom1Click1)
            time.sleep(4)
        except pyautogui.ImageNotFoundException:
            print("Not in deathrealm Room 0.")
        try:
            deathrealmRoom1Click2 = pyautogui.locateOnScreen("deathrealmRoom1Click2.png", confidence = 0.8)
            pyautogui.click(deathrealmRoom1Click2)
            time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print("Not in deathrealm Room 0.")
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Kongo!")
    try:
        fraskfire = pyautogui.locateOnScreen("fraskfire.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Wesker!") 
    try:
        ainzvariant = pyautogui.locateOnScreen("ainzvariant.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Ainzvariant!")
    try:
        aqua = pyautogui.locateOnScreen("aqua.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Aqua!")    
    try:
        fraskwinter = pyautogui.locateOnScreen("fraskwinter.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Fraskwinter!")
    try:
        frasksand = pyautogui.locateOnScreen("frasksand.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Frasksand!")
    try:
        universe = pyautogui.locateOnScreen("universe.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Universe!")
    try:
        perditioboss = pyautogui.locateOnScreen("perditioboss.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Perditioboss!")
    try:
        carnax = pyautogui.locateOnScreen("carnax.png", confidence = 0.9)
        try:
            carnaxRoom1 = pyautogui.locateOnScreen("carnaxRoom1.png", confidence = 0.9)
            pyautogui.click(carnaxRoom1)
            time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print("Not in carnax Room 0.")
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Kongo!")
# Asking the user for task to perform.
roomNumber = random.randint(11111,99999)
task = input("1. Farm HCs\n2. Farm World Boss\n3. Get XP\n4. Generic Attack\n5. Farm Uppercloud\n6. Farm Hermes\n")
if task == "1" :
    # Farming HCs
    try:
        redHeroTaskBarIcon = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/RedHeroTaskBarIcon.png", confidence = 0.8)
        pyautogui.click(redHeroTaskBarIcon)
    except pyautogui.ImageNotFoundException:
        print('Red Hero is not open.')
    pyautogui.write("/join farm-68480")
    pyautogui.hotkey('enter')
    time.sleep(2)
    try:
        farmRoom1 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/FarmRoom1.png", confidence = 0.8)
        pyautogui.click(farmRoom1)
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print('Not in Farm Room 1.')
    try:
        ADVENTURESQuest = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/ADVENTURESQuest.png", confidence = 0.8)
        pyautogui.click(ADVENTURESQuest)
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print("Can't find ADVENTURESQuest")
    try:
        certificateYourself = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/CertificateYourself.png", confidence = 0.8)
        pyautogui.click(certificateYourself)
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print("Can't find Certificate Yourself!")
    try:
        accept = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Accept.png", confidence = 0.8)
        pyautogui.click(accept)
    except pyautogui.ImageNotFoundException:
        print("Can't find Accept!")
    pyautogui.hotkey('l')
    time.sleep(1)
    try:
        farmRoom2 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/FarmRoom2.png")
        pyautogui.click(farmRoom2)
        time.sleep(4)
    except pyautogui.ImageNotFoundException:
        print("Not in Farm Room 2.")
    try:
        farmRoom3 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/FarmRoom3.png")
        pyautogui.click(farmRoom3)
        time.sleep(4)
        pyautogui.click(farmRoom3)
        time.sleep(5)
    except pyautogui.ImageNotFoundException:
        print("Not in Farm Room 3 or 4.")
    questItem = int(0)
    while questItem != 1 :
        try:
            pyautogui.hotkey('l')
            time.sleep(1)
            try:
                certificateYourself = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/CertificateYourself.png", confidence = 0.8)
                pyautogui.click(certificateYourself)
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Can't find Certificate Yourself!")
            scarecrowDefeat = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/ScarecrowDefeat.png", confidence = 0.9)
            treeantDefeat = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/TreeantDefeat.png", confidence = 0.9)
            questItem = int(1)
        except pyautogui.ImageNotFoundException:
            pyautogui.hotkey('l')
            print("Still battling Scarecrows!")
            pyautogui.hotkey('3')
            time.sleep(0.5)
            pyautogui.hotkey('4')
            time.sleep(0.5)
            pyautogui.hotkey('5')
            time.sleep(0.5)
    pyautogui.write("/join umbra-68480")
    pyautogui.hotkey('enter')
    time.sleep(2)
    pyautogui.hotkey('l')
    try:
        umbraRoom1 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/UmbraRoom1.png", confidence = 0.9)
        pyautogui.click(umbraRoom1)
        time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Not in Farm Room 1.")
    try:
        umbraRoom2 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/UmbraRoom2.png", confidence = 0.9)
        pyautogui.click(umbraRoom2)
        time.sleep(4)
        pyautogui.click(umbraRoom2)
        time.sleep(4)
    except pyautogui.ImageNotFoundException:
        print("Not in Farm Room 2.")
    questItem = int(0)
    while questItem != 1 :
        try:
            pyautogui.hotkey('l')
            time.sleep(1)
            try:
                certificateYourself = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/CertificateYourself.png", confidence = 0.8)
                pyautogui.click(certificateYourself)
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Can't find Certificate Yourself!")
            ghoulSoul = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/GhoulSoul.png", confidence = 0.9)
            neophyteSoul = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/NeophyteSoul.png", confidence = 0.9)    
            knightSoul = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/KnightSoul.png", confidence = 0.9)
            questItem = int(1)
        except pyautogui.ImageNotFoundException:
            pyautogui.hotkey('l')
            print("Still battling Umbral Knight!")
            pyautogui.hotkey('3')
            time.sleep(0.5)
            pyautogui.hotkey('4')
            time.sleep(0.5)
            pyautogui.hotkey('5')
            time.sleep(0.5)
    pyautogui.hotkey('l')
    pyautogui.write("/join saloon-68480")
    pyautogui.hotkey('enter')
    time.sleep(2)
    try:
        saloonRoom1 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/SaloonRoom1.png", confidence = 0.9)
        pyautogui.click(saloonRoom1)
        time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Not in Saloon Room 1.")
    try:
        saloonRoom2 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/SaloonRoom2.png", confidence = 0.9)
        pyautogui.click(saloonRoom2)
        time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Not in Saloon Room 2.")
    questItem = int(0)
    while questItem != 1 :
        try:
            pyautogui.hotkey('l')
            time.sleep(1)
            try:
                certificateYourself = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/CertificateYourself.png", confidence = 0.8)
                pyautogui.click(certificateYourself)
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Can't find Certificate Yourself!")  
            bulletless = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Bulletless.png", confidence = 0.9)
            questItem = int(1)
        except pyautogui.ImageNotFoundException:
            pyautogui.hotkey('l')
            print("Still battling BULLETLESS BANDIT!")
            pyautogui.hotkey('3')
            time.sleep(0.5)
            pyautogui.hotkey('4')
            time.sleep(0.5)
            pyautogui.hotkey('5')
            time.sleep(0.5)
    pyautogui.hotkey('l')
    pyautogui.write("/join blackhorn-68480")
    pyautogui.hotkey('enter')
    time.sleep(2)
    try:
        blackhornRoom1 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/BlackhornRoom1.png", confidence = 0.8)
        pyautogui.click(blackhornRoom1)
        time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Not in Blachorn Room 1.")
    questItem = int(0)
    while questItem != 1 :
        try:
            pyautogui.hotkey('l')
            time.sleep(1)
            try:
                certificateYourself = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/CertificateYourself.png", confidence = 0.8)
                pyautogui.click(certificateYourself)
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Can't find Certificate Yourself!")  
            tombSpider = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/TombSpider.png", confidence = 0.9)
            questItem = int(1)
        except pyautogui.ImageNotFoundException:
            pyautogui.hotkey('l')
            print("Still battling TOMB SPIDER!")
            pyautogui.hotkey('3')
            time.sleep(0.5)
            pyautogui.hotkey('4')
            time.sleep(0.5)
            pyautogui.hotkey('5')
            time.sleep(0.5)
    pyautogui.hotkey('l')
    try:
        blackhornRoom2 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/BlackhornRoom2.png", confidence = 0.8)
        pyautogui.click(blackhornRoom2)
        time.sleep(2)
    except pyautogui.ImageNotFoundException:
        print("Not in Blackhorn Room 2.")
    try:
        blackhornRoom3 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/BlackhornRoom3.png", confidence = 0.8)
        pyautogui.click(blackhornRoom3)
        time.sleep(4)
    except pyautogui.ImageNotFoundException:
        print("Not in Blackhorn Room 3.")
    try:
        blackhornRoom4 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/BlackhornRoom4.png", confidence = 0.8)
        pyautogui.click(blackhornRoom4)
        time.sleep(4)
    except pyautogui.ImageNotFoundException:
        print("Not in Blackhorn Room 4.")
    questItem = int(0)
    while questItem != 1 :
        try:
            pyautogui.hotkey('l')
            time.sleep(1)
            try:
                certificateYourself = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/CertificateYourself.png", confidence = 0.8)
                pyautogui.click(certificateYourself)
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Can't find Certificate Yourself!")  
            restlessUndead = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/RestlessUndead.png", confidence = 0.9)
            questItem = int(1)
        except pyautogui.ImageNotFoundException:
            pyautogui.hotkey('l')
            print("Still battling RESTLESS UNDEAD")
            pyautogui.hotkey('3')
            time.sleep(0.5)
            pyautogui.hotkey('4')
            time.sleep(0.5)
            pyautogui.hotkey('5')
            time.sleep(0.5)
    pyautogui.hotkey('l')
# Farming World Boss
if task == "2" :
    try:
        redHeroTaskBarIcon = pyautogui.locateOnScreen("RedHeroTaskBarIcon.png", confidence = 0.8)
        pyautogui.click(redHeroTaskBarIcon)
    except pyautogui.ImageNotFoundException:
        pyautogui.hotkey("alt", "tab")
    programIsRunning = 1
    while programIsRunning == 1 :
        try :
            farmWorldBoss()
# There is no world boss at the moment.
        except pyautogui.ImageNotFoundException:
            print("No World Boss at the moment!")
            for drops in range (6) : 
                try:
                    yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                    pyautogui.click(yes)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("No items left to claim.")
            try:
                try:
                    orc = pyautogui.locateOnScreen("orc.png", confidence = 0.8)
                except pyautogui.ImageNotFoundException:
                    pyautogui.write("/join orc-" + str(roomNumber))
                    pyautogui.hotkey("enter")
                    time.sleep(5)
            except pyautogui.ImageNotFoundException:
                print("Unable to join orc.")
            try:
                orcRoom1 = pyautogui.locateOnScreen("OrcRoom1.png", confidence = 0.8)
                pyautogui.click(orcRoom1)
                time.sleep(4)
            except pyautogui.ImageNotFoundException:
                print("Not in orc Room 0.")
            try:
                orcRoom2 = pyautogui.locateOnScreen("OrcRoom2.png", confidence = 0.9)
                pyautogui.click(orcRoom2)
                time.sleep(4)
            except pyautogui.ImageNotFoundException:
                print("Not in orc Room 1.")
            try:
                orcRoom3 = pyautogui.locateOnScreen("OrcRoom3.png", confidence = 0.9)
                pyautogui.click(orcRoom3)
                time.sleep(2)
            except pyautogui.ImageNotFoundException:
                print("Not in orc Room 2.")
            try:
                orcRoom4 = pyautogui.locateOnScreen("OrcRoom4.png", confidence = 0.9)
                pyautogui.click(orcRoom4)
                time.sleep(4)
            except pyautogui.ImageNotFoundException:
                print("Not in orc Room 3.")
            genericAttack()
if task == "3" : 
    pyautogui.hotkey("alt", "tab")
    try:
        getxp = pyautogui.locateOnScreen("getxp.png", confidence = 0.9)
    except pyautogui.ImageNotFoundException:
        print("Not in getxp.")
        pyautogui.write("/join getxp")
        time.sleep(2)
    programIsRunning = 1
    while programIsRunning == 1 :
        genericAttack()
# Generic Attack 
if task == "4" : 
    pyautogui.hotkey("alt", "tab")
    programIsRunning = 1
    while programIsRunning == 1 :
        genericAttack()
# Farming Uppercloud
if task == "5" :
    try:
        redHeroTaskBarIcon = pyautogui.locateOnScreen("RedHeroTaskBarIcon.png", confidence = 0.8)
        pyautogui.click(redHeroTaskBarIcon)
    except pyautogui.ImageNotFoundException:
        pyautogui.hotkey("alt", "tab")
    programIsRunning = 1
    while programIsRunning == 1 :
        try : 
            farmWorldBoss()
# There is no world boss at the moment.
        except pyautogui.ImageNotFoundException:
            print("No World Boss at the moment!")
            for drops in range (6) : 
                try:
                    yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                    pyautogui.click(yes)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("No items left to claim.")
            try:
                uppercloud = pyautogui.locateOnScreen("uppercloud.png", confidence = 0.9)
            except pyautogui.ImageNotFoundException:
                pyautogui.write("/join uppercloud-68480")
                pyautogui.hotkey("enter")
                time.sleep(5)
            try:
                prismata = pyautogui.locateOnScreen("PRISMATA.png", confidence = 0.8)
                pyautogui.click(prismata)
            except pyautogui.ImageNotFoundException:
                print("Prismata is not selected.")
            genericAttack()
if task == "6" :
    subTask = input("1. Glyph Boat\n2. Glyph Hael\n3. Glyph Tent\n4. Glyph Tree\n5. Glyph Voxel\n6. Symbol Fiend Nation Hermes\n7. Symbol Ice Hermes\n")
    if subTask == "1" : 
        subSubTask = input("1. Kill Pirate\n2. Hangout Pirate Token\n3. Aquamancer Particle\n")
# Kill Pirate
        if subSubTask == "1" : 
            pyautogui.hotkey("alt", "tab")
            programIsRunning = 1
            while (programIsRunning == 1) :
                try : 
                    farmWorldBoss()
                # There is no world boss at the moment.
                except pyautogui.ImageNotFoundException:
                    print("No World Boss at the moment!")
                    for drops in range (6) : 
                        try:
                            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                            pyautogui.click(yes)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("No items left to claim.")
                    try:
                        pirateship = pyautogui.locateOnScreen("pirateship.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.write("/join pirateship-" + str(roomNumber))
                        pyautogui.hotkey("enter")
                        time.sleep(5)
                    try:
                        pirateshipRoom1 = pyautogui.locateOnScreen("pirateshipRoom1.png", confidence = 0.8)
                        pyautogui.click(pirateshipRoom1)
                        time.sleep(3)
                    except pyautogui.ImageNotFoundException:
                        print("pirateshipRoom1 not found.")
                    try:
                        pirateshipRoom2 = pyautogui.locateOnScreen("pirateshipRoom2.png", confidence = 0.8)
                        pyautogui.click(pirateshipRoom2)
                        time.sleep(3)
                    except pyautogui.ImageNotFoundException:
                        print("pirateshipRoom2 not found.")
                    try:
                        pirateshipRoom3 = pyautogui.locateOnScreen("pirateshipRoom3.png", confidence = 0.8)
                        pyautogui.click(pirateshipRoom3)
                        time.sleep(3)
                    except pyautogui.ImageNotFoundException:
                        print("pirateshipRoom3 not found.")
                    genericAttack()
# Hangout Pirate Token
        if subSubTask == "2" : 
            pyautogui.hotkey("alt", "tab")
            programIsRunning = 1
            while (programIsRunning == 1) :
                try : 
                    farmWorldBoss()
                # There is no world boss at the moment.
                except pyautogui.ImageNotFoundException:
                    print("No World Boss at the moment!")
                    for drops in range (6) : 
                        try:
                            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                            pyautogui.click(yes)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("No items left to claim.")
                    try:
                        pirate = pyautogui.locateOnScreen("pirate.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.write("/join pirate-" + str(roomNumber))
                        pyautogui.hotkey("enter")
                        time.sleep(5)
                    try:
                        BERRYBERROY = pyautogui.locateOnScreen("BERRYBERROY.png", confidence = 0.8)
                        pyautogui.click(BERRYBERROY)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Berry Berroy is not found.")   
                    try:
                        REWARDSTalklikeapirate = pyautogui.locateOnScreen("REWARDSTalklikeapirate.png", confidence = 0.8)
                        pyautogui.click(REWARDSTalklikeapirate)
                        time.sleep(5)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find REWARDSTalklikeapirate.")
                    try:
                        misc = pyautogui.locateOnScreen("misc.png", confidence = 0.9)
                        pyautogui.click(misc)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find misc.")
                    try:
                        PirateTicket = pyautogui.locateOnScreen("PirateTicket.png", confidence = 0.8)
                        pyautogui.click(PirateTicket)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Pirate Ticket.")
                    for buyCount in range (10) : 
                        try:
                            Buy = pyautogui.locateOnScreen("Buy.png", confidence = 0.8)
                            pyautogui.click(Buy)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("Cannot find Buy.")
                        try:
                            Yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.7)
                            pyautogui.click(Yes)
                            time.sleep(2)
                        except pyautogui.ImageNotFoundException:
                            print("Cannot find Yes.")
                    for xCount in range (1) : 
                        try:
                            x = pyautogui.locateOnScreen("x.png", confidence = 0.8)
                            pyautogui.click(x)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("Cannot find x.")
                    try:
                        ADVENTUREQuests = pyautogui.locateOnScreen("ADVENTUREQuests.png", confidence = 0.8)
                        pyautogui.click(ADVENTUREQuests)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find ADVENTUREQuests.")      
                    try:
                        GambleOrDie = pyautogui.locateOnScreen("GambleOrDie.png", confidence = 0.8)
                        pyautogui.click(GambleOrDie)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Gamble Or Die.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try:
                        GambleOrDie = pyautogui.locateOnScreen("GambleOrDie.png", confidence = 0.8)
                        pyautogui.click(GambleOrDie)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Gamble Or Die.")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png")
                        pyautogui.click(TurnIn)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Turn In!")
                    try:
                        one = pyautogui.locateOnScreen("1.png", confidence = 0.8)
                        pyautogui.click(one)
                        time.sleep(1)
                        pyautogui.hotkey("0")
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find 1.")
                    try:
                        Yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.7)
                        pyautogui.click(Yes)
                        time.sleep(5)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Yes.")
                    try:
                        Yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.7)
                        pyautogui.click(Yes)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Yes.")
                    try:
                        x = pyautogui.locateOnScreen("x.png", confidence = 0.8)
                        pyautogui.click(x)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find x.")
# Aquamancer Particle
        if subSubTask == "3" : 
            pyautogui.hotkey("alt", "tab")
            programIsRunning = 1
            while (programIsRunning == 1) :
                try : 
                    farmWorldBoss()
                # There is no world boss at the moment.
                except pyautogui.ImageNotFoundException:
                    print("No World Boss at the moment!")
                    for drops in range (6) : 
                        try:
                            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                            pyautogui.click(yes)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("No items left to claim.")
                    try:
                        piratebeach = pyautogui.locateOnScreen("piratebeach.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.write("/join piratebeach-" + str(roomNumber))
                        pyautogui.hotkey("enter")
                        time.sleep(5)
                    try:
                        x = pyautogui.locateOnScreen("x.png", confidence = 0.8)
                        pyautogui.click(x)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find x.")
                    try:
                        npc = pyautogui.locateOnScreen("npc.png", confidence = 0.8)
                        pyautogui.click(npc)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("NPC is not found.")   
                    try:
                        ADVENTUREQuests = pyautogui.locateOnScreen("ADVENTUREQuests.png", confidence = 0.8)
                        pyautogui.click(ADVENTUREQuests)
                        time.sleep(5)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find ADVENTUREQuests.")
                    try:
                        AquamancerDefeat = pyautogui.locateOnScreen("AquamancerDefeat.png", confidence = 0.9)
                        pyautogui.click(AquamancerDefeat)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Aquamancer Defeat.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try:
                        piratebeachRoom1 = pyautogui.locateOnScreen("piratebeachRoom1.png", confidence = 0.8)
                        pyautogui.click(piratebeachRoom1)
                        time.sleep(3)
                    except pyautogui.ImageNotFoundException:
                        print("Not in piratebeachroom0.")
                    try:
                        piratebeachRoom2 = pyautogui.locateOnScreen("piratebeachRoom2.png", confidence = 0.9)
                        pyautogui.click(piratebeachRoom2)
                        time.sleep(5)
                    except pyautogui.ImageNotFoundException:
                        print("Not in piratebeachroom1.")
                    try:
                        piratebeachRoom3 = pyautogui.locateOnScreen("piratebeachRoom3.png", confidence = 0.9)
                        pyautogui.click(piratebeachRoom3)
                        time.sleep(4)
                    except pyautogui.ImageNotFoundException:
                        print("Not in piratebeachroom2.")
                    pyautogui.hotkey("1")
                    try:
                        AquamancerDefeat = pyautogui.locateOnScreen("AquamancerDefeat.png", confidence = 0.9)
                        pyautogui.click(AquamancerDefeat)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Aquamancer Defeat.")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png", confidence = 0.9)
                        pyautogui.click(TurnIn)
                        time.sleep(5)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Turn In.")
                    for drops in range (4) : 
                        try:
                            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                            pyautogui.click(yes)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("No items left to claim.")