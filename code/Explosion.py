import pygame

from code.Entity import Entity


class Explosion(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.frame = 0
        self.animation_speed = 2  # Controla a velocidade da animação
        self.counter = 0

    def move(self):
        # Animação da explosão
        self.counter += 1
        if self.counter >= self.animation_speed:
            self.counter = 0
            self.frame += 1
            if self.frame <= 15:  # 16 frames (0-15)
                # Atualiza a imagem para o próximo frame
                self.surf = pygame.image.load(f'./asset/Explosion{self.frame}.png').convert_alpha()
                self.rect = self.surf.get_rect(center=self.rect.center)
            else:
                # Finaliza a explosão quando todos os frames foram exibidos
                self.health = 0