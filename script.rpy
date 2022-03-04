# Characters used by this game. 

define cal = Character("Cal")
define cooper = Character("2Lt Cooper")
define williams = Character("Cpt Williams")
define roland = Character("Sgt. Roland")

# The game starts here.

label start:

    stop music

    # the game continues here

    # No background image
    ##TODO: Need to add imgs

    # no character sprite
    ##TODO: Need to add sprites

    # These display lines of dialogue.
    ### TODO: need to add background images here: fleet img, planet glass img, covenant img, odst img, etc.
    play music 'audio/music/Overture.mp3'
    pause
    "The year is 2552."
    "Humanity has been at war with the covenant for over 25 years."

    "While war rages on throughout the galaxy, the planet of Felix Major has been attacked by a small Covenant fleet."

    "At first, the planet was subject to glassing, just like Reach."
    ##planet glassing img and transition
    "However, the glassing did stop."

    "That's when the ground invasion began."
    ##covenant fight img and transition
    "Operation Heavy Tide has been initiated by the UNSC in an effort to reduce civilian casualties and protect weapons manufacturing points in the area. "

    "The ground forces are already fighting a losing battle, but that's where we come in."
    ###Insert ODST img and transition.
    
    "Orbital Drop Shock Troopers, or ODSTs for short. We jump feet first into hell."

    #FIXME: Remember to remove this later
    "This is the end of the game"
    # This ends the game.

return
