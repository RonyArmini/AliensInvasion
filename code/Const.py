# C
import pygame

C_ORANGE = (255, 128, 0)
C_YELLOW = (255, 255, 0)
C_WHITE = (255, 255, 255)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)

# E
EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SHOT_DELAY = {
    'Player1': 20,
    'Player2': 15,
    'Enemy1': 100,
    'Enemy2': 200,
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 1,
    'Player1Shot': 25,
    'Player2': 1,
    'Player2Shot': 20,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15,
    'Explosion0': 0,
    'Explosion1': 0,
    'Explosion2': 0,
    'Explosion3': 0,
    'Explosion4': 0,
    'Explosion5': 0,
    'Explosion6': 0,
    'Explosion7': 0,
    'Explosion8': 0,
    'Explosion9': 0,
    'Explosion10': 0,
    'Explosion11': 0,
    'Explosion12': 0,
    'Explosion13': 0,
    'Explosion14': 0,
    'Explosion15': 0,

}

ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'Player1': 0,
    'Player1Shot': 0,
    'Player2': 0,
    'Player2Shot': 0,
    'Enemy1': 100,
    'Enemy1Shot': 0,
    'Enemy2': 120,
    'Enemy2Shot': 0,
    'Explosion0': 0,
    'Explosion1': 0,
    'Explosion2': 0,
    'Explosion3': 0,
    'Explosion4': 0,
    'Explosion5': 0,
    'Explosion6': 0,
    'Explosion7': 0,
    'Explosion8': 0,
    'Explosion9': 0,
    'Explosion10': 0,
    'Explosion11': 0,
    'Explosion12': 0,
    'Explosion13': 0,
    'Explosion14': 0,
    'Explosion15': 0,


}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level2Bg0': 999,
    'Level2Bg1': 999,
    'Level2Bg2': 999,
    'Level2Bg3': 999,
    'Level2Bg4': 999,
    'Player1': 300,
    'Player1Shot': 1,
    'Player2': 300,
    'Player2Shot': 1,
    'Enemy1': 50,
    'Enemy1Shot': 1,
    'Enemy2': 60,
    'Enemy2Shot': 1,
    'Explosion0': 1,
    'Explosion1': 1,
    'Explosion2': 1,
    'Explosion3': 1,
    'Explosion4': 1,
    'Explosion5': 1,
    'Explosion6': 1,
    'Explosion7': 1,
    'Explosion8': 1,
    'Explosion9': 1,
    'Explosion10': 1,
    'Explosion11': 1,
    'Explosion12': 1,
    'Explosion13': 1,
    'Explosion14': 1,
    'Explosion15': 1,


}

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0.2,
    'Level1Bg3': 0.2,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level2Bg0': 1,
    'Level2Bg1': 2,
    'Level2Bg2': 3,
    'Level2Bg3': 4,
    'Level2Bg4': 5,
    'Player1': 3,
    'Player1Shot': 3,
    'Player2': 3,
    'Player2Shot': 3,
    'Enemy1': 1,
    'Enemy1Shot': 5,
    'Enemy2': 1,
    'Enemy2Shot': 2,
    'Explosion0': 1,
    'Explosion1': 1,
    'Explosion2': 1,
    'Explosion3': 1,
    'Explosion4': 1,
    'Explosion5': 1,
    'Explosion6': 1,
    'Explosion7': 1,
    'Explosion8': 1,
    'Explosion9': 1,
    'Explosion10': 1,
    'Explosion11': 1,
    'Explosion12': 1,
    'Explosion13': 1,
    'Explosion14': 1,
    'Explosion15': 1,

}

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_SPACE,
                    'Player2': pygame.K_LCTRL}

# S
SPAWN_TIME = 1000

#
TIMEOUT_STEP = 100  # 100ms
TIMEOUT_LEVEL = 40000  # 20 segundos

# W
WIN_WIDTH = 500
WIN_HEIGHT = 750

# S
SCORE_POS = {'Title': (WIN_WIDTH / 2, 250),
             'EnterName': (WIN_WIDTH / 2, 290),
             'Label': (WIN_WIDTH / 2, 300),
             'Name': (WIN_WIDTH / 2, 320),
             0: (WIN_WIDTH / 2, 330),
             1: (WIN_WIDTH / 2, 350),
             2: (WIN_WIDTH / 2, 370),
             3: (WIN_WIDTH / 2, 390),
             4: (WIN_WIDTH / 2, 410),
             5: (WIN_WIDTH / 2, 430),
             6: (WIN_WIDTH / 2, 450),
             7: (WIN_WIDTH / 2, 470),
             8: (WIN_WIDTH / 2, 490),
             9: (WIN_WIDTH / 2, 510),
             }
