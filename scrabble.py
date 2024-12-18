class Tile:
    def __init__(self, letter, value):
        self.letter = letter
        self.value = value

class Bag:
    def __init__(self):
        self.tiles = self.generate_tiles()

    def generate_tiles(self):
        # Define tile distribution and values
        distribution = {
            'A': (9, 1), 'B': (2, 3), 'C': (2, 3), 'D': (4, 2),
            'E': (12, 1), 'F': (2, 4), 'G': (3, 2), 'H': (2, 4),
            'I': (9, 1), 'J': (1, 8), 'K': (1, 5), 'L': (4, 1),
            'M': (2, 3), 'N': (6, 1), 'O': (8, 1), 'P': (2, 3),
            'Q': (1, 10), 'R': (6, 1), 'S': (4, 1), 'T': (6, 1),
            'U': (4, 1), 'V': (2, 4), 'W': (2, 4), 'X': (1, 8),
            'Y': (2, 4), 'Z': (1, 10), ' ': (2, 0) # Blanks
        }

        tiles = []
        for letter, (count, value) in distribution.items():
            tiles.extend([Tile(letter, value) for _ in range(count)])
        return tiles

    def draw_tiles(self, num):
        import random
        drawn_tiles = random.sample(self.tiles, num)
        for tile in drawn_tiles:
            self.tiles.remove(tile)
        return drawn_tiles

class Rack:
    def __init__(self, tiles=None):
        self.tiles = tiles if tiles else []

    def add_tiles(self, tiles):
        self.tiles.extend(tiles)

    def remove_tile(self, letter):
        for tile in self.tiles:
            if tile.letter == letter:
                self.tiles.remove(tile)
                return tile
        return None

    def display(self):
        return ''.join([tile.letter for tile in self.tiles])

class Player:
    def __init__(self, name):
        self.name = name
        self.rack = Rack()
        self.score = 0

    def draw_tiles(self, bag, num=7):
        self.rack.add_tiles(bag.draw_tiles(num))

    def play_word(self, word):
        word_score = 0
        for letter in word:
            tile = self.rack.remove_tile(letter)
            if tile:
                word_score += tile.value
            else:
                print(f"{letter} is not in your rack.")
                return 0
        self.score += word_score
        return word_score

class Board:
    def __init__(self):
        self.grid = [[' ' for _ in range(15)] for _ in range(15)]

    def place_word(self, word, start_row, start_col, direction):
        if direction not in ('horizontal', 'vertical'):
            print("Invalid direction. Use 'horizontal' or 'vertical'.")
            return False

        for i, letter in enumerate(word):
            row, col = start_row, start_col
            if direction == 'horizontal':
                col += i
            elif direction == 'vertical':
                row += i

            if row >= 15 or col >= 15 or self.grid[row][col] != ' ':
                print("Word placement invalid.")
                return False

        for i, letter in enumerate(word):
            row, col = start_row, start_col
            if direction == 'horizontal':
                col += i
            elif direction == 'vertical':
                row += i

            self.grid[row][col] = letter

        return True

    def display(self):
        for row in self.grid:
            print(' '.join(row))

class Game:
    def __init__(self, players):
        self.players = players
        self.bag = Bag()
        self.board = Board()
        self.current_player_index = 0

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def play(self):
        while self.bag.tiles:
            player = self.players[self.current_player_index]
            print(f"{player.name}'s turn.")
            print(f"Rack: {player.rack.display()}")
            self.board.display()

            word = input("Enter a word to play: ")
            start_row = int(input("Enter start row (0-14): "))
            start_col = int(input("Enter start column (0-14): "))
            direction = input("Enter direction (horizontal/vertical): ")

            if self.board.place_word(word.upper(), start_row, start_col, direction):
                score = player.play_word(word.upper())
                print(f"{player.name} scored {score} points!")
            else:
                print("Word placement failed.")

            player.draw_tiles(self.bag, 7 - len(player.rack.tiles))
            self.next_turn()

        print("Game over!")
        for player in self.players:
            print(f"{player.name}: {player.score} points")

# Example of starting the game
if __name__ == "__main__":
    player1 = Player("Thuo")
    player2 = Player("Njiji")
    game = Game([player1, player2])

    for player in game.players:
        player.draw_tiles(game.bag)

    game.play()
