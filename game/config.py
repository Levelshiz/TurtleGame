import configparser

config = configparser.ConfigParser()
config.read('../config.ini')

MAX_HP = int(config.get('GameSettings', 'MAX_HP', fallback=100))
WINDOW_WIDTH = int(config.get('GameSettings', 'WINDOW_WIDTH', fallback=800))
WINDOW_HEIGHT = int(config.get('GameSettings', 'WINDOW_HEIGHT', fallback=800))
PLAYER_SPEED = float(config.get('GameSettings', 'PLAYER_SPEED', fallback=5.0))

if __name__ == '__main__':
    print(f"MAX_HP: {MAX_HP}")
    print(f"WINDOW_WIDTH: {WINDOW_WIDTH}")
    print(f"WINDOW_HEIGHT: {WINDOW_HEIGHT}")
    print(f"PLAYER_SPEED: {PLAYER_SPEED}")