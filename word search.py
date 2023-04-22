import random

def generate_word_search(words, size):
    # Create the empty grid
    grid = [[' ' for _ in range(size)] for _ in range(size)]

    # Try to place each word in the grid
    for word in words:
        placed = False
        while not placed:
            # Choose a random starting position and direction
            start_x = random.randint(0, size-1)
            start_y = random.randint(0, size-1)
            direction_x, direction_y = random.choice([(1,0), (0,1), (1,1), (-1,1)])

            # Check if the word fits in the chosen starting position and direction
            if direction_x == 1 and size - start_x >= len(word) or \
                direction_y == 1 and size - start_y >= len(word) or \
                direction_x == -1 and start_x >= len(word)-1 or \
                direction_y == 1 and size - start_y >= len(word):
                fits = True
                for i in range(len(word)):
                    x = start_x + i * direction_x
                    y = start_y + i * direction_y
                    if grid[y][x] != ' ' and grid[y][x] != word[i]:
                        fits = False
                        break

                # If the word fits, place it in the grid
                if fits:
                    for i in range(len(word)):
                        x = start_x + i * direction_x
                        y = start_y + i * direction_y
                        grid[y][x] = word[i]
                    placed = True

    # Fill the remaining spaces with random letters
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for y in range(size):
        for x in range(size):
            if grid[y][x] == ' ':
                grid[y][x] = random.choice(letters)

    # Convert the grid to a string
    word_search = ''
    for row in grid:
        word_search += ' '.join(row) + '\n'

    return word_search

if __name__ == '__main__':
    while True:
        # Ask for the number of words and the size of the grid
        num_words = int(input('How many words do you want to include? '))
        grid_size = int(input('What should be the size of the grid? '))

        # Generate the words
        words = []
        for i in range(num_words):
            word = input('Enter word #{}: '.format(i+1)).upper()
            words.append(word)

        # Generate the word search and print it
        word_search = generate_word_search(words, grid_size)
        print(word_search)

        # Ask the user if they want to generate another word search
        answer = input('Do you want to generate another word search? (yes or no) ')
        if answer.lower() != 'yes':
            break