﻿# Characters used by this game. 

define cal = Character("Cal")
define alice = Character("2Lt Alice")
define williams = Character("Cpt Williams")
define roland = Character("Sgt. Roland")
define violet = Character("Violet")

# Images used by this game
image bg fleet = im.Scale('covfleet.jpg', 1920, 1080)
image bg earth = im.Scale('earth.jfif', 1920, 1080)
image bg war = im.Scale('war.jpg', 1920, 1080)
image bg intro = im.Scale('intro.jpg', 1920, 1080)
image bg intro2 = im.Scale('intro2.jpg', 1920, 1080)
image bg ship = im.Scale('ship.jpg', 1920, 1080)

# The game starts here.

label start:

    stop music

    ##TODO: Need to add sprites

    ### TODO: need to add background images here: fleet img, planet glass img, covenant img, odst img, etc.
    play music 'audio/music/Halo 3 ODST OST Disk 1 Track 1 Overture.mp3'
    pause

    "The year is 2552." 

    scene bg earth
    with dissolve

    "Humanity has been at war with the covenant for over 25 years."
    "While war rages on throughout the galaxy, the planet of Felix Major has been attacked by a small Covenant fleet."

    scene bg fleet
    with dissolve

    "At first the planet was subject to glassing, just like Reach."
    ##planet glassing img and transition
    "The glassing did eventually come to a stop."
    "That's when the ground invasion began."

    scene bg war
    with dissolve
    "Operation Heavy Tide has been initiated by the UNSC in an effort to reduce civilian casualties and protect weapons manufacturing points in the area. "
    "The ground forces are already fighting a losing battle, but that's where we come in."
    scene bg intro

    "Orbital Drop Shock Troopers, or ODSTs for short. We jump feet first into hell."
    scene bg intro2
    # TODO: Need to change this text to center top of screen
    "We can't do the impossible, but we do our best to help turn the tides."
    scene black
    "ODSTs perform highly specialized, small scale, high-risk operations."
    "Anything from Deep Ground Surveillance, Long Range Reconnaissance, Direct Action, Unconventional Warfare, Counter-Terrorism Operations..." 
    # alice calls out to Cal

    scene black
    with hpunch
    # TODO: Find a way to change this to center of black screen. Some sort of effects? Fade in?
    "\"Cal\"{w}"
    with hpunch
    "... Among other things, but you get the point."
    "Essentially theres no end to the dangers that ..."
    with hpunch
    # TODO: Find a way to change this to center of black screen. Some sort of effects? Fade in?
    "\"CAL!!!\"{w}"
    with hpunch
    stop music
    "Whoops, I might be getting a little carried away."
    "Guess I better wake up or alice will keep shouting at me."

    scene bg ship
    with fade
    cal "Yeah yeah, I'm awake."

    # show alice angry
    alice "It's almost time for the brief! Did you get any sleep at all last night??"
    "Alice shrugged her head as she nudged me awake one last time."
    cal "Look, I was just getting a little extra for the road. No sweat."
    alice "Alright Cal, whatever you say. Just, pay attention, will ya?"
    "I give her a short smile and start to train my eyes on the main overhead display."
    "There are symbols on the screen that indicate various UNSC and Covenant forces, including battle composition, strength, and location."
    "I'm too tired to put together the full picture, so I wait until the commander enters the room."
    # TODO: Need to add a scene with the commander in the room.
    # Insert sound here of the bridge door opening and the commander entering the room
    williams "Alright, look alive people. We've got a lot to catch up on."
    "Oh brother, this is gonna be fun. Should I pay attention to this?"
    # Insert choice here to listen to the commander or ignore it.
    menu tutorial:
        "Should I stay awake for the brief, or should I just take a nap?"
        "Stay awake":
            "Nah, I better stay awake. This is important."
            williams "This mission is gonna be fast and simple."
            williams "The enemy is on Felix Major below us, and they intend on eliminating all human life on the planet."
            williams "We're not going to let that happen."
            

        "Doze off":
            "I'm gonna doze off instead."
            "I could use the extra sleep."
            scene black
            with fade
            "..."
    scene bg ship
    williams "And with that people, we're done here. Do I have any questions?"


    #FIXME: Remember to remove this later
    "This is the end of the game"
    # This ends the game.

return
