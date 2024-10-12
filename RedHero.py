# Importing required libraries.
import pyautogui
import time
# Generic Attack function
def genericAttack() : 
    for attackDuration in range (2) :
        pyautogui.hotkey("1")
        time.sleep(0.3)
        pyautogui.hotkey("2")
        time.sleep(0.3)
        pyautogui.hotkey("3")
        time.sleep(0.3)
        pyautogui.hotkey("4")
        time.sleep(0.3)
        pyautogui.hotkey("5")
# Asking the user for task to perform.
task = input("1. Farm HCs\n2. Farm World Boss\n")
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
        redHeroTaskBarIcon = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/RedHeroTaskBarIcon.png", confidence = 0.8)
        pyautogui.click(redHeroTaskBarIcon)
    except pyautogui.ImageNotFoundException:
        print('Red Hero is not open.')
    programIsRunning = 1
    while programIsRunning == 1 :
        try :
            join = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Join.png", confidence = 0.8)
            pyautogui.click(join)
            time.sleep(2)
            try:
                drakath = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/drakath.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
            except pyautogui.ImageNotFoundException:
                print("Not Drakath!")
            # try:
            #     firstspeaker = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/firstspeaker.png")
            #     for seconds in range (1) :
            #         genericAttack()
            # except pyautogui.ImageNotFoundException:
            #     print("Not Firstspeaker!")    
            try:
                red = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/red.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Red")
            try:
                paragonboss = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/paragonboss.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")        
            except pyautogui.ImageNotFoundException:
                print("Not Paragon Boss!")    
            try:
                kuroshi = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/kuroshi.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Kuroshi!")  
            try:
                daemon = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/daemon.png", confidence = 0.9)
                try:
                    daemonRoom1 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/daemonRoom1.png", confidence = 0.9)
                    pyautogui.click(daemonRoom1)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("Not in Daemon Room 0.")
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Daemon!")
            try:
                wesker = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/wesker.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Wesker!")    
            try:
                kongo = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/kongo.png", confidence = 0.9)
                try:
                    kongoRoom1 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/kongoRoom1.png", confidence = 0.9)
                    pyautogui.click(kongoRoom1)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("Not in kongo Room 0.")
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Kongo!")  
            try:
                deathrealm = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/deathrealm.png", confidence = 0.9)
                try:
                    deathrealmRoom1Click1 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/deathrealmRoom1Click1.png", confidence = 0.9)
                    pyautogui.click(deathrealmRoom1Click1)
                    time.sleep(4)
                except pyautogui.ImageNotFoundException:
                    print("Not in deathrealm Room 0.")
                try:
                    deathrealmRoom1Click2 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/deathrealmRoom1Click2.png", confidence = 0.9)
                    pyautogui.click(deathrealmRoom1Click2)
                    time.sleep(2)
                except pyautogui.ImageNotFoundException:
                    print("Not in deathrealm Room 0.")
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Kongo!")
            try:
                fraskfire = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/fraskfire.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Wesker!") 
            try:
                ainzvariant = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/ainzvariant.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Ainzvariant!")
            try:
                aqua = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/aqua.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Aqua!")    
            try:
                fraskwinter = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/fraskwinter.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Fraskwinter!")
            try:
                frasksand = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/frasksand.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Frasksand!")
            try:
                universe = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/universe.png", confidence = 0.9)
                bossStillAlive = 1
                while bossStillAlive == 1 :
                    genericAttack()
                    try:
                        yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.9)
                        pyautogui.click(yes)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")
                    try:
                        town = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/town.png", confidence = 0.9)
                        bossStillAlive = 0
                    except pyautogui.ImageNotFoundException:
                        print("Boss is still alive!")    
            except pyautogui.ImageNotFoundException:
                print("Not Universe!")
# There is no world boss at the moment.
        except pyautogui.ImageNotFoundException:
            print("No World Boss at the moment!")
            for drops in range (6) : 
                try:
                    yes = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/Yes.png", confidence = 0.8)
                    pyautogui.click(yes)
                    time.sleep(1)
                except pyautogui.ImageNotFoundException:
                    print("No items left to claim.")
            try:
                try:
                    orc = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/orc.png")
                except pyautogui.ImageNotFoundException:
                    pyautogui.write("/join orc-68480")
                    pyautogui.hotkey("enter")
                    time.sleep(5)
            except pyautogui.ImageNotFoundException:
                print("Unable to join orc.")
            try:
                orcRoom1 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/OrcRoom1.png", confidence = 0.8)
                pyautogui.click(orcRoom1)
                time.sleep(4)
            except pyautogui.ImageNotFoundException:
                print("Not in orc Room 0.")
            try:
                orcRoom2 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/OrcRoom2.png", confidence = 0.9)
                pyautogui.click(orcRoom2)
                time.sleep(4)
            except pyautogui.ImageNotFoundException:
                print("Not in orc Room 1.")
            try:
                orcRoom3 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/OrcRoom3.png", confidence = 0.9)
                pyautogui.click(orcRoom3)
                time.sleep(2)
            except pyautogui.ImageNotFoundException:
                print("Not in orc Room 2.")
            try:
                orcRoom4 = pyautogui.locateOnScreen("C:/Users/justi/OneDrive/Documents/RedHero/RedHero-Bot/OrcRoom4.png")
                pyautogui.click(orcRoom4)
                time.sleep(4)
            except pyautogui.ImageNotFoundException:
                print("Not in orc Room 3.")
            genericAttack()