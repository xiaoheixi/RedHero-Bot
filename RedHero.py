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
    for drops in range (2) : 
        try:
            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
            pyautogui.click(yes)
            time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("No items left to claim.")
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
        try:
            join = pyautogui.locateOnScreen("Join.png", confidence = 0.8)
            bossStillAlive = 0
        except pyautogui.ImageNotFoundException:
            print("Boss is still alive!")
def farmWorldBoss() : 
    try:
        Respawn = pyautogui.locateOnScreen("Respawn.png", confidence = 0.9)
        pyautogui.click(Respawn)
        time.sleep(1)
    except pyautogui.ImageNotFoundException:
        print("Still alive!")
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
        print("Not Carnax!")
    try:
        ultimate = pyautogui.locateOnScreen("ultimate.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not Ultimate!")
    try:
        emotes = pyautogui.locateOnScreen("emotes.png", confidence = 0.9)
        bossIsStillALive()
    except pyautogui.ImageNotFoundException:
        print("Not emotes!")
# Asking the user for task to perform.
roomNumber = random.randint(11111,99999)
task = input("1. Farm HCs\n2. Farm World Boss\n3. Get XP\n4. Generic Attack\n5. Farm Uppercloud\n6. Farm Hermes\n7. Farm Dwakel\n8. Guild Raids\n")
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
            for drops in range (3) : 
                try:
                    yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                    pyautogui.click(yes)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("No items left to claim.")
# Farming Hermes
if task == "6" :
    subTask = input("1. Glyph Boat\n2. Glyph Hael\n3. Glyph Tent\n4. Glyph Tree\n5. Glyph Voxel\n6. Symbol Fiend Nation Hermes\n7. Symbol Ice Hermes\n")
