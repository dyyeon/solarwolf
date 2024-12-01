import pygame
from pygame.locals import *
import game, gfx, snd
import random

class GalagaGame:
    def __init__(self, prevhandler):
        self.prevhandler = prevhandler
        self.done = False
        self.first = True
        self.player_pos = [gfx.rect.centerx, gfx.rect.bottom - 50]
        self.player_dx = 0
        self.player_lives = 3
        self.score = 0
        self.player_bullets = []
        self.player_rect = None

        self.myfont = pygame.font.SysFont('Comic Sans MS', 20)

        # 외계인 우주선 여러 개 생성 (랜덤화)
        self.alien_number = 6
        self.alien_x = []
        self.alien_y = []
        self.alien_dx = []
        self.alien_dy = []
        self.alien_images = [gfx.load('enemy1.png'), gfx.load('enemy2.png'), gfx.load('enemy3.png')]

        # 외계인 초기 설정 (랜덤 위치, 속도, 이미지 선택)
        for _ in range(self.alien_number):
            self.alien_x.append(random.randint(50, gfx.rect.width - 50))  # 랜덤한 X 위치
            self.alien_y.append(random.randint(50, 150))  # 랜덤한 Y 위치
            self.alien_dx.append(random.uniform(0.05, 0.2))  # 랜덤한 속도
            self.alien_dy.append(0.0)  # Y 방향 속도
        self.alien_current_image = [random.choice(self.alien_images) for _ in range(self.alien_number)]

    def draw_player(self):
        ship_image = gfx.load('ship-up.png')
        self.player_rect = ship_image.get_rect(center=self.player_pos)
        gfx.surface.blit(ship_image, self.player_rect)
        gfx.dirty(self.player_rect)

    def draw_aliens(self):
        for i in range(self.alien_number):
            alien_image = self.alien_current_image[i]
            alien_rect = alien_image.get_rect(center=(self.alien_x[i], self.alien_y[i]))
            gfx.surface.blit(alien_image, alien_rect)
            gfx.dirty(alien_rect)

    def draw_score(self):
        score_text = self.myfont.render(f'Score: {self.score}', True, (255, 255, 255))
        gfx.surface.blit(score_text, (10, gfx.rect.height - 30))

    def update_player_position(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player_dx = -1
            elif event.key == pygame.K_RIGHT:
                self.player_dx = 1
            elif event.key == pygame.K_SPACE:
                self.fire_player_bullet()
        elif event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                self.player_dx = 0

    def move_player(self):
        self.player_pos[0] += self.player_dx
        self.player_pos[0] = max(0, min(self.player_pos[0], gfx.rect.width))

    def fire_player_bullet(self):
        bullet_frames = gfx.animstrip(gfx.load('fire.png'))
        bullet_x = self.player_pos[0]
        bullet_y = self.player_pos[1] - 20
        self.player_bullets.append({
            "frames": bullet_frames,
            "current_frame": 0,
            "x": bullet_x,
            "y": bullet_y,
            "dy": -1
        })

    def draw_bullets(self):
        for bullet in self.player_bullets:
            current_frame = bullet["frames"][bullet["current_frame"]]
            bullet_rect = current_frame.get_rect(center=(bullet["x"], bullet["y"]))
            gfx.surface.blit(current_frame, bullet_rect)
            gfx.dirty(bullet_rect)

    def update_bullets(self):
        for bullet in self.player_bullets:
            bullet["y"] += bullet["dy"]
            bullet["current_frame"] = (bullet["current_frame"] + 1) % len(bullet["frames"])
            if bullet["y"] < 0:
                self.player_bullets.remove(bullet)

    def check_collisions(self):
        for bullet in self.player_bullets:
            bullet_rect = pygame.Rect(bullet["frames"][bullet["current_frame"]].get_rect(center=(bullet["x"], bullet["y"])))
            for i in range(self.alien_number):
                alien_rect = pygame.Rect(self.alien_current_image[i].get_rect(center=(self.alien_x[i], self.alien_y[i])))
                if bullet_rect.colliderect(alien_rect):
                    self.player_bullets.remove(bullet)
                    self.score += 1
                    self.alien_x[i], self.alien_y[i] = random.randint(50, gfx.rect.width - 50), random.randint(50, 150)
                    self.alien_dx[i] *= random.choice([-1, 1])
                    self.alien_current_image[i] = random.choice(self.alien_images)  # 외계인 이미지 랜덤 변경
                    break

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                self.player_rect = None
                gfx.surface.fill((0, 0, 0))
                pygame.display.update()
                self.abort_game()
            self.update_player_position(event)

    def abort_game(self):
        self.done = True
        game.handler = self.prevhandler

    def move_aliens(self):
        for i in range(self.alien_number):
            self.alien_x[i] += self.alien_dx[i]
            if self.alien_x[i] <= 0 or self.alien_x[i] >= gfx.rect.width - self.alien_current_image[0].get_width():
                self.alien_dx[i] *= -1
                self.alien_y[i] += 30

    def game_over(self):
        self.abort_game()
        pygame.display.update()

    def run(self):
        while not self.done:
            self.handle_events()
            self.move_player()
            self.move_aliens()
            self.update_bullets()
            self.check_collisions()

            gfx.surface.fill((0, 0, 0))
            self.draw_player()
            self.draw_aliens()
            self.draw_bullets()
            self.draw_score()

            pygame.display.update()

        return game.handler
