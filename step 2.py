class Computer:
    def __init__(self, dictionary, board, score=0):
        """
        Initialize the Computer player.

        :param dictionary: A set or list of valid words.
        :param board: A 2D list representing the game board.
        :param score: Initial score of the computer.
        """
        self.dictionary = dictionary
        self.board = board
        self.score = score

    def select_valid_word(self, last_word):
        """
        Select a valid word from the dictionary that overlaps correctly with the last word.

        :param last_word: The word previously placed by another player.
        :return: A valid word or None if no valid word is found.
        """
        for word in self.dictionary:
            if self._can_overlap(last_word, word):
                return word
        return None

    def _can_overlap(self, last_word, new_word):
        """
        Check if the new_word can overlap with the last_word.

        :param last_word: The word previously placed on the board.
        :param new_word: A candidate word to be placed.
        :return: True if the words can overlap; otherwise, False.
        """
        for char in last_word:
            if char in new_word:
                return True
        return False

    def place_word_on_board(self, word, last_word_position):
        """
        Place the word on the board based on the overlap with the last word.

        :param word: The word to place.
        :param last_word_position: A tuple (row, col, direction) indicating the position of the last word.
                                   Direction is 'horizontal' or 'vertical'.
        :return: A boolean indicating if the placement was successful.
        """
        row, col, direction = last_word_position

        for i, char in enumerate(word):
            if direction == 'horizontal':
                if 0 <= col + i < len(self.board[0]):
                    self.board[row][col + i] = char
                else:
                    return False
            elif direction == 'vertical':
                if 0 <= row + i < len(self.board):
                    self.board[row + i][col] = char
                else:
                    return False
        return True

    def update_score(self, word):
        """
        Update the computer's score based on the word placed.

        :param word: The word that was placed.
        :return: None
        """
        self.score += len(word)

# # Example usage
# dictionary = {"apple", "pear", "grape", "orange", "peach"}
# board = [[" " for _ in range(15)] for _ in range(15)]
# computer = Computer(dictionary, board)

# # Simulating a turn
# last_word = "apple"
# last_word_position = (4, 4, 'horizontal')  # Example: "apple" is placed starting at (4, 4) horizontally

# word = computer.select_valid_word(last_word)
# if word:
#     success = computer.place_word_on_board(word, last_word_position)
#     if success:
#         computer.update_score(word)
#         print(f"Computer placed '{word}' on the board. Current score: {computer.score}")
#     else:
#         print("Failed to place the word on the board.")
# else:
#     print("No valid word found.")
