from mainmenu_lib_sample1 import game_selection
from mainmenu_lib_sample1 import login_user
from mainmenu_lib_sample1 import coin_balance
from mainmenu_lib_sample1 import rank_status



def main():  # main menu where user can choose options
    username, usernames, balance, logged_in, password, rank = login_user('login.csv')
    if logged_in == True:
      while True:
        try:
          print("Welcome to the Arcade!")
          print("Please select an option:")
          print("1. Play a game")
          print("2. View Coin Balance")
          print("3. Check your Rank")
          print("4. Quit the game")
          option = input("Enter your selection: ")
          
          if (option == "1"):
            game_selection('login.csv', username, usernames, balance, password, rank) #Call the game selection function
          elif (option == "2"):
            coin_balance(username, usernames, balance) #Call the coin balance function
          elif (option == "3"):
            rank_status(username, usernames, rank) #Call the view rank function
          elif (option == "4"):
            break
          else:
            raise ValueError()
        except ValueError:
          print("Please enter a valid option")
      print("Thank you for playing!")
    else:
      pass

if __name__ == '__main__':
    main()