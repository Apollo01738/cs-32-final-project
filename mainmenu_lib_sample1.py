from hangman import hangman2_main
from tictactoe_new import tictactoe_main1
from good_tennis_sample3 import tennis_main

import csv
import pandas as pd

def login_user(c):
  logged_in = True
  #open csv file
  with open(c, newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    #store usernames, passwords, and coin balance in three separate lists
    usernames = []
    passwords = []
    balance = []
    rank = []
    for row in csv_reader:
      usernames.append(row[0])
      passwords.append(row[1])
      balance.append(row[2])
      rank.append(row[3])
  #prompt user to enter username and password
  username = input("Please enter your username: ")
  password = input("Please enter your password: ")

  #check if username and password are in csv file
  if username in usernames and password in passwords:
  #if username and password are in csv file, go to main menu
    pass
        
  else:
    while True:
        try:
            #if username and password are not in csv file, prompt user to create an account
            create_account = input("Login failed. Would you like to create an account? (yes/no): ").lower()
            if create_account == 'yes':
            #if yes, store new username, password, and account balance in csv file
                with open(c, 'a', newline='') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    csv_writer.writerow([username, password, '0', 'Noob'])

                    # updates the usernames, passwords, and balance list
                    usernames.append(username)
                    passwords.append(password)
                    balance.append('0')
                    rank.append('Noob')

                    #CALL MAIN MENU FUNCTION
                    print("Account created successfully! Welcome to the main menu!")
                    break
            elif create_account =='no':
                print("Goodbye")
                logged_in = False
                break
            else:
                raise ValueError()
        except ValueError:
           print("Answer must be 'yes' or 'no'")
  return username, usernames, balance, logged_in, password, rank

# The function that will update the coin balance after each game
def update_coins(c, won, usernames, username, balance, password):
    username_index = usernames.index(username)
    coins = balance[username_index]

     # creating the data frame to be edited to edit csv file
    df = pd.read_csv(c)

    if won == True:
        coins = int(coins) + 10
        # finds the row number of the data frame for the specific login info, but returns a list
        row_number = df[(df['username'] == username) & (df['password'] == password)].index
        #updates the column value in the data frame object
        df.at[row_number[0], 'balance'] = coins
        # writing the information back into the csv file
        df.to_csv(c, index=False)

        #updates the balance list that the coin_balance function uses to give user's balance
        balance[username_index] = str(coins)

    elif won == False:
        coins = int(coins) + 1
        # finds the row number of the data frame for the specific login info, but returns a list
        row_number = df[(df['username'] == username) & (df['password'] == password)].index
        #updates the column value in the data frame object
        df.at[row_number[0], 'balance'] = coins
        # writing the information back into the csv file
        df.to_csv(c, index=False)

        #updates the balance list that the coin_balance function uses to give user's balance
        balance[username_index] = str(coins)
  

#game selection function/interface
def game_selection(c, username, usernames, balance, password, rank):
  while True:
    try:
      print("Please select a game to play:")
      print("1. Hangman")
      print("2. Tic Tac Toe")
      print("3. Tennis")
      game = input("Enter your selection: ")
      
      if (game == "1"):
        won, replay = hangman2_main()
        update_coins('login.csv', won, usernames, username, balance, password)
        update_rank('login.csv', usernames, username, balance, password, rank)
        while replay == True:
          won, replay = hangman2_main()
          update_coins('login.csv', won, usernames, username, balance, password)
          update_rank('login.csv', usernames, username, balance, password, rank)
      elif (game == "2"):
        won, replay = tictactoe_main1()
        update_coins('login.csv', won, usernames, username, balance, password)
        update_rank('login.csv', usernames, username, balance, password, rank)
        while replay == True:
          won, replay = tictactoe_main1()
          update_coins('login.csv', won, usernames, username, balance, password)
          update_rank('login.csv', usernames, username, balance, password, rank)
      elif (game == "3"):
        won = tennis_main()
        update_coins('login.csv', won, usernames, username, balance, password)
        update_rank('login.csv', usernames, username, balance, password, rank)
        while True:
          try:
            print('1. Play again')
            print('2. Return to main menu')
            tennis_option = input('Enter your selection:')
            if tennis_option == '1':
              won = tennis_main()
              update_coins('login.csv', won, usernames, username, balance, password)
              update_rank('login.csv', usernames, username, balance, password, rank)
            elif tennis_option == '2':
              break
            else:
              raise ValueError()
          except ValueError:
            print("Please choose either '1' or '2'")
      else:
        raise ValueError()
      break
    except ValueError:
      print("Please enter a valid game")

# coin balance function/interface
def coin_balance(username, usernames, balance): 
  username_index = usernames.index(username)
  coins = balance[username_index]
  print("Your current coin balance is: " + coins)

  # gives user choice of when to return to main menu
  while True:
    try:
      next_action = input("Return to main menu? Yes or No: ").lower()
      if next_action == 'yes':
        break
      elif next_action == 'no':
        while True:
          try:
            return_to_main = input("Press 1 to return to main menu when ready ")
            if return_to_main == '1':
              break
            else:
              raise ValueError()
          except ValueError:
            print("Remember to hit '1'")
      else:
            raise ValueError()
      break
    except ValueError:
      print("Sorry, please choose 'Yes' or 'No'")
  return coins

# Function to update rank from noob to intermediate to expert to god
def update_rank(c, usernames, username, balance, password, rank):
    username_index = usernames.index(username)
    coins = int(balance[username_index])

     # creating the data frame to be edited to edit csv file
    df = pd.read_csv(c)

    if coins>= 500:
      # finds the row number of the data frame for the specific login info, but returns a list
        row_number = df[(df['username'] == username) & (df['password'] == password)].index
        #updates the column value in the data frame object
        df.at[row_number[0], 'rank'] = 'god'
        # writing the information back into the csv file
        df.to_csv(c, index=False)

        #updates the balance list that the coin_balance function uses to give user's balance
        rank[username_index] = 'god'

    elif coins >= 200:
      # finds the row number of the data frame for the specific login info, but returns a list
        row_number = df[(df['username'] == username) & (df['password'] == password)].index
        #updates the column value in the data frame object
        df.at[row_number[0], 'rank'] = 'Expert'
        # writing the information back into the csv file
        df.to_csv(c, index=False)

        #updates the balance list that the coin_balance function uses to give user's balance
        rank[username_index] = 'Expert'

    elif coins >= 50:
        # finds the row number of the data frame for the specific login info, but returns a list
        row_number = df[(df['username'] == username) & (df['password'] == password)].index
        #updates the column value in the data frame object
        df.at[row_number[0], 'rank'] = 'Intermediate'
        # writing the information back into the csv file
        df.to_csv(c, index=False)

        #updates the balance list that the coin_balance function uses to give user's balance
        rank[username_index] = 'Intermediate'
    
    else:
      pass


# function to check rank
def rank_status(username, usernames, rank): 
  username_index = usernames.index(username)
  user_rank = rank[username_index]
  print("Your current ranking is: " + user_rank)

  # gives user choice of when to return to main menu
  while True:
    try:
      next_action = input("Return to main menu? Yes or No: ").lower()
      if next_action == 'yes':
        break
      elif next_action == 'no':
        while True:
          try:
            return_to_main = input("Press 1 to return to main menu when ready ")
            if return_to_main == '1':
              break
            else:
              raise ValueError()
          except ValueError:
            print("Remember to hit '1'")
      else:
            raise ValueError()
      break
    except ValueError:
      print("Sorry, please choose 'Yes' or 'No'")
