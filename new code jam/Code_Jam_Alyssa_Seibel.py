import keyboard
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import random
import time
from PIL import Image
os.system("cls")



#title screen
print("--__--__(Doctor's Creation)__--__--")
time.sleep(1) #pauses for 3 seconds
print("Press 'Enter' to start...")

keyboard.wait('enter')
#starting the game now

def startscreen():
    print("\n\n\nIn this game you play as Rick...")
    time.sleep(1)

    print("\nYour wife is Sarah...")
    time.sleep(.5)

    print("\nFrom now on, press enter to go to the next diologue.")
    keyboard.wait('enter')
    os.system('cls')

# Begin the code
startscreen()


# Open and display the image
img_path = './image originals/road.webp'
img = mpimg.imread(img_path)

# create figure
plt.figure(figsize=(10, 6))

# display img
plt.imshow(img)

# hide the axes
plt.axis('off')

# show img
plt.show()


def OnTheWay():
    print('You\'re driving your wife to a hospital that her current doctor assigned you to. Her doctor is out of office for a few days. but you guys wanted to induce the labor.')
    keyboard.wait('enter')

    print('\nAfter some time passes and winding through lots of dark and creepy roads, you arrive at a run-down looking "hospital"')
    keyboard.wait('enter')

    img_path = './image originals/hos_outside.webp'
    img = mpimg.imread(img_path)
    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.axis('off')
    plt.show()

    print('\nThe silence of the abandoned-looking building was eerie')
    keyboard.wait('enter')
    os.system('cls')

    print('Chills crawl up your spine as you imagine your pregnant wife and your new child entering this frightening building.')
    keyboard.wait('enter')

    print(f"\nWhat should you do?:\n  Convince your wife to go home(Press '1')\n  Ask how she\'s doing(Press '2')")
    
    
    while True:
        if keyboard.is_pressed('1'):
            OnTheWay1()
            break
        if keyboard.is_pressed('2'):
            OnTheWay2()
            break

def OnTheWay1():
    print('\n\n  Rick:\n"Are you sure this is where Dr. Seel directed us to?", you say with some sort of suspicion.')
    keyboard.wait('enter')

    print('\n  Sarah:\nYes, I\'m sure.')
    keyboard.wait('enter')

    print('\n  Rick:\n"Maybe we should go home and wait for Dr. Seel to operate on you himself", you say with a convincing tone. Theres no way you were letting your frail wife in this eerie building in the middle of no where')
    keyboard.wait('enter')

    print('\n  Sarah:\n"Rick it\'s fine", she irked. She seemed slightly on edge. Maybe it\'s from the uncomfort from our unborn child, pushing uncomfortably against her spine.')
    keyboard.wait('enter')
    os.system('cls')

def OnTheWay2():
    print('\n  Rick:\n"How are you feeling?"')
    keyboard.wait('enter')

    print('\nYou could hear Sarah\'s breath pick up speed. You look over to see her blank face. You couldn\'t tell if she was scared or spaced out.')
    keyboard.wait('enter')
    os.system('cls')

#start OTW sequence
OnTheWay()

# doctor appearence
print('\n---SLAM---')
keyboard.wait('enter')

print('\nA dark figure struck the passenger window causing both of you to gasp for air.')
keyboard.wait('enter')

print('\nIn the dim lighting, you can make out a figure of a man in a lab coat. You roll down the window just enough to hear what he has to say.')
keyboard.wait('enter')
os.system('cls')
    
print('\n  ???:\nHello, you must be the Lauers, right?')
keyboard.wait('enter')
print('\nIn the dim lighting, you can make out slight features of this man.')
keyboard.wait('enter')
os.system('cls')

print('\n  Rick:\n"Uh..Yes... we are..." You were hesitent to give away your information, but you WERE sent here.')
keyboard.wait('enter')

print('\n  ???:\nI\'m Dr. Evans. Dr. Seel sent you to see me", he stated in a soothing voice. He seems trusting, but you don\'t immediately buy his act.')
keyboard.wait('enter')
os.system('cls')

print('\nThe passenger door swings open which catches you by suprise. As a natural response, you grab your wife by her arm.')
keyboard.wait('enter')

