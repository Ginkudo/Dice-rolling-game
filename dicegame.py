import random 
playing = True 
while playing: 
    num_dice = int(input("Enter number of dice: ")) 
    results = [random.randint(1, 6) for _ in range(num_dice)] 
    print(f"{results}") 
    play_again = input("Roll again? (y/n): ").lower() 
    if play_again == 'n': 
        print("Thanks for playing!") 
        playing = False
