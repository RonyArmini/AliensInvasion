#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, ENTITY_SPEED, WIN_HEIGHT
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.float_x += ENTITY_SPEED[self.name]
        self.rect.x = int(self.float_x)

        if self.rect.left >= WIN_WIDTH:
            self.float_x = -self.rect.width
            self.rect.x = int(self.float_x)
