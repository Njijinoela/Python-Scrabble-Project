def handle_player_turn(player_tiles, board, word, word_position, dictionary, draw_tiles):
    # Extract position details
    row, col, direction = word_position['row'], word_position['col'], word_position['direction']

    # Validate the word exists in the dictionary
    if word not in dictionary:
        return player_tiles, board, f"'{word}' is not a valid word."

    # Check if the word can be formed with the player's tiles
    temp_tiles = player_tiles.copy()
    for letter in word:
        if letter in temp_tiles:
            temp_tiles.remove(letter)
        else:
            return player_tiles, board, f"You don't have the tiles to form the word '{word}'."

    # Check if the word fits on the board and overlaps correctly
    for i, letter in enumerate(word):
        # Calculate the current position on the board
        curr_row = row + (i if direction == 'vertical' else 0)
        curr_col = col + (i if direction == 'horizontal' else 0)

        # Check board boundaries
        if curr_row >= len(board) or curr_col >= len(board[0]):
            return player_tiles, board, "The word doesn't fit on the board."

        # Check overlap or empty space
        if board[curr_row][curr_col] == letter:
            continue  # Valid overlap
        elif board[curr_row][curr_col] == '':
            continue  # Empty space is fine
        else:
            return player_tiles, board, "The word conflicts with existing tiles on the board."

    # Place the word on the board
    for i, letter in enumerate(word):
        curr_row = row + (i if direction == 'vertical' else 0)
        curr_col = col + (i if direction == 'horizontal' else 0)
        board[curr_row][curr_col] = letter

    # Remove used tiles and draw new ones
    for letter in word:
        if letter in player_tiles:
            player_tiles.remove(letter)
    new_tiles = draw_tiles(len(word))
    player_tiles.extend(new_tiles)

    return player_tiles, board, f"'{word}' was successfully played! You drew {new_tiles}."