print('\n  Dr. Evans:\n"Now, now Mr. Lauers", the unsettling doctor verbalized in a cunning voice. "We will take good care of your wife."')
keyboard.wait('enter')
os.system('cls')

print('\nA nurse appears from behind the doctor, grabbing Sarah\'s arm in a soft but agressive way. There was something off about her. Not only was she wearing a disturbingly skimpy outfit for a professional, but she looked... sickly.')
keyboard.wait('enter')
os.system('cls')

print('Sarah hesitates slightly before submitting to the nurse. The nurse helps her out of the car and lead her towards the abandoned building')
keyboard.wait('enter')

print('\n  Dr. Evans:\n"Now Mr. Lauers, I\'ll take you in through the guest entrance. It\'s towards the front parking lot"')

def follow():
    print("\nWhat do you do?:\n  Follow the strange doctor?(Press '1')\n  Stay in the car.(Press '2')")

    while True:
        if keyboard.is_pressed('1'):
            os.system('cls')
            follow1()
            break
        if keyboard.is_pressed('2'):
            os.system('cls')
            follow2()
            break

def follow1():
    # keep for long messages
    message1= ['You open the door and step out of your car.',
               'You stumble a little from the hours of driving.'
                ' While keeping atleast a 6-foot distance, you follow along the doctor in an alert way.',
                'As you scan your surroundings you notice the lack of lights. You think "Where are we? Why is there a hospital in the middle of no where..."',
                'The suspicion rises as you follow towards the front parking lot.']
    for mess in message1:
        print(mess)
        time.sleep(1)
    keyboard.wait('enter')

    img_path = './image originals/parking_lot.webp'
    img = mpimg.imread(img_path)

    # create figure
    plt.figure(figsize=(10, 6))

    # display img
    plt.imshow(img)

    # hide the axes
    plt.axis('off')

    # show img
    plt.show()

    os.system('cls')

def follow2():
    print('The doctor takes a step back, waiting for you to come out of the car. You hesitate, not trusting this man who looked like he hasn\'t slept in a decade.')
    keyboard.wait('enter')
    print('\n  Dr. Evans:\n"If you would prefer to wait in the car, you may."')
    keyboard.wait('enter')
    os.system('cls')
    
    # keep for long message
    message2= ['\nThe doctor slowly creeps away.',
            'Although you almost took that option, you remembered that you would be leaving Sarah alone in that horrifying building.',
            'You jolted out of the car and followed behind the doctor. The lack of light creeped you out.',
            'You wondered why a hospital would be out in the middle of no where.',
            'You and the doctor slowly arrive towards the front parking lot.']
    for mess in message2:
        print(mess)
        time.sleep(1)
    keyboard.wait('enter')
    img_path = './image originals/parking_lot.webp'
    img = mpimg.imread(img_path)

    # create figure
    plt.figure(figsize=(10, 6))

    # display img
    plt.imshow(img)

    # hide the axes
    plt.axis('off')

    # show img
    plt.show()
    os.system('cls')

# start follow sequence
follow()

def investigate():
    print('You hear the faint calls of wild animals in the distance, and see the flickering of the old street lights in the parking lot.')
    keyboard.wait('enter')

    print('\n\n---FLICK---')
    keyboard.wait('enter')

    print('\n\nThis makes the front parking lot look ominous.')
    keyboard.wait('enter')

    print('\nYou pass through the side of the hospital which is strangely surrounded in metal fences.')
    keyboard.wait('enter')

    print('\n\n---FLICK---')
    keyboard.wait('enter')

    print('\n\nAs you\'re scanning the surroundings a slight movement catches your attention.')
    keyboard.wait('enter')

    print('\n\n---FLICK---\n')
    keyboard.wait('enter')
    
    print("\nWhat will you do?:\n  Point out the movement to the doctor.(Press '1')\n  Ignore it and keep walking.(Press '2')")

    while True:
        if keyboard.is_pressed('1'):
            os.system('cls')
            investigate1()
            break
        if keyboard.is_pressed('2'):
            os.system('cls')
            investigate2()
            break

