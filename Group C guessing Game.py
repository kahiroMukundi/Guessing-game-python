import random


class NumberGuessingGame:

    def __init__(self):
        self.LOWER = 1
        self.HIGHER = 100
        self.MAX_CHANCES = 5
        self.OUT_OF_CHANCES = False

    def get_random_number(self):
        return random.randint(self.LOWER, self.HIGHER)

    def start(self):
       
        random_number = self.get_random_number()

        print(
            f"Guess the randomly generated number from {self.LOWER} to {self.HIGHER}")

        chances = 0
        while True and not(self.OUT_OF_CHANCES):
            if chances < self.MAX_CHANCES :
               user_number = int(input("Enter the guessed number: "))
               chances += 1
            else : self.OUT_OF_CHANCES = True

            if self.OUT_OF_CHANCES :
                print ("-> Izah Bana. Your out of chances")
            

            if user_number == random_number   :
                print(
                    f"-> Wat a gwan! Umepata na {chances + 1} step{'s' if chances > 1 else ''}!")
                break
            elif user_number < random_number:
                print("-> Number yako ni ndogo kuliko the random number")
            else:
                print("-> Number yako ni kubwa kuliko the random number") 
                
           

numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start()

