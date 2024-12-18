class Dictionary:
    class WordBoard:
     def __init__(self, rows, cols):
        # Initialize the board with empty cells
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.rows = rows
        self.cols = cols

    def can_place_word(self, word, start_row, start_col, direction):
        """
        Check if a word can be placed on the board.
        Args:
            word (str): The word to place.
            start_row (int): Starting row index.
            start_col (int): Starting column index.
            direction (str): 'H' for horizontal, 'V' for vertical.

        Returns:
            bool: True if the word can be placed, False otherwise.
        """
        if direction not in ('H', 'V'):
            raise ValueError("Direction must be 'H' (horizontal) or 'V' (vertical).")

        word_length = len(word)
        if direction == 'H':
            if start_col + word_length > self.cols:  # Check board boundary
                return False
            for i in range(word_length):
                cell = self.board[start_row][start_col + i]
                if cell != ' ' and cell != word[i]:  # Overlap rules
                    return False
        elif direction == 'V':
            if start_row + word_length > self.rows:  # Check board boundary
                return False
            for i in range(word_length):
                cell = self.board[start_row + i][start_col]
                if cell != ' ' and cell != word[i]:  # Overlap rules
                    return False

        return True

    def load_dictionary(self, dictionary_file):
        """
        Load words from a dictionary file into a set for quick lookup.
        Args:
            dictionary_file (str): Path to the dictionary file.

        Returns:
            set: A set of valid words from the file.
        """
        try:
            with open(dictionary_file, 'r') as file:
                return {line.strip().upper() for line in file}
        except FileNotFoundError:
            raise FileNotFoundError(f"The dictionary file {dictionary_file} was not found.")

    def is_valid_word(self, word):
        """
        Check if a word is valid according to the dictionary.
        Args:
            word (str): The word to validate.

        Returns:
            bool: True if the word exists in the dictionary, False otherwise.
        """
        return word.upper() in self.dictionary

    def can_place_word(self, word, start_row, start_col, direction):
        """
        Check if a word can be placed on the board.
        Args:
            word (str): The word to place.
            start_row (int): Starting row index.
            start_col (int): Starting column index.
            direction (str): 'H' for horizontal, 'V' for vertical.

        Returns:
            bool: True if the word can be placed, False otherwise.
        """
        if not self.is_valid_word(word):
            raise ValueError(f"The word '{word}' is not valid according to the dictionary.")

        word_length = len(word)
        if direction == 'H':
            if start_col + word_length > self.cols:  # Check board boundary
                return False
            for i in range(word_length):
                cell = self.board[start_row][start_col + i]
                if cell != ' ' and cell != word[i]:  # Overlap rules
                    return False
        elif direction == 'V':
            if start_row + word_length > self.rows:  # Check board boundary
                return False
            for i in range(word_length):
                cell = self.board[start_row + i][start_col]
                if cell != ' ' and cell != word[i]:  # Overlap rules
                    return False
        else:
            raise ValueError("Direction must be 'H' (horizontal) or 'V' (vertical).")

        return True
    def place_word(self, word, start_row, start_col, direction):
        """
        Place a word on the board.
        Args:
            word (str): The word to place.
            start_row (int): Starting row index.
            start_col (int): Starting column index.
            direction (str): 'H' for horizontal, 'V' for vertical.

        Raises:
            ValueError: If the word cannot be placed.
        """
        if not self.can_place_word(word, start_row, start_col, direction):
            raise ValueError("Word cannot be placed at the given position.")

        if direction == 'H':
            for i in range(len(word)):
                self.board[start_row][start_col + i] = word[i]
        elif direction == 'V':
            for i in range(len(word)):
                self.board[start_row + i][start_col] = word[i]

    def display_board(self):
        """Print the current state of the board."""
        for row in self.board:
            print(' '.join(row))


