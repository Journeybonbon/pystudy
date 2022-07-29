from hangman import User, HangMan

if __name__ == "__main__":
    user = User()
    game = HangMan(user)
    game.execute()
    game.gameOver()