def investigate1():
    print(f'You stop in your tracks abruptly.')
    keyboard.wait('enter')

    print('\n\n---FLICK---')
    keyboard.wait('enter')
    
    print('\n\n  Rick:\n"Hey, do you see that?" The doctor stops in his tracks and looks in the same direction as you.')
    keyboard.wait('enter')
    
    print('\n\n---FLICK---')
    keyboard.wait('enter')
    
    print('\n\nYou focus closer, developing the scene between each light flicker. You spot what looks like one of the nurses off in the distace.')
    keyboard.wait('enter')
    os.system('cls')

    print(f'After examining it for a while you notice that she is lugging a heavy object that is trailing liquid. Maybe it\'s trash.')
    keyboard.wait('enter')
    
    print('\n\n---FLICK---')
    keyboard.wait('enter')

    print(f'\n\n---FLICK---')
    keyboard.wait('enter')
    
    print('\n\nAs you inspect the object, you notice hair like lumps sliding off of it.')
    keyboard.wait('enter')
    
    print('\n\n---FLICK---')
    keyboard.wait('enter')
    
    print('\n\nIs that...')
    keyboard.wait('enter')

    print('a body?')
    keyboard.wait('enter')

    print(f'In a split second you freeze.')
    keyboard.wait('enter')

    print('\n\n---FLICK---')
    keyboard.wait('enter')

    print('\n\nYou notice the thick dark liquid which you now realize is...')
    keyboard.wait('enter')

    print('\n\n---FLICK---')
    keyboard.wait('enter')

    print('\n\n...blood.')
    keyboard.wait('enter')

    print('\nRUN, you think-')
    time.sleep(.5)
    os.system('cls')
    print('\n--WHAM--')

def investigate2():
    print("You think nothing of it and keep walking behind Dr. Evans.")
    keyboard.wait('enter')

    print('\n  Rick:\n"So...where is that nurse taking my wife?", you press the doctor calmly hoping for a direct answer.')
    keyboard.wait('enter')

    print('\n  Dr. Evans:\n"The nurse will check her into a room. There\'s no need to worry. You will see her soon."')
    keyboard.wait('enter')

    print('\nDr. Evans was quick to cut the convo.')
    keyboard.wait('enter')
    os.system('cls')

    message3 = ['\nYou arrive at what seems to be the front entrance',
    'You notice the overgrown vines surrounding the door.',
    'How old is this place?']

    for mess in message3:
        print(mess)
        time.sleep(.75)
    keyboard.wait('enter')

    print('\n  Dr. Evans:\n"I\'ll check you into a private waiting room.", he states while holding open the creaky door. He pauses and continues, "Some of the guests out here can be kind of... roudy"')
    keyboard.wait('enter')

    print('\nYou think nothing of that comment and continue through the door.')
    keyboard.wait('enter')
    os.system('cls')

    print('\nDr. Evans approaches the from desk while you wait a few feet away. As you wait, you observe the public waiting room.')
    keyboard.wait('enter')

    message4 = ['\nThere were a few guests sitting down. They seemed...off',
    'Almost like they weren\'t really there...',
    'The woman in the corner was staring at the same flier on the wall.',
    'What could be so interesting?',
    'A man was at the vending machine. It seemed normal until you observed closer.',
    'He was pressing the buttons without putting any money in. Doesn\'t he know how vending machines work?']

    for mess in message4:
        print(mess)
        time.sleep(1)
    keyboard.wait('enter')
    os.system('cls')

    print('\nAll of these guests seemed strange. Maybe it\'s from the musty air. I guess it\'s a good thing that you are getting a private waiting room.')
    keyboard.wait('enter')

    print('\nAfter what seemed like a while, Dr. Evans directs you to the room. He is keeping a 2-foot distance behind you.')
    keyboard.wait('enter')

    message5 = ["\nYou look around at the nerve racking hallways.",
    "They all look the same. How could you not get lost in this building.",
    "Not to mention, the lighting was terrible. Half of the lights were out and the rest had a yellow tint.",
    "How could a hospital not have good lighting?"]

    for mess in message5:
        print(mess)
        time.sleep(1)

    keyboard.wait('enter')
    os.system('cls')

    print("You come up to this small room towards the side of the hospital")
    keyboard.wait('enter')

    print('\n  Dr. Evans:\n"Right here, Mr. Lauers."')
    keyboard.wait('enter')

    print("\nYou hesitate before opening the door.")
    keyboard.wait('enter')

    print('\nThe room had an examination chair with a large light peering overtop of it. It seemed like the only light that really worked in this hospital. There were jars of stuff like q-tips and bandaids.')
    keyboard.wait('enter')

    print('\nIt looked like any normal hospital room, but for some reason a strange suspicion crept up your spine.')
    keyboard.wait('enter')

    print('\nYou slowly pace inside, still observing the rest of the room. The shades were open and you could see the side of the building that you came from.')
    keyboard.wait('enter')

    print('\nMovement caught your attention in the same spot you saw beforehand.')
    keyboard.wait('enter')

    print('\nIs that a nurse?')
    keyboard.wait('enter')

    print('\nLugging a body?-')
    time.sleep(1)
    os.system('cls')
    print("---WHAM---")
    keyboard.wait('enter')