# Glyph Boat
    if subTask == "1" : 
        subSubTask = input("1. Kill Pirate\n2. Hangout Pirate Token\n3. Aquamancer Particle\n4. Alpha Particle\n5. Key Groggag\n6. Wreck Token\n7. Pirates on the Beach\n8. Kraken Raid\n")
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
# Alpha Particle
        if subSubTask == "4" : 
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
                        piratetown = pyautogui.locateOnScreen("piratetown.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.write("/join piratetown-" + str(roomNumber))
                        pyautogui.hotkey("enter")
                        time.sleep(5)
                    try:
                        Assile = pyautogui.locateOnScreen("Assile.png", confidence = 0.8)
                        pyautogui.click(Assile)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Assile is not found.")   
                    try:
                        Quest = pyautogui.locateOnScreen("Quest.png", confidence = 0.8)
                        pyautogui.click(Quest)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Quest.")
                    try:
                        AlphaPirateDuel = pyautogui.locateOnScreen("AlphaPirateDuel.png", confidence = 0.9)
                        pyautogui.click(AlphaPirateDuel)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Alpha Pirate Duel.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try:
                        piratetownRoom1 = pyautogui.locateOnScreen("piratetownRoom1.png", confidence = 0.9)
                        pyautogui.click(piratetownRoom1)
                        time.sleep(5)
                        pirateTownRoom = 1
                    except pyautogui.ImageNotFoundException:
                        print("Not in piratetownRoom1.")
                    pyautogui.hotkey("1")
                    time.sleep(1)
                    pyautogui.hotkey("2")
                    time.sleep(1)
                    try:
                        AlphaPirateDuel = pyautogui.locateOnScreen("AlphaPirateDuel.png", confidence = 0.9)
                        pyautogui.click(AlphaPirateDuel)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.hotkey("l")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png", confidence = 0.8)
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
# Key Groggag
        if subSubTask == "5" : 
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
                        piratetown = pyautogui.locateOnScreen("piratetown.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.write("/join piratetown-" + str(roomNumber))
                        pyautogui.hotkey("enter")
                        time.sleep(5)
                    try:
                        Assile = pyautogui.locateOnScreen("Assile.png", confidence = 0.8)
                        pyautogui.click(Assile)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Assile is not found.")   
                    try:
                        Quest = pyautogui.locateOnScreen("Quest.png", confidence = 0.8)
                        pyautogui.click(Quest)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Quest.")
                    try:
                        GroggageddonDefeated = pyautogui.locateOnScreen("GroggageddonDefeated.png", confidence = 0.9)
                        pyautogui.click(GroggageddonDefeated)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Groggageddon Defeated.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try:
                        piratetownRoom1 = pyautogui.locateOnScreen("piratetownRoom1.png", confidence = 0.9)
                        pyautogui.click(piratetownRoom1)
                        time.sleep(5)
                        pyautogui.click(piratetownRoom1)
                        time.sleep(5)
                    except pyautogui.ImageNotFoundException:
                        print("Not in piratetownRoom1.")
                    pyautogui.hotkey("1")
                    time.sleep(1)
                    pyautogui.hotkey("2")
                    time.sleep(1)
                    try:
                        GroggageddonDefeated = pyautogui.locateOnScreen("GroggageddonDefeated.png", confidence = 0.9)
                        pyautogui.click(GroggageddonDefeated)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.hotkey("l")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png", confidence = 0.8)
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
# Wreck Token
        if subSubTask == "6" : 
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
                        shipwreck = pyautogui.locateOnScreen("shipwreck.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.write("/join shipwreck-" + str(roomNumber))
                        pyautogui.hotkey("enter")
                        time.sleep(5) 
                    try:
                        Quest2 = pyautogui.locateOnScreen("Quest2.png", confidence = 0.8)
                        pyautogui.click(Quest2)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Quest.")
                    try:
                        WingsFish = pyautogui.locateOnScreen("WingsFish.png", confidence = 0.9)
                        pyautogui.click(WingsFish)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Wings Fish.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try:
                        WreckTokenFreeOption = pyautogui.locateOnScreen("WreckTokenFreeOption.png", confidence = 0.7)
                        pyautogui.click(WreckTokenFreeOption)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Wreck Token (Free Option).")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    genericAttack()
                    try:
                        WingsFish = pyautogui.locateOnScreen("WingsFish.png", confidence = 0.9)
                        pyautogui.click(WingsFish)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Wings Fish.")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png", confidence = 0.8)
                        pyautogui.click(TurnIn)
                        time.sleep(5)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Turn In.")
                        pyautogui.hotkey("l")
                        time.sleep(1)
                        pyautogui.hotkey("l")
                        time.sleep(1)
                    try:
                        WreckTokenFreeOption = pyautogui.locateOnScreen("WreckTokenFreeOption.png", confidence = 0.7)
                        pyautogui.click(WreckTokenFreeOption)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find WreckToken (Free Option).")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png", confidence = 0.8)
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
# Pirates on the Beach
        if subSubTask == "7" : 
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
                        pyautogui.write("/join shipwreck-" + str(roomNumber))
                        pyautogui.hotkey("enter")
                        time.sleep(5) 
                    try:
                        Quest2 = pyautogui.locateOnScreen("Quest2.png", confidence = 0.8)
                        pyautogui.click(Quest2)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Quest.")
                    try:
                        IntheSea = pyautogui.locateOnScreen("IntheSea.png", confidence = 0.9)
                        pyautogui.click(IntheSea)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find In the Sea.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try:
                        piratebeach = pyautogui.locateOnScreen("piratebeach.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException:
                        pyautogui.write("/join piratebeach-" + str(roomNumber))
                        pyautogui.hotkey("enter")
                        time.sleep(5) 
                    try:
                        piratebeachRoom1 = pyautogui.locateOnScreen("piratebeachRoom1.png", confidence = 0.8)
                        pyautogui.click(piratebeachRoom1)
                        time.sleep(3)
                    except pyautogui.ImageNotFoundException:
                        print("Not in piratebeachroom0.")
                    try:
                        piratebeachRoom2 = pyautogui.locateOnScreen("piratebeachRoom2.png", confidence = 0.8)
                        try:
                            pirateCrew = pyautogui.locateOnScreen("PIRATECREW.png", confidence = 0.6)
                            print("In the correct room!")
                        except pyautogui.ImageNotFoundException:
                            pyautogui.click(piratebeachRoom2)
                            time.sleep(4)
                    except pyautogui.ImageNotFoundException:
                        print("Not in piratebeachroom1.")
                    try:
                        piratebeachRoom3 = pyautogui.locateOnScreen("piratebeachRoom3.png", confidence = 0.9)
                        pyautogui.click(piratebeachRoom3)
                        time.sleep(3)
                    except pyautogui.ImageNotFoundException:
                        print("Not in piratebeachRoom2.")    
                    genericAttack()
                    try:
                        IntheSea = pyautogui.locateOnScreen("IntheSea.png", confidence = 0.9)
                        pyautogui.click(IntheSea)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find In the Sea.")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png", confidence = 0.8)
                        pyautogui.click(TurnIn)
                        time.sleep(6)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Turn In.")
                        pyautogui.hotkey("l")
                        time.sleep(1)
                    for drops in range(4) : 
                        try:
                            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                            pyautogui.click(yes)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("No items left to claim.")   
# Kraken Raid
        if subSubTask == "8" : 
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
                        shipwreck1 = pyautogui.locateOnScreen("shipwreck1.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException:
                        try:
                            shipwreck = pyautogui.locateOnScreen("shipwreck.png", confidence = 0.8)
                        except pyautogui.ImageNotFoundException:
                            pyautogui.write("/join shipwreck-" + str(roomNumber))
                            pyautogui.hotkey("enter")
                            time.sleep(5) 
                    try:
                        Quest2 = pyautogui.locateOnScreen("Quest2.png", confidence = 0.8)
                        pyautogui.click(Quest2)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Quest.")
                    try:
                        DefeatTheKraken = pyautogui.locateOnScreen("DefeatTheKraken.png", confidence = 0.9)
                        pyautogui.click(DefeatTheKraken)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Defeat The Kraken.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try:
                        shipwreckRoom1 = pyautogui.locateOnScreen("shipwreckRoom1.png", confidence = 0.8)
                        pyautogui.click(shipwreckRoom1)
                        time.sleep(4)
                        pyautogui.click(shipwreckRoom1)
                        time.sleep(4)
                    except pyautogui.ImageNotFoundException:
                        print("Not in shipwreckRoom1.")   
                    genericAttack()
                    try:
                        DefeatTheKrakenComplete = pyautogui.locateOnScreen("DefeatTheKrakenComplete.png", confidence = 0.9)
                        pyautogui.click(DefeatTheKrakenComplete)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Defeat The Kraken is not complete.")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png", confidence = 0.8)
                        pyautogui.click(TurnIn)
                        time.sleep(6)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Turn In.")
                        pyautogui.hotkey("l")
                        time.sleep(1)
                    for drops in range(4) : 
                        try:
                            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                            pyautogui.click(yes)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("No items left to claim.")
# Glyph Hael
    if subTask == "2" : 
        subSubTask = input("1. Guest Eros\n2. Forest Soul Priest\n")
# Guest Eros
        if subSubTask == "1":
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
                        try:
                            piratebeach = pyautogui.locateOnScreen("piratebeach.png", confidence = 0.8)
                        except pyautogui.ImageNotFoundException:
                            pyautogui.write("/join piratebeach-" + str(roomNumber))
                            pyautogui.hotkey("enter")
                            time.sleep(5) 
                    try:
                        npc = pyautogui.locateOnScreen("npc.png", confidence = 0.8)
                        pyautogui.click(npc)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Deep.")
                    try:
                        ADVENTUREQuests = pyautogui.locateOnScreen("ADVENTUREQuests.png", confidence = 0.8)
                        pyautogui.click(ADVENTUREQuests)
                        time.sleep(2)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find ADVENTURE Quests.")
                    try:
                        UndeadPiratesDestroy = pyautogui.locateOnScreen("UndeadPiratesDestroy.png", confidence = 0.8)
                        pyautogui.click(UndeadPiratesDestroy)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Undead Pirates Destroy.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                        pyautogui.hotkey("l")
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try :
                        piratebeach = pyautogui.locateOnScreen("piratebeach.png", confidence = 0.8)
                        pyautogui.write("/join pirateship-" + str(roomNumber))
                        pyautogui.hotkey("Enter")
                        time.sleep(5)
                    except pyautogui.ImageNotFoundException:
                        print("Already in the correct room.")
                    try:
                        pirateshipRoom1 = pyautogui.locateOnScreen("pirateshipRoom1.png", confidence = 0.8)
                        pyautogui.click(pirateshipRoom1)
                        time.sleep(4)
                    except pyautogui.ImageNotFoundException:
                        print("Not in pirateshipRoom0.")
                    try:
                        pirateshipRoom2 = pyautogui.locateOnScreen("pirateshipRoom2.png", confidence = 0.8)
                        pyautogui.click(pirateshipRoom2)
                        time.sleep(4)
                    except pyautogui.ImageNotFoundException:
                        print("Not in pirateshipRoom1.") 
                    try:
                        pirateshipRoom3 = pyautogui.locateOnScreen("pirateshipRoom3.png", confidence = 0.8)
                        pyautogui.click(pirateshipRoom3)
                        time.sleep(4)
                    except pyautogui.ImageNotFoundException:
                        print("Not in pirateshipRoom2.") 
                    genericAttack()
                    try:
                        pyautogui.hotkey("l")
                        UndeadPiratesDestroyComplete = pyautogui.locateOnScreen("UndeadPiratesDestroyComplete.png", confidence = 0.6)
                        pyautogui.click(UndeadPiratesDestroyComplete)
                        time.sleep(2)
                    except pyautogui.ImageNotFoundException:
                        print("Undead Pirates Destroy not complete.")
                    try:
                        TurnIn = pyautogui.locateOnScreen("TurnIn.png", confidence = 0.9)
                        pyautogui.click(TurnIn)
                        time.sleep(6)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Turn In.")
                        pyautogui.hotkey("l")
                        time.sleep(1)
                    for drops in range(4) : 
                        try:
                            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                            pyautogui.click(yes)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("No items left to claim.")
# Forest Soul Priest
        if subSubTask == "2":
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
                        forest = pyautogui.locateOnScreen("forest.png", confidence = 0.8)
                    except pyautogui.ImageNotFoundException: 
                        pyautogui.write("/join forest-" + str(roomNumber))
                        pyautogui.hotkey("Enter")
                        time.sleep(5)
                    try:
                        RapHael = pyautogui.locateOnScreen("RapHael.png", confidence = 0.8)
                        pyautogui.click(RapHael)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("No items left to claim.")
                    try:
                        ADVENTUREQuests1 = pyautogui.locateOnScreen("ADVENTUREQuests1.png", confidence = 0.8)
                        pyautogui.click(ADVENTUREQuests1)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find ADVENTURE Quests.")
                    try:
                        FarmForestToken = pyautogui.locateOnScreen("FarmForestToken.png", confidence = 0.8)
                        pyautogui.click(FarmForestToken)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Farm Forest Token.")
                    try:
                        accept = pyautogui.locateOnScreen("Accept.png", confidence = 0.8)
                        pyautogui.click(accept)
                        time.sleep(1)
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find Accept.")
                    try:
                        FarmForestTokenComplete = pyautogui.locateOnScreen("FarmForestTokenComplete.png", confidence = 0.8)
                        pyautogui.click(FarmForestTokenComplete)
                        time.sleep(1)
                        try:
                            TurnIn = pyautogui.locateOnScreen("TurnIn.png")
                            pyautogui.click(TurnIn)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("Cannot find Turn In.")
                    except pyautogui.ImageNotFoundException:
                        print("Farm Forest Token is not complete yet.")
                    try:
                        forestRoom1 = pyautogui.locateOnScreen("forestRoom1.png", confidence = 0.8)
                        pyautogui.click(forestRoom1)
                        time.sleep(5)
                        for genericAttackCount in range (4) :
                            genericAttack()
                        pyautogui.click(forestRoom1)
                        time.sleep(5)
                        for genericAttackCount in range (3) :
                            genericAttack()
                        pyautogui.click(forestRoom1)
                        time.sleep(5)
                        pyautogui.hotkey("1")
                        pyautogui.write("/join lostisland-" + str(roomNumber))
                        pyautogui.hotkey("Enter")
                        time.sleep(5)
                        try:
                            lostIslandRoom1 = pyautogui.locateOnScreen("lostIslandRoom1.png", confidence = 0.8)
                            pyautogui.click(lostIslandRoom1)
                            time.sleep(4)
                        except pyautogui.ImageNotFoundException:
                            print("Cannot find lostIslandRoom1.")
                        for genericAttackCount in range (3) :
                            genericAttack()
                    except pyautogui.ImageNotFoundException:
                        print("Cannot find forestRoom1.")
                    for drops in range(4) : 
                        try:
                            yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                            pyautogui.click(yes)
                            time.sleep(1)
                        except pyautogui.ImageNotFoundException:
                            print("No items left to claim.")
# Farming Dwakel
if task == "7" :
    try:
        redHeroTaskBarIcon = pyautogui.locateOnScreen("RedHeroTaskBarIcon.png", confidence = 0.8)
        pyautogui.click(redHeroTaskBarIcon)
    except pyautogui.ImageNotFoundException:
        pyautogui.hotkey("alt", "tab")
    programIsRunning = 1
    while programIsRunning == 1 :
        try : 
            farmWorldBoss()
        except :
            print("No World Boss at the moment!")
            for drops in range (6) : 
                try:
                    yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                    pyautogui.click(yes)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("No items left to claim.")
            try:
                dwakel = pyautogui.locateOnScreen("dwakel.png", confidence = 0.8)
            except pyautogui.ImageNotFoundException:
                pyautogui.write("/join dwakel-" + str(roomNumber))
                pyautogui.hotkey("enter")
                time.sleep(5)
            try:
                dwakelRoom1 = pyautogui.locateOnScreen("dwakelRoom1.png", confidence = 0.9)
                pyautogui.click(dwakelRoom1)
                time.sleep(2)
            except pyautogui.ImageNotFoundException:
                print("Not in Dwakel Room 0.")
            try:
                hideChatPane = pyautogui.locateOnScreen("hideChatPane.png", confidence = 0.9)
                pyautogui.click(hideChatPane)
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Cannot hide the chat pane.")
            try:
                dwakelRoom2 = pyautogui.locateOnScreen("dwakelRoom2.png", confidence = 0.9)
                pyautogui.click(dwakelRoom2)
                time.sleep(4)
            except pyautogui.ImageNotFoundException:
                print("Not in Dwakel Room 1.")
            try:
                dwakelRoom3 = pyautogui.locateOnScreen("dwakelRoom3.png", confidence = 0.9)
                pyautogui.click(dwakelRoom3)
                time.sleep(4)
            except pyautogui.ImageNotFoundException:
                print("Not in Dwakel Room 2.")
            genericAttack()
            try:
                dwakelRoom4 = pyautogui.locateOnScreen("dwakelRoom4.png", confidence = 0.9)
                pyautogui.click(dwakelRoom4)
                time.sleep(1)
            except pyautogui.ImageNotFoundException:
                print("Not in Dwakel Room 3.")
            genericAttack()
            for drops in range (6) : 
                try:
                    yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                    pyautogui.click(yes)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("No items left to claim.")
# Guild Raids
if task == "8" :
    subTask = input("1. Galdon\n2. Sunken\n3. Ginkotsu\n4. Kawte\n5. Syvoid\n6. Cold\n")
    if subTask == "1" : 
        pyautogui.hotkey("alt", "tab")
        pyautogui.write("/join galdon")
        pyautogui.press("Enter")
        time.sleep(5)
        try:
            galdonRoom1 = pyautogui.locateOnScreen("galdonRoom1.png", confidence = 0.8)
            pyautogui.click(galdonRoom1)
            time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom0.")
        genericAttack()
        try:
            galdonRoom2 = pyautogui.locateOnScreen("galdonRoom2.png", confidence = 0.8)
            pyautogui.click(galdonRoom2)
            time.sleep(1)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom1.")
        try:
            galdonRoom2Click1 = pyautogui.locateOnScreen("galdonRoom2Click1.png", confidence = 0.8)
            pyautogui.click(galdonRoom2Click1)
            time.sleep(3)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom1.")
        try:
            galdonRoom2Click2 = pyautogui.locateOnScreen("galdonRoom2Click2.png", confidence = 0.9)
            pyautogui.click(galdonRoom2Click2)
            time.sleep(3)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom1.")
        genericAttack()
        try:
            galdonRoom3 = pyautogui.locateOnScreen("galdonRoom3.png", confidence = 0.9)
            pyautogui.click(galdonRoom3)
            time.sleep(4)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom2.")
        try:
            galdonRoom3Click1 = pyautogui.locateOnScreen("galdonRoom3Click1.png", confidence = 0.8)
            pyautogui.click(galdonRoom3Click1)
            time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom2.")
        genericAttack()
        for drops in range (2) : 
                try:
                    yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                    pyautogui.click(yes)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("No items left to claim.")
        try:
            galdonRoom4 = pyautogui.locateOnScreen("galdonRoom4.png", confidence = 0.9)
            pyautogui.click(galdonRoom4)
            time.sleep(4)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom3.")
        try:
            galdonRoom4Click1 = pyautogui.locateOnScreen("galdonRoom4Click1.png", confidence = 0.8)
            pyautogui.click(galdonRoom4Click1)
            time.sleep(4)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom3.")
        genericAttack()
        try:
            galdonRoom5 = pyautogui.locateOnScreen("galdonRoom5.png", confidence = 0.8)
            pyautogui.click(galdonRoom5)
            time.sleep(4)
            genericAttack()
            pyautogui.click(galdonRoom5)
            time.sleep(4)
            genericAttack()
            pyautogui.click(galdonRoom5)
            time.sleep(4)
            genericAttack()
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom4.")
        for drops in range (3) : 
                try:
                    yes = pyautogui.locateOnScreen("Yes.png", confidence = 0.8)
                    pyautogui.click(yes)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("No items left to claim.")
        try:
            galdonRoom6 = pyautogui.locateOnScreen("galdonRoom6.png", confidence = 0.8)
            pyautogui.click(galdonRoom6)
            time.sleep(2)
        except pyautogui.ImageNotFoundException:
            print("Not in galdonRoom5.")
        for genericAttackDuration in range(15) :
            genericAttack()
        