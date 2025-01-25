import random

class PenduLogic:
    def __init__(self, word_list, max_lives):
        self.word_list = word_list
        self.max_lives = max_lives
        self.reset_game()
        self.Score = 0
        self.stage = 1
        self.word = random.choice(self.word_list).lower()
        self.lives = self.max_lives
        self.guessed_letters = set()
        self.display_word = ['_' for _ in self.word]
        self.game_over = False
        self.won = False
        self.Founded_word = []

    def next_stage(self):
        self.stage += 1
        self.word = random.choice(self.word_list).lower()
        self.lives = self.max_lives
        self.guessed_letters = set()
        self.display_word = ['_' for _ in self.word]
        self.won = False

    def survival(self):
        self.Score += len(self.word)
        self.word = random.choice(self.word_list).lower()
        self.guessed_letters = set()
        self.display_word = ['_' for _ in self.word]
        self.game_over = False


    def reset_game(self):
        self.word = random.choice(self.word_list).lower()
        self.lives = self.max_lives
        self.guessed_letters = set()
        self.display_word = ['_' for _ in self.word]
        self.Score = 0
        self.stage = 1
        self.game_over = False
        self.won = False
        self.Founded_word = []

    def arcade_mode(self, letter):
        if self.game_over or not letter or len(letter) != 1 or not letter.isalpha():
            return "Invalid input."

        letter = letter.lower()
        if letter in self.guessed_letters:
            return f"Letter '{letter}' already guessed."

        self.guessed_letters.add(letter)
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.display_word[i] = letter

            if '_' not in self.display_word:
                self.won = True
                self.Founded_word.append(self.word)
                self.next_stage()
                return f"Stage completed! Next word: {' '.join(self.display_word)}"

        else:
            self.lives -= 1
            f"Lives : {self.lives}"
            if self.lives <= 0:
                self.game_over = True
                f"Game Over. The word was '{self.word}'."
                self.reset_game()

    def survival_mode(self, letter):
        if self.game_over or not letter or len(letter) != 1 or not letter.isalpha():
            return "Invalid input."

        letter = letter.lower()
        if letter in self.guessed_letters:
            return f"Letter '{letter}' already guessed."

        self.guessed_letters.add(letter)
        if letter in self.word:
            for i, char in enumerate(self.word):
                if char == letter:
                    self.display_word[i] = letter

            if '_' not in self.display_word:
                self.won = True
                self.Founded_word.append(self.word)
                self.survival()
                return f"Next word: {' '.join(self.display_word)}"


        else:
            self.lives -= 1
            f"Lives : {self.lives}"
            if self.lives <= 0:
                self.game_over = True
                f"Game Over"
                return self.reset_game()



    def get_display_word(self):
        return ' '.join(self.display_word)

class ScrabbleLogic:
    def __init__(self, word_list):
        self.word_list = word_list
        self.reset_game()
        self.Score = 0
        self.selected_words = random.sample(self.word_list, 3)
        combined_letters = ''.join(self.selected_words)
        self.letters = list(set(combined_letters))
        random.shuffle(self.letters)
        self.found_words = []
        self.remaining_words = set(self.selected_words)
        self.game_over = False
        self.won = False

    def reset_game(self):
        self.selected_words = random.sample(self.word_list, 3)
        combined_letters = ''.join(self.selected_words)
        self.letters = list(set(combined_letters))
        random.shuffle(self.letters)
        self.found_words = []
        self.remaining_words = set(self.selected_words)
        self.game_over = False
        self.won = False
        self.Score = 0

    def submit_word(self, word):
        if self.game_over:
            return "Game already over."

        word = word.lower()
        if word in self.remaining_words:
            self.found_words.append(word)
            self.remaining_words.remove(word)
            self.Score += len(word)

            if not self.remaining_words:
                self.game_over = True
                return f"Congratulations! You found all words: {', '.join(self.found_words)}."

            return f"Correct! Words found: {', '.join(self.found_words)}"
        elif word in self.found_words:
            return f"'{word}' Already found."
        elif word not in self.remaining_words and word in self.word_list:
            self.Score += (len(word)//2)
            self.found_words.append(word)
            return f"Bonus word :'{word}'"
        else:
            return f"'{word}' is incorrect."

    def get_letters(self):
        return ' '.join(self.letters)