investigate()

#wake up in room
print("After what seems like hours, you wake up.")
keyboard.wait('enter')

print('\n  Rick:\n"What happened?", you groan out while rubbing your head.')
keyboard.wait('enter')

print("\nThe room was filled with the yellow tinted lights which made it hard to see.")
keyboard.wait('enter')

img_path = './image originals/office.jpg'
img = mpimg.imread(img_path)

# create figure
plt.figure(figsize=(10, 6))

# display img
plt.imshow(img)

# hide the axes
plt.axis('off')

# show img
plt.show()

os.system('cls')


# initial states
door_locked = True
has_key = False
flashlight = False
clutter = False
# items in left
has_bat = False
investleftdoor2 = False

has_leftdoor1_key = False
investleftdoor1 = False

invest_rightlefthall = False
invest_rightrighthall = False
aftermirror = False

#end credit
def end():
    os.system('cls')
    print("--__--__(Doctor's Creation)__--__--")
    time.sleep(1) #pauses for 3 seconds
    print("Thank you for playing")
    keyboard.wait('enter')
    exit()
    
#ending 1
def end1():
    os.system('cls')
    print("Did I just kill my wife?")
    keyboard.wait('enter')
    end()

#ending 2
def death():
    os.system('cls')
    print("This is your wife...You can\'t kill her...")
    keyboard.wait('enter')

    print("\nThe monster roars as it launches at you.")
    keyboard.wait('enter')

    print("\nWhat more can you do but just stand there and let fate take it\n's course.")
    keyboard.wait('enter')

    print("\nThe only thing left in your life was your wife and your child, and both of them are gone. What is left for you...")
    keyboard.wait('enter')
    end()

#if you die try again
def tryagain():
    os.system('cls')

    print("\nDo you want to try again?\n  Yes (Press '1')\n  No (Press '2')")
    while True:
        event = keyboard.read_event()
        if event.event_type == 'down':
            if event.name == '1':
                battle()
            elif event.name == '2':
                print("\nBy clicking no, you will not complete the game and will have to restart from the beginning. Are you sure you want to end the game?\n  Yes (Press '1')\n  No (Press '2')")
                while True:
                    event = keyboard.read_event()
                    if event.event_type == 'down':
                        if event.name == '1':
                            exit()
                        elif event.name == '2':
                            tryagain()
#Battle coding-----

class fighter:
    name = ""
    hp = 0
    attack = 0
    defense = 0
    medication = 0


rick = fighter()
rick.name = "Rick"
rick.hp = 100
rick.attack = 20
rick.defense = 15
rick.medication = 2

sarah = fighter()
sarah.name = "SARAH???"
sarah.hp = 200
sarah.attack = 30
sarah.defense = 0
sarah.medication = 0

