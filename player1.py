def player_turn(word, player_rack, previous_word, board, tile_bag, dictionary):
    # 1. Validate word
    if not is_valid_word(word, dictionary):
        print("Invalid word. Please try again.")
        return False
    
    # 2. Validate overlap
    if not is_correct_overlap(word, previous_word, board):
        print("Word doesn't overlap correctly with the previous word.")
        return False
    
    # 3. Update tiles
    player_rack = update_tiles(player_rack, word, tile_bag)
    
    # 4. Update the board
    place_word_on_board(word, board)
    
    print(f"Your word '{word}' has been placed!")
    print(f"Remaining tiles in your rack: {player_rack}")
    return True
