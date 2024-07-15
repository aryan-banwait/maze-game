from game import play_game
import os

def main():
    os.environ['SDL_AUDIODRIVER'] = 'dummy'
    play_game()

main()