# WHile the hero and enemy are alive
def battle():
    while (rick.hp > 0 and sarah.hp >0):

        temporary_defense = 0

        print(f'\n\n{rick.name} has {rick.hp} HP and {sarah.name} has {sarah.hp} HP.')
        print("\nWhat would you like to do?\n  Attack (Press '1')\n  Defend (Press '2')\n  Heal (Press '3')")
        while True:
            event = keyboard.read_event()
            if event.event_type == 'down':
                if event.name == '1':
                    sarah.hp -= rick.attack - sarah.defense
                    print(f'\n{rick.name} wacked {sarah.name} with a bat for {str(rick.attack - sarah.defense)} damage')
                    keyboard.wait('enter')
                    break
                elif event.name == '2':
                    temporary_defense = 10
                    print(f'\n{rick.name} dodged slightly out of the way.')
                    keyboard.wait('enter')
                    break

                elif event.name == '3':
                    if (rick.medication > 0):
                        rick.hp += 50
                        rick.medication -= 1
                        print(f'\n{rick.name} used medication to heal his wounds for 50 hp. You have {str(rick.medication)} left')
                        keyboard.wait('enter')
                        break
                    else:
                        print(f'\n{rick.name} is out of potions')
                        keyboard.wait('enter')

        rick.hp -= sarah.attack - (rick.defense + temporary_defense)
        print(f"\n{sarah.name} swung at {rick.name} for {str(sarah.attack - (rick.defense + temporary_defense))} damage.")
        keyboard.wait('enter')
        
    #if either of them die then do this
    if (sarah.hp <= 0):
        print(f"\n{rick.name} swings one final strong blow, knocking {sarah.name} down, finishing her off.")
        keyboard.wait('enter')
        end1()

    elif (rick.hp <= 0):
        print(f"\n{sarah.name} lunges at you, grasping you hard and ripping you to shreds.")
        keyboard.wait('enter')
        tryagain()
    elif (rick.hp <= 0 and sarah.hp <=0):
        print(f"You and Sarah go head and head. You swing at her with one final blow and she rips you to shreds. Both of you die...Try again.")
        keyboard.wait('enter') 
        tryagain()  



def mutation():
    os.system('cls')
    print("Dr. Evans holds you back tightly. You struggle but fail to get out of his grasp.")
    keyboard.wait('enter')

    print("\nOne of the nurses approaches Sarah and holds her down. Sarah starts to kick and scream.")
    keyboard.wait('enter')

    print('\n  Dr. Evans:\n"I\'m sorry you had to see this happen, but you left me no choice. You were going to ruin my experiment."')
    keyboard.wait('enter')

    print('\nAs Sarah kicks and screams, the nurse injects her with a syringe.')
    keyboard.wait('enter')

    print('\nYou start to aggressivly squirm.\n\n  Rick:\n"What was that?! What are you doing?!"')
    keyboard.wait('enter')

    print('\nSarah stopped screaming and her body started to contort. Her stomach which was originally carrying your child starts to grow and grow.')
    keyboard.wait('enter')

    print('\nSarah starts to scream in agonizing pain as her pregnant stomach grows larger and larger until...')
    keyboard.wait('enter')

    print('\nA mutated figure pops out of her skin. Did the serum mutate your baby too?')
    keyboard.wait('enter')

    print('\nSarah\'s body continued to contort. Her limbs grew long and full of pustules. Her back cortorted, causing her to be in a back-bend position. The creature that is appearing out of her stomache, which used to be your child, now seemed to be taking over her body. The creature rips the nurse to shreds. What has the doctor created?')
    keyboard.wait('enter')

    print('\n  Rick:\n"What the- What the fuck is going on?!", the more you stare at this creature, the more you realize it is real. You freeze in shock.')
    keyboard.wait('enter')

    print('\nDr. evans shoves you forward in fear and runs out of the room, locking the door behind you. You are left in the room ALONE with this creature.')
    keyboard.wait('enter')
    os.system('cls')

    print("What do you do?\nFight your wife (Press '1')\nLet your wife kill you (Press '2')")

    while True:
        event = keyboard.read_event()
        if event.event_type == 'down':
            if event.name == '1':
                battle()
            if event.name == '2':
                death()
                break

    
    
#after going through the wall
def throughmirror():
    os.system('cls')
    print("You walk through this wall into this dark room. The only thing you can see is a few feet in front of you due to your flashlight.")
    keyboard.wait('enter')

    print('\n  Rick:\n"I have to find Sarah"')
    keyboard.wait('enter')

    print("\nAs you walk around the room you see a light switch. You go to turn on the lights but the fuze breaks and leaves you in complete darkness again.")
    keyboard.wait('enter')

    print("\nYou walk out into the hallway.")
    keyboard.wait('enter')

    print("\nYou hear screaming in the distance so you pick up speed down the hallway")
    keyboard.wait('enter')
    os.system('cls')

    print('You walk into a brightly lit room...')
    keyboard.wait('enter')

    print('\nIt took your eyes a second to adjust.')
    keyboard.wait('enter')

    print('\n  ???:\n"Rick?", a voice yelped out to you.')
    keyboard.wait('enter')

    print('\nThe yelp caught you off guard but you soon realized it was Sarah.')
    keyboard.wait('enter')

    print('\nYou quickly run towards Sarah who was tightly strapped down to a hospital bed.')
    keyboard.wait('enter')
    os.system('cls')

    print('\n  Rick:\n"Sarah?!"')
    keyboard.wait('enter')

    print('\n  Rick:\n"What did they do to you?", you exclaimed while struggling to untie her.')
    keyboard.wait('enter')

    print('\n  Sarah:\n"I don\'t know what they are planning, but I know it isn\'t goo-')
    keyboard.wait('enter')

    print('\n  Sarah:\n"WATCH OUT!", she quickly exclaimed')
    keyboard.wait('enter')

    print('\nYou quickly turn around where you see Dr. Evans swinging an IV stand at you.')
    keyboard.wait('enter')

    print("He knocks you to the ground and holds you tightly")
    keyboard.wait('enter')
    
    mutation()

def leftdoor2():
   os.system('cls')
   print("You walk into the rustic door. It almost seems bent out of place.")
   keyboard.wait('enter') 

   print("\nThere isn't much in the room but scattered objects.")
   keyboard.wait('enter')

   while True:
    os.system('cls')
    print("\nWhat do you want to do?:\nInvestigate (Press '1')\nLeave (Press '2')")
       
    event = keyboard.read_event()
    if event.event_type == 'down':
        if event.name == '1':
            invest_leftdoor2()
            break
        elif event.name == '2':
            left_of_office()
            break

def left_of_office():
    os.system('cls')
    print("\nYou walk outside to the left. There are two doors you can go through. Which door will you go through?\n  Door 1 (Press '1')\n  Door 2 (Press '2')\n  Go back (Press '3')")
    while True:
        event = keyboard.read_event()
        if event.event_type == 'down':
            if event.name == '1':
                if has_leftdoor1_key == True:
                    if investleftdoor1 == True:
                        print("\nYou already checked this room...")
                       
                    elif investleftdoor1 == False:
                        leftdoor1()

                elif has_leftdoor1_key == False:
                    print("\nThe door is locked...You need a  red key.")
                    
                 
            elif event.name == '2':
                if investleftdoor2 == True:
                    print("You already checked here...Try looking somewhere else...")
                    
                elif investleftdoor2 == False:
                    leftdoor2()
            elif event.name == '3':
                post_exit_choice()


def leftdoor1():
    global investleftdoor1
    os.system('cls')
    print("You creak open the door. It seems empty, so you walk in.")
    keyboard.wait('enter')

    print("\nIn the corner of your eye you see movement. You quickly fling to the left.")
    keyboard.wait('enter')

    print("\n\n---SLAM--\n\n")
    keyboard.wait('enter')

    # start nurse battle
    print("You encounter a nurse.")
    keyboard.wait('enter')

    print('\n  Nurse:\n"What are you doing here? You aren\'t supposed to be alive..." Without giving you time to process, she lunges at you with a broken piece of wood.')
    keyboard.wait('enter')

    print("\nYou quickly dodge her attack, hitting her in the back of the head with the metal bat. I don\'t think she will be waking up.")
    keyboard.wait('enter')

    investleftdoor1 = True

    left_of_office()



def invest_leftdoor2():
    global has_bat, investleftdoor2, has_leftdoor1_key
    os.system('cls')
    print("As you walk around the room, you pick up different items you think may help you.")
    keyboard.wait('enter')

    print("\nYou have obtained:\n  Medication x2\n  A bat\n  A red key")
    keyboard.wait('enter')

    has_bat = True
    investleftdoor2 = True
    has_leftdoor1_key = True
    
    left_of_office()


def right_righthall():
    global invest_rightrighthall
    os.system('cls')

    print("You walk down the right side of the hallway. There is nothing much down the hallway.")
    keyboard.wait('enter')

    print("At the end you see a room with a large glass window.")
    keyboard.wait('enter')

    print("In the room you could make out mutated figures in cages.")
    keyboard.wait('enter')

    os.system('cls')

    print('--SLAM--')
    keyboard.wait('enter')

    print("A large mutated monster slammed on the window, knocking you off your feet.")
    keyboard.wait
    print('\n  Rick:\n"What the hell is that?"')
    keyboard.wait('enter')
    invest_rightrighthall = True
    right_of_office()


def right_lefthall():
    global invest_rightlefthall
    os.system('cls')
    print("\nThere\'s nothing down this hallway but locked doors. I dont think there are any keys around to help.")
    keyboard.wait('enter')
    invest_rightlefthall = True
    right_of_office()

def after_mirror():
    global aftermirror
    print("\nYou smash the mirror with your bat creating glass shards. You put the shards on the opposite site of the balace scale to balance the bottle out.")
    keyboard.wait('enter')
    print('\n  Rick:\n"Now what-", before you finish your sentence, the wall to your left opens up like a door. You walk inside.')
    keyboard.wait('enter')
    throughmirror()
    
def interactmirror():#next
    global has_bat
    while True:
        if has_bat == False:
            print("You stare at yourself in the mirror. What could that paper mean?")
            keyboard.wait('enter')
            break
        if has_bat == True:
            print("You stare at the mirror for a second.")
            after_mirror()
            break
        
        

def right_of_office():

    os.system('cls')
    print("You walk down the dark hallway.")
    keyboard.wait('enter')

    print('\nYou get to the end. There\'s a table with a balance scale. On the one side is a bottle of poison and a piece of paper."')
    keyboard.wait('enter')

    print('\nThe paper reads "Use your reflection to balance me out."')
    keyboard.wait('enter')

    print('\n  Rick:\nWhat does that mean?')
    keyboard.wait('enter')


    print("\nWhat do you want to do?\n  Go right (Press '1')\n  Go left (Press '2')\n  Interact with mirror (Press '3')\n  Go back (Press '4')")

    while True:
        event = keyboard.read_event()
        if event.event_type == 'down':
            if event.name == '1':
                if invest_rightrighthall == False:
                    right_righthall()
                elif invest_rightrighthall == True:
                    print("\nYou already checked this place.")
                    
                    
            elif event.name == '2':
                if invest_rightlefthall == False:
                    right_lefthall()
                elif invest_rightlefthall == True:
                    print("\nYou already checked this place.")
            elif event.name == '3':
                interactmirror()
            elif event.name == '4':
                post_exit_choice()

def post_exit_choice():
    os.system('cls')
    print("\nYou are exiting the office, which way would you like to go?\n  Left (Press '1')\n  Right (Press '2')")
    while True:
        event = keyboard.read_event() # wait for player to press a key
        if event.event_type == 'down': # ensure it's a key-down not key-up
            if event.name == '1':
                left_of_office()
        
            if event.name == '2':
                right_of_office()


def exitingoffice():
    os.system('cls')
    print("Once you exit the room you look down each side of the halls. It's dark with barely any light. Thankfully you have your flashlight.")
    keyboard.wait('enter')

    post_exit_choice()




def officedoor_interact():
    os.system('cls')
    global door_locked, has_key
    if door_locked == True:
        if has_key == True:
            print("You shove the key into the slot and twist it open.\n\n---CLICK---\n\nThe door unlocks")
            door_locked = False # unlock door
            exitingoffice()
            return
        else:
            print('You rattle the knob hard but it doesn\'t budge.\n  Rick:\n"Damn it. Where would a key be?"')
    keyboard.wait('enter')
    os.system('cls')
    office()

