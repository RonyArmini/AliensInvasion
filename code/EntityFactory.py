#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(6):  # level1bg images number
                    list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (WIN_WIDTH / 2, 493))
            case 'Player2':
                return Player('Player2', (WIN_WIDTH / 2 + 40, 493))
            case 'Enemy1':
                side = random.choice(("left", "right"))
                if side == "left":
                    return Enemy('Enemy1', (-50, random.randint(40, WIN_HEIGHT // 2)), direction="right")
                else:
                    return Enemy('Enemy1', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT // 2)), direction="left")
            case 'Enemy2':
                side = random.choice(("left", "right"))
                if side == "left":
                    return Enemy('Enemy2', (-50, random.randint(40, WIN_HEIGHT // 2)), direction="right")
                else:
                    return Enemy('Enemy2', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT // 2)), direction="left")