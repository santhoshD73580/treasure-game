#print('''                    ____...------------...____
 #              _.-"` /o/__ ____ __ __  __ \o\_`"-._
  #           .'     / /                    \ \     '.
   #          |=====/o/======================\o\=====|
    #         |____/_/________..____..________\_\____|
     #        /   _/ \_     <_o#\__/#o_>     _/ \_   \
      #       \_________\####/_________/             / 
       #       |===\!/========================\!/===|
        #      |   |=|          .---.         |=|   |
         #     |===|o|=========/     \========|o|===|
          #    |   | |         \() ()/        | |   |
           #   |===|o|======{'-.) A (.-'}=====|o|===|
           #
            #  | __/ \__     '-.\uuu/.-'    __/ \__ |
             # |==== .'.'^'.'.====|                 
              #|  _\o/   __  {.' __  '.} _   _\o/  _|
              #`""""-""""""""""""""""""""""""""-""""`''')
print('''Welcome to Treasure Island.
Your mission is to find the treasure.''')
start=input('''you'r at a cross. Where do you want to go?
                      Type "left" or "Right" : ''').lower()
if start =="left":
    print("you've come to a lake. There is an island in the middle of the lake.")
    #swim _ or wait ...
    swim_or_wait=input('''Are you going to "swim" or "wait" : ''').lower()
    if swim_or_wait =="wait":
        print("you are going to wait for the boat")
    else:
        print("game over")    
    Which_boat=input('''Which boat do you choose "Red","Yellow","Blue"''').lower()
    if Which_boat =="yellow":
        print("You Win!")
    elif Which_boat =="blue":
        print("Eaten by beasts. Game Over. ")    
    elif Which_boat =="red":
        print(" Burned by fire.Game Over.")
    else:
        print("Game Over")     
else:
    print("Fall into a hole.Game Over.")