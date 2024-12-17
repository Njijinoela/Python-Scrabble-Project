def start_game(player, computer, board, dictionary):
  
    print("Welcome to Scrabble!")
    print("Game is starting...\n")
    print(board.display())
    game_over = False

    while not game_over:
      
        print("\n--- Player's Turn ---")
        player_word = player.make_move(board, dictionary)
        
        if player_word:
            print(f"Player played: {player_word}")
        else:
            print("Player skipped their turn.")

      
        if player.is_out_of_tiles() or board.is_full():
            game_over = True
            break

    
        print("\n--- Computer's Turn ---")
        computer_word = computer.make_move(board, dictionary)
        
        if computer_word:
            print(f"Computer played: {computer_word}")
        else:
            print("Computer skipped their turn.")

       
        if computer.is_out_of_tiles() or board.is_full():
            game_over = True

   
    print("\nGame Over!")
    print("Final board state:\n")
    print(board.display())
    player_score = player.calculate_score()
    computer_score = computer.calculate_score()
    print(f"Final Scores:\nPlayer: {player_score}\nComputer: {computer_score}")
    
    if player_score > computer_score:
        print("Congratulations, you win!")
    elif player_score < computer_score:
        print("Computer wins! Better luck next time!")
    else:
        print("It's a tie!")

