import random

TILE_BAG = {
    "A": 9, "B": 2, "C": 2, "D": 4, "E": 12, "F": 2, "G": 3, "H": 2, "I": 9,
    "J": 1, "K": 1, "L": 4, "M": 2, "N": 6, "O": 8, "P": 2, "Q": 1, "R": 6,
    "S": 4, "T": 6, "U": 4, "V": 2, "W": 2, "X": 1, "Y": 2, "Z": 1, "@": 2  
}

LETTER_POINTS = {
    "A": 1, "B": 3, "C": 3, "D": 2, "E": 1, "F": 4, "G": 2, "H": 4, "I": 1,
    "J": 8, "K": 5, "L": 1, "M": 3, "N": 1, "O": 1, "P": 3, "Q": 10, "R": 1,
    "S": 1, "T": 1, "U": 1, "V": 4, "W": 4, "X": 8, "Y": 4, "Z": 10, "@": 0
}

def draw_tiles(tile_bag, num=7):
    """
    Draw tiles randomly from the tile bag.
    
    Parameters:
        tile_bag (dict): The available tiles and their quantities.
        num (int): The number of tiles to draw.
    
    Returns:
        list: A list of tiles drawn.
    """
    tiles = []
    for _ in range(num):
        if not tile_bag:
            break
        tile = random.choice(list(tile_bag.keys()))
        tiles.append(tile)
        tile_bag[tile] -= 1
        if tile_bag[tile] == 0:
            del tile_bag[tile]
    return tiles


def calculate_score(word):
    """
    Calculate the Scrabble score for a given word.

    Parameters:
        word (str): The word to score.
    
    Returns:
        int: The score for the word.
    """
    return sum(LETTER_POINTS.get(letter.upper(), 0) for letter in word)


def refill_rack(rack, tile_bag, max_tiles=7):
    """
    Refills the player's rack to the maximum number of tiles.

    Parameters:
        rack (list): The current rack of tiles.
        tile_bag (dict): The tile bag to draw from.
        max_tiles (int): The maximum number of tiles in a rack.
    
    Returns:
        list: The updated rack.
    """
    while len(rack) < max_tiles and tile_bag:
        rack += draw_tiles(tile_bag, 1)
    return rack


def display_tile_bag(tile_bag):
    """
    Displays the remaining tiles in the bag.

    Parameters:
        tile_bag (dict): The tile bag to display.
    """
    print("Tile Bag:")
    for tile, count in sorted(tile_bag.items()):
        print(f"{tile}: {count}")


# Example Usage
if __name__ == "__main__":
    # Initial setup
    tile_bag = TILE_BAG.copy()
    player_rack = draw_tiles(tile_bag, 7)

    # Display initial state
    print(f"Initial Rack: {player_rack}")
    display_tile_bag(tile_bag)

    # Play a word
    word = "HELLO"
    print(f"\nPlaying word: {word}")
    score = calculate_score(word)
    print(f"Score for '{word}': {score}")

    # Refill rack
    player_rack = refill_rack(player_rack, tile_bag)
    print(f"\nUpdated Rack: {player_rack}")
    display_tile_bag(tile_bag)