# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kev = Character("Kevin")
define ben = Character("Benny")
define frd = Character("Fred")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg theatre
    show benny idle at left
    show kevin idle at right
    kev "Hello I am pleased to meet you."
    ben "Fuck you" 
    hide benny
    # This ends the game.

    return
