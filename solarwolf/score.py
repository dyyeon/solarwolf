import pygame
from pygame.locals import *
<<<<<<< HEAD
import game, gfx, math
<<<<<<< HEAD
from random import randint


img_1 = None
img_5 = None
img_10 = None
img_50 = None


def load_game_resources():
    global img_1, img_5, img_10, img_50
    img_1 = gfx.load('score_1.png')
    img_5 = gfx.load('score_5.png')
    img_10 = gfx.load('score_10.png')
    img_50 = gfx.load('score_50.png')

=======
from pygame.font import Font
>>>>>>> parent of bf8521a (translate finish)
=======
import game, gfx, math, txt
from pygame.font import Font
>>>>>>> bf8521a5af4ffe589903bbe11c20d1be3410706c

def render(score):
    #0일땐 출력하지 않게 함
    if score <= 0:
<<<<<<< HEAD
<<<<<<< HEAD
        out = pygame.Surface(img_1.get_size()).convert()
        out.set_colorkey(0, RLEACCEL)
        return out
    
    if score >= 50:
        imgs.append(img_50)
        score -= 50
    while score >= 40:
        imgs.append(img_10)
        imgs.append(img_50)
        score -= 40
    while score >= 10:
        imgs.append(img_10)
        score -= 10
    while score >= 9:
        imgs.append(img_1)
        imgs.append(img_10)
        score -= 9
    while score >= 5:
        imgs.append(img_5)
        score -= 5
    while score >= 4:
        imgs.append(img_1)
        imgs.append(img_5)
        score -= 4
    while score:
        imgs.append(img_1)
        score -= 1

    width = 0
    for i in imgs:
        width += i.get_width()
=======
        # 기존 코드와 동일한 크기의 빈 Surface 생성
        empty_surface = pygame.Surface((30, 36))  # 크기는 적절히 조정 가능
        empty_surface.set_colorkey(0, RLEACCEL)
        return empty_surface
    # 기본 폰트 사용
    font = Font(None, 36)
    
    # '[숫자]단계' 형식으로 텍스트 생성
    level_text = f"Stage {score}"
>>>>>>> parent of bf8521a (translate finish)
=======
        # 기존 코드와 동일한 크기의 빈 Surface 생성
        empty_surface = pygame.Surface((30, 36))  # 크기는 적절히 조정 가능
        empty_surface.set_colorkey(0, RLEACCEL)
        return empty_surface
    
    # 한글 폰트 사용
    font = Font(txt.font_path, 20)  #--- 단계 폰트를 36에서 20로 변경 ---
>>>>>>> bf8521a5af4ffe589903bbe11c20d1be3410706c
    

    # '[숫자]단계' 형식으로 텍스트 생성
    level_text = f"단계 {score}"
    
    # 흰색으로 텍스트 렌더링
    text_surface = font.render(level_text, True, (255, 255, 255))
    
    # 투명한 배경을 위한 설정
    text_surface.set_colorkey(0, RLEACCEL)
    
    return text_surface

# 게임 리소스 로드 함수는 더 이상 필요없으므로 비워둡니다
def load_game_resources():
    pass