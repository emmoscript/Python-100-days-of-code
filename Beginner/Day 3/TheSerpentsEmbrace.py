print("""


                                       ..
                                     .(  )`-._
                                   .'  ||     `._
                                 .'    ||        `.
                              .'       ||          `._
                            .'        _||_            `-.
                         .'          |====|              `..
                       .'             \__/               (  )
                     ( )               ||          _      ||
                     /|\               ||       .-` \     ||
                   .' | '              ||   _.-'    |     ||
                  /   |\ \             || .'   `.__.'     ||   _.-..
                .'   /| `.            _.-'   _.-'       _.-.`-'`._`.`
                \  .' |  |        .-.`    `./      _.-`.    `._.-'
                 |.   |  `.   _.-'   `.   .'     .'  `._.`---`
                .'    |   |  :   `._..-'.'        `._..'  ||
               /      |   \  `-._.'    ||                 ||
              |     .'|`.  |           ||_.--.-._         ||
              '    /  |  \ \       __.--'\    `. :        ||
               \  .'  |   \|   ..-'   \   `._-._.'        ||
`.._            |/    |    `.  \  \    `._.-              ||
    `-.._       /     |      \  `-.'_.--'                 ||
         `-.._.'      |      |        | |         _ _ _  _'_ _ _ _ _
              `-.._   |      \        | |        |_|_|_'|_|_|_|_|_|_|
                  [`--^-..._.'        | |       /....../|  __   __  |
                   \`---.._|`--.._    | |      /....../ | |__| |__| |
                    \__  _ `-.._| `-._|_|_ _ _/_ _ _ /  | |__| |__| |
                     \   _o_   _`-._|_|_|_|_|_|_|_|_/   '-----------/
                      \_`.|.'  _  - .--.--.--.--.--.`--------------'
      .```-._ ``-.._   \__   _    _ '--'--'--'--'--'  - _ - _  __/
 .`-.```-._ ``-..__``.- `.      _     -  _  _  _ -    _-   _  __/(.``-._
 _.-` ``--..  ..    _.-` ``--..  .. .._ _. __ __ _ __ ..--.._ / .( _..``
`.-._  `._  `- `-._  .`-.```-._ ``-..__``.-  -._--.__---._--..-._`...```
   _.-` ``--..  ..  `.-._  `._  `- `-._ .-_. ._.- -._ --.._`` _.-`   `-.

--------------------------------------------------------------------------------

 __   ____  ___   ___   ____  _     _____  __       ____  _      ___   ___    __    __    ____ 
( (` | |_  | |_) | |_) | |_  | |\ |  | |  ( (`     | |_  | |\/| | |_) | |_)  / /\  / /`  | |_  
_)_) |_|__ |_| \ |_|   |_|__ |_| \|  |_|  _)_)     |_|__ |_|  | |_|_) |_| \ /_/--\ \_\_, |_|__ 

""")

    
print('')

print("In 'The Serpent's Embrace,' you embark on an unforgettable treasure island adventure in the Caribbean. Set in the early 19th century, the game combines elements of swashbuckling adventure, mystery, and mysticism. As a daring and resourceful protagonist, you find yourself drawn to a fabled island rumored to hold untold riches." +  "You wake up in a giant ship awaiting the opportunity to steal a little boat and reach the island.")


while True:
    # Conditional 1: Secretly stealing the boat
    choice = input("Do you want to secretly steal the boat in the dead of night to go to the island? (yes/no): ")

    if choice.lower() == "yes":
        print("The game continues. You set off on a daring solo adventure.")
        # Rest of the game's code for this path
        break
    elif choice.lower() == "no":
        # Conditional 2: Informing your companions
        choice = input("Do you want to inform your companions about your plan to steal the boat? (yes/no): ")

        if choice.lower() == "yes":
            print("You lose: They believe you are planning to betray them and, as a result, they turn against you.")
            # Rest of the game's code with companions' reactions and their influence on the journey
            break
    else:
        print("Invalid choice. Please try again.")

while True:
    # Rest of the game's code for the solo adventure path
    # ...

    # Rest of the game's code for the companions' reactions path
    # ...

    # After the previous paths, continue the story for both paths
    print("You finally reach the island and begin exploring.")
    # Rest of the game's code for exploring the island, encountering obstacles, etc.
    # ...

    # Eventually, the player discovers the location of the ancient Boa ruins
    print("After hours of exploration, you stumble upon the legendary Boa ruins.")

    # Check if the player wants to enter the ruins
    choice = input("Do you want to enter the ruins? (yes/no): ")

    if choice.lower() == "yes":
        print("You cautiously enter the ruins, excited to uncover the hidden treasure.")
        # Rest of the game's code for exploring the ruins, solving puzzles, etc.
        # ...

        # Check if the player finds a mysterious artifact
        choice = input("While exploring, you stumble upon a mysterious artifact. Do you pick it up? (yes/no): ")

        if choice.lower() == "yes":
            print("You pick up the artifact, feeling a surge of power coursing through your veins.")
            # Rest of the game's code for the artifact's influence on the journey
            # ...

        else:
            print("You decide to leave the artifact behind, unsure of its true nature.")
            # Rest of the game's code for alternative paths or exploration
            # ...

        # Finally, the player discovers the treasure!
        print("Congratulations! You found the long-lost treasure of the Boa civilization!")
        # Rest of the game's code for the conclusion of the game
        # ...

        break
    elif choice.lower() == "no":
        print("You decide not to enter the ruins and continue your journey elsewhere.")
        # Rest of the game's code for alternative paths or exploration
        # ...

        break
    else:
        print("Invalid choice. Please try again.")
