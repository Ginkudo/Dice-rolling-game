import random 
dice_faces = {
    1: "⚀", 2: "⚁", 3: "⚂", 4: "⚃", 5: "⚄", 6: "⚅"
}
playing = True 
roll_count = 0
while playing: 
    num_dice = int(input("Enter number of dice: ")) 
    results = [random.randint(1, 6) for _ in range(num_dice)]
    roll_count += 1
    print(f"Roll {roll_count}: {results}") 
    faces = [dice_faces[val] for val in results]
    print('Faces: ' + ' '.join(faces))
    play_again = input("Roll again? (y/n): ").lower() 
    if play_again == 'n': 
        print("Thanks for playing!") 
        playing = False
