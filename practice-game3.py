import sys
import pygame
from datetime import datetime
import time

pygame.init()
pygame.display.set_caption("데브라쿤 파이썬게임 연습1")
MAX_WIDTH = 800
MAX_HEIGHT = 400
# 게임에서 필요한 색상표
RED = (255, 0, 0)
ORANGE = (255, 153, 51)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
SEAGREEN = (60, 179, 113)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
VIOLET = (204, 153, 255)
PINK = (255, 153, 153)

# 폰트 설정
font = pygame.font.SysFont('Tahoma', 60)  # 기본 폰트 및 사이즈 설정(폰트1)
small_font = pygame.font.SysFont('Malgun Gothic', 20)  # 작은 사이즈 폰트(폰트2)
game_over = font.render("Game Over", True, BLACK)  # 게임 종료시 문구

def main():
    # 게임 화면의 사이즈 설정
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

    # #공룡 이미지 로드
    image_dino1 = pygame.image.load("images/dino1.png")
    image_dino2 = pygame.image.load("images/dino2.png")

    dino_height = image_dino1.get_size()[1]
    # 공룡이 바닥에 붙어 있는 모양을 만들고 싶음
    dino_bottom = MAX_HEIGHT - dino_height
    leg_swap = True
    is_jumping = False
    max_jumping_height = dino_bottom - 120

    # 공룡 좌표
    dino_x = 50
    dino_y = dino_bottom

    image_tree = pygame.image.load("images/tree.png")
    # 화면의 제일 우측에 장애물을 위치하게 해준다.
    tree_height = image_tree.get_size()[1]
    tree_x = MAX_WIDTH - 30
    tree_y = MAX_HEIGHT - tree_height

    tree_move_by_tick = 5
    # 게임 화면의 프레임 설정 ( 1초의 몇번을 깜빡일것인가)
    fps = pygame.time.Clock()
    check_time = 0

    dino_character = image_dino1.get_rect()
    tree_character = image_tree.get_rect()
    while True:
        tick = fps.tick(30)
        check_time = check_time + 1
        print("time : ", datetime.now(), "초당 frame 수 :", check_time)
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if not is_jumping:
                    is_jumping = True
        # 공룡이미지를 화면에 나오게 하는 부분 , dino_x , dino_y 좌표에 나오게됨
        if leg_swap:
            screen.blit(image_dino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(image_dino2, (dino_x, dino_y))
            leg_swap = True

        if is_jumping:
            dino_y = dino_y - 10
            if dino_y <= max_jumping_height:
                is_jumping = False
        else:
            dino_y = dino_y + 10
            if dino_y >= dino_bottom:
                dino_y = dino_bottom

        # 장애물의 x 위치값을 화면이 한번 깜빡일때 마다 tree_move_by_tick만큼 왼쪽으로 이동
        # 왼쪽으로 이동은 x값이 작아지게 만들어야 하니까 원래 장애물의 위치에서 계속 minus를 해준다.
        tree_x = tree_x - tree_move_by_tick
        # 장애물나무의 위치를 설정해서 화면에 나오게 함.
        screen.blit(image_tree, (tree_x, tree_y))
        #장애물이 왼쪽 화면 끝까지 가면 다시 처음으로 가서 이동되게 한다.
        if tree_x < 0:
            tree_x = MAX_WIDTH - 5

        # 공룡과 장애물의 충돌 감지를 위해 위치 정보를 업데이트해줘야 한다.
        dino_character.left = dino_x
        dino_character.top = dino_y
        tree_character.left = tree_x
        tree_character.top = tree_y

        if dino_character.colliderect(tree_character):
            print("충돌")
            time.sleep(0.5)
            screen.fill(SEAGREEN)
            screen.blit(game_over, (280, 200))
            time.sleep(1)


        pygame.display.update()

if __name__ == '__main__':
    main()