def officedesk_interact():
    os.system('cls')
    print("You walk towards the desk.")

    print("\nWhat would you like the inspect?\n  The desk top (Press '1')\n  The drawers (Press '2')\n  Go back (Press '3')?")
    while True:
        event = keyboard.read_event() # wait for player to press a key
        if event.event_type == 'down': # ensure it's a key-down not key-up
            if event.name == '1':
                officedesktop_interact()
                break
            elif event.name == '2':
                officedeskdrawers_interact()
                break
            elif event.name == '3':
                office()
                break
    

def officedesktop_interact(): # desk top
    os.system('cls')
    print('On the desk were scattered manilla folders.')
    print("\nDo you want to investigate?\n  Yes (Press '1')\n  Go back (Press '2')")

    while True:
        event = keyboard.read_event()
        if event.event_type == 'down':
            if event.name == '1': # manilla folders
                os.system('cls')
                print("\nYou open one of the manilla folders from the top")
                keyboard.wait('enter')

                print("\nIt seems to be patient files.")
                keyboard.wait('enter')

                print('\nAs you read into the patient profiles, you realize something is strange about them. A key word that struck your attention.')
                time.sleep(2)
                print('"Mutation?"')
                keyboard.wait('enter')

                print('\nOne file read,\n "Jerry Stringer, 29, Male.\n\tDay 1: "Jerry was injected with the serum."\n\tDay 2: "The patient starting experiencing pruritus."\n\tDay 8: The patient started becoming violent. Injured three nurses and infected 1."\n\tDay 14: "Patient started to mutate. Became very large. Skin became grey and filled with pustules. Voice began to turn."')
                keyboard.wait('enter')

                print('\n\nYou look through the rest of the files and they are all similar.')
                keyboard.wait('enter')

                print('\n  Rick:\n"What the hell is this? And what serum are they injecting people."')
                keyboard.wait('enter')
                officedesk_interact()
                break
            elif event.name == '2':
                os.system('cls')
                officedeskdrawers_interact()
                break

            

def officedeskdrawers_interact():
    global flashlight, clutter
    os.system('cls')
    if flashlight == True:
        print("The desk is empty, you have already taken everything out of it.")
        keyboard.wait('enter')
        officedesk_interact()

    if flashlight == False:
        print('In the desk you find a bunch of clutter. This includes a magnet, coins, string, wire, a flashlight, and other unorganized crap. You keep in just in case.')
        keyboard.wait('enter')

        flashlight = True
        clutter = True

        print('\nNow you can use the flashlight to see better.')
        keyboard.wait('enter')
        officedesk_interact()

def officesink_interact():
    global flashlight, clutter, has_key
    os.system('cls')

    if flashlight == True:
        print('\nYou shine your light down the rusty sink.')
        keyboard.wait('enter')

        print("\nIn the bottom you see a key, but how will you get it?")
        keyboard.wait('enter')

        if clutter == True:
            print('\n  Rick:\n"Shit, I could use the magnet and the string."')
            keyboard.wait('enter')

            print('\nYou stick the small magnet attached to the string down the sink hoping it will hold.')
            keyboard.wait('enter')

            print('\nAfter slowly pulling the string back up, you obtain the dirty key.')
            keyboard.wait('enter')

            print('\n  Rick:\n"Yuck", you grunt out. "This better work."')
            keyboard.wait('enter')

            has_key = True #obtained key
        else:
            print("\nYou don't have anything to reach the key with/")
            keyboard.wait('enter')

    else: # no flashlight
        print('\n You try and look down the drain, but it is too dark to see.')
        keyboard.wait('enter')
    
    office() # return to office
     

def office():
    os.system('cls')
    
    print('Choose a place to search.')
    print("\n The Door (Press '1')\n  The desk (Press'2')\n  The sink (Press '3')")
    
    while True:
        event = keyboard.read_event()
        if event.event_type == 'down':
            if event.name == '1': # the door
                officedoor_interact()
                break

            elif event.name == '2': # desk
                officedesk_interact()
                break

            elif event.name == '3': # sink
                officesink_interact()
                break

        

#start the rest of the code

office()












