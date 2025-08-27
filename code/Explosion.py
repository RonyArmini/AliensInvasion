import pygame
from code.Entity import Entity

class Explosion(Entity):
    def __init__(self, position: tuple):
        # carrega todos os frames
        self.frames = [pygame.image.load(f'./asset/Explosion{i}.png').convert_alpha() for i in range(16)]
        self.current_frame = 0
        self.animation_speed = 3  # controla a velocidade da animação
        self.counter = 0

        # usa o primeiro frame como imagem inicial
        self.surf = self.frames[self.current_frame]
        self.rect = self.surf.get_rect(center=position)

        # valores obrigatórios para Entity
        self.name = "Explosion0"
        self.float_x = float(self.rect.x)
        self.float_y = float(self.rect.y)
        self.health = 1
        self.damage = 0
        self.score = 0
        self.last_dmg = "None"

    def move(self):
        self.counter += 1
        if self.counter >= self.animation_speed:
            self.counter = 0
            self.current_frame += 1
            if self.current_frame < len(self.frames):
                self.surf = self.frames[self.current_frame]
                self.rect = self.surf.get_rect(center=self.rect.center)
            else:
                self.health = 0  # explosão termina e se remove