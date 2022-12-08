import random

words = ["python", "strings", "integers", "indexes","program","list","floats","arrays","loops","statement","variable",
"method","define","boolean","object","print","data","function","while","return","input","operator","elif","slicing","append","condition"]

words = random.choice(words) #picks random word from the list

print("Try figuring out the word by guessing the characters, You got this!")


guesses = " " #Empty string 
tries = 10 #number of tries

while tries > 0:   #while loop begins
    wrong_guess = 0
    for char in words:   #Iterate every character in chosen word
        if char in words:
            if char in guesses:  #insert character into empty string (guesses)
                print(char, end = " ")
            if char not in guesses:
                print("_",end= " ") 
                wrong_guess +=1
    #top section allows the computer to print out the number of empty spaces requried base on the amount of letters in the chosen word
    
    if wrong_guess == 0:
        print("you win!")
        print("the word is:" , words)
        break
    guess = input("guess a character or type 'quit' to end the game: ")
    
    if guess.isalpha():
        guess = guess.lower() #forces the letter to be lower case
        guesses += guess
    else:
        print("Error: Please only input letters")
        guess = input("guess a character or type 'quit' to end the game: ")
        
    if guess.lower() == "quit": #User wants to quit
        print("You chose to quit")
        print("The word was:", words)
        break
    
    if guess not in words:
        tries -= 1
        print("Wrong, you have",tries, "more guesses" )
        if tries == 0:
            print("you lose, the word was...",words + "!")
    


