import random


class rps:

    def __init__(self):
        self.list_of_moves = ["Rock", "Paper", "Scissors"]
        self.computer_choice = random.choice(self.list_of_moves)
        self.user_choice = self.get_user_choice()

    def show_please_enter():

        print("!!!Please enter either 1, 2 or 3!!!\n")

    def get_user_choice(self):

        while True:
            print("To select a move press:\n")

            for count, move in enumerate(self.list_of_moves):
                print(f"{count+1} => {move}")

            user_input = input("Please enter your choice.\n")

            try:
                user_input = int(user_input)
                
                if user_input in [1,2,3]:
                    break
                
                else:
                    rps.show_please_enter()

            except:
                rps.show_please_enter()
            

        return self.list_of_moves[user_input-1]


    def get_winner(computer_choice, user_choice):

        print(f"The computer chose {computer_choice} and you chose {user_choice}.\n")

        hierarchy = ["Rock", "Scissors", "Paper", "Rock"]

        if computer_choice == user_choice:
            print("It is a tie!")
            return

        elif hierarchy.index(computer_choice) + 1 == hierarchy.index(user_choice,1):
            print("You lost")
            return computer_choice
            
        else:
            print("You won!")
            return user_choice

def play():
    game = rps()
    rps.get_winner(game.computer_choice, game.user_choice)

play()