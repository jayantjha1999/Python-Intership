import random
import os  

WIN_LIST_RPS = [('ROCK', 'SCISSORS'), ('SCISSORS', 'PAPER'), ('PAPER', 'ROCK')]  
SELECTIONS_LIST_RPS = ['ROCK', 'PAPER', 'SCISSORS']

WIN_LIST_RPSLS = [('ROCK', 'SCISSORS'), ('ROCK', 'LIZARD'), ('SCISSORS', 'LIZARD'), ('SCISSORS', 'PAPER'), ('LIZARD', 'PAPER'), ('LIZARD', 'SPOCK'), ('PAPER', 'SPOCK'), ('PAPER', 'ROCK'),('SPOCK', 'ROCK'), ('SPOCK', 'SCISSORS')]

SELECTIONS_LIST_RPSLS = ['ROCK','PAPER','SCISSORS','LIZARD','SPOCK']

WIN_LIST_COMPANIES = [('GOOGLE', 'APPLE'), ('GOOGLE', 'MICROSOFT'), ('GOOGLE', 'SAMSUNG'),  
                      ('APPLE', 'MICROSOFT'), ('APPLE', 'SAMSUNG'), ('APPLE', 'AMAZON'),   
                      ('MICROSOFT', 'SAMSUNG'), ('MICROSOFT', 'AMAZON'), ('MICROSOFT', 'NINTENDO'), 
                      ('SAMSUNG', 'AMAZON'), ('SAMSUNG', 'NINTENDO'), ('SAMSUNG', 'SONY'), 
                      ('AMAZON', 'NINTENDO'), ('AMAZON', 'SONY'), ('AMAZON', 'GOOGLE'),  
                      ('NINTENDO', 'SONY'), ('NINTENDO', 'GOOGLE'), ('NINTENDO', 'APPLE'), 
                      ('SONY', 'GOOGLE'), ('SONY', 'APPLE'), ('SONY', 'MICROSOFT')] 
                    
SELECTIONS_LIST_COMPANIES = ['GOOGLE', 'APPLE', 'MICROSOFT', 'SAMSUNG', 'AMAZON', 'NINTENDO', 'SONY']


stats_count = {'player':0, 'computer':0, 'ties':0}

def clrscr():
  
  if os.name == "posix":  
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):  
    os.system('CLS')

def welcome():
  
  clrscr()
  while True:
    option = input(
      "-------------- Welcome to JAYANT Rock-Paper-Scissors Games --------------------"
    "\n-------------------------------------------------------------------------------"
    "\n                                 OPTIONS                                       "
    "\n-------------------------------------------------------------------------------"
    "\n [1] - Rock Paper Scissors                                          "
    "\n [2] - Rock Paper Scissors Lizard Spock                          "
    "\n [3] - Google, Apple, Microsoft, Samsung, Amazon, Nintendo, Sony "
    "\n [4] - Exit                                                                  "                   
    "\n------------------------------------------------------------------------------"
    "\n Please select an option (1, 2, 3 or 4): ")
    if option == '1' or option == '2' or option == '3':
        lets_play(option) 
    elif option == '4': 
      print("BYE BYE THANKS FOR COMING")
      exit()
    else:  
      input("Invalid option. Try again... Please press ENTER to continue")
      clrscr()
    
def lets_play(option):
  """ A function that sets which game is going to be played based on the option selected """
  clrscr()
  
  if option == '1':  
    intro = (" Welcome to Rock + Paper + Scissors game!")  
    option_help = ("\n This game is simple and goes as following:"  
          "\n *You can choose between: Rock, Paper or Scissors."
          "\n\n You must take in consideration that:"
          "\n *Rock crushers Scissors."
          "\n *Scissors cut Paper."
          "\n *Paper covers Rock."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'.")

    selections_list = SELECTIONS_LIST_RPS  
    win_list = WIN_LIST_RPS  
  
  elif option == '2':  
    intro = (" Welcome to Rock + Paper + Scissors + Lizard + Spock game!")
    option_help = ("\n This game is simple and goes as following:"
          "\n *You can choose between: Rock, Paper, Scissors, Lizard or Spock."
          "\n *Rock crushers Scissors and Lizard."
          "\n *Scissors cut Paper and decapitate Lizard."
          "\n *Lizard eats Paper and poisons Spock."
          "\n *Paper disproves Spock and covers Rock."
          "\n *Spock vaporizes Rock and smashes Scissors."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'.")
    selections_list = SELECTIONS_LIST_RPSLS  
    win_list = WIN_LIST_RPSLS  
  
  elif option == '3': 
    intro = (" Welcome to Google + Apple + Microsoft + Samsung + Amazon + Nintendo + Sony game!")
    option_help = ("\n This game is simple and goes as following:"
          "\n *You can choose between: Google, Apple, Microsoft, Samsung, Amazon, Nintendo or Sony."
          "\n\n You must take in consideration these facts:"
          "\n *Google's shares are higher than Apple, Microsoft and Samsung."
          "\n *Apple sells more phones than Microsoft, Samsung and Amazon."
          "\n *Microsoft can buy Samsung, Amazon and Nintendo."
          "\n *Samsung pays more money in advertising than Amazon, Nintendo and Sony."
          "\n *Amazon sells Nintendo, Sony and Google stuff on its website."
          "\n *Nintendo is older than Sony, Google and Apple."
          "\n *Sony has made better video game systems than Google, Apple and Microsoft."
          "\n\n Notes: *The first one that scores 5 points WINS the game!"
          "\n        *If you forgot the rules, just type 'help'."
          "\n        *If you want to go to main menu to try the other games, just type 'quit'.")
          
    selections_list = SELECTIONS_LIST_COMPANIES  
    win_list = WIN_LIST_COMPANIES  
      
  print(intro)  
  print(option_help) 
    
  while True:
    player_selection = input("Your Selection {}: ".format(selections_list))
    player_selection = player_selection.upper()
    
    if player_selection in selections_list:
      clrscr()
      computer_selection = random.choice(selections_list)
      
      print("Player Selection: {}".format(player_selection))
      print("Computer Selection: {}".format(computer_selection))
      
      match = player_selection, computer_selection 
      
      if player_selection == computer_selection:
        stats_count['ties'] += 1
        print("\nResult: Both are {}! So that's a Tie!".format(player_selection))
      elif match in win_list:
        stats_count['player'] += 1
        print("\nResult: The power of {} beats {}! You won!".format(player_selection, computer_selection))
      else:  
        stats_count['computer'] += 1
        print("\nResult: The power of {} is stronger than {}! You lost!".format(computer_selection, player_selection))
      print("-------  STATS  -------"
            "\n YOU  | COMPUTER | DRAW"
            "\n  {player}        {computer}        {ties}"
            "\n-----------------------".format(**stats_count))
      if stats_count['player'] == 5:  
        print("THE GAME IS OVER! YOU WON! CONGRATULATIONS!")
        exit()
      elif stats_count['computer'] == 5:  
        print("THE GAME IS DONE! YOU LOST AGAINST COMPUTER! PRACTICE HARD!")
        exit()
    elif player_selection == 'HELP':
      clrscr()
      print(option_help)
    elif player_selection == 'QUIT': 
      stats_count['player'] = 0
      stats_count['computer'] = 0
      stats_count['ties'] = 0
      input("Let's try another game mode then. I hope you enjoyed! Please press ENTER to continue...")
      clrscr()
      break
    elif player_selection == 'EXIT':
      print("Bye bye... TRY HARD!")
      exit()
    else:
      print("Invalid selection. Try again...")

        
welcome()