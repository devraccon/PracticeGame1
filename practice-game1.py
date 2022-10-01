import sys

import pygame

pygame.init()
pygame.display.set_caption("데브라쿤 파이썬게임 연습1")
MAX_WIDTH = 800
MAX_HEIGHT = 400


def main():
    # 게임 화면의 사이즈 설정
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

    # 게임 화면의 프레임 설정 ( 1초의 몇번을 깜빡일것인가)
    fps = pygame.time.Clock()
    # #공룡 이미지 로드
    image_dino1 = pygame.image.load("images/dino1.png")
    image_dino2 = pygame.image.load("images/dino2.png")
    dino_height = image_dino1.get_size()[1]
    # 공룡이 바닥에 붙어 있는 모양을 만들고 싶음
    dino_bottom = MAX_HEIGHT - dino_height

    image_tree = pygame.image.load("images/tree.png")
    #화면의 제일 우측에 장애물을 위치하게 해준다.
    tree_height = image_tree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    # 공룡 좌표
    dino_x = 50
    dino_y = dino_bottom
    #공룡이 뛰는것처럼 보이게 하고 싶어 이미지1 , 이미지2 를 바꿔서 화면에 보여주기 위한 flag
    leg_swap = True
    is_jumping = False
    max_jumping_height = dino_bottom - 120
    jumping_speed = 0.5
    tree_move_speed = 0.5
    while True:
        tick = fps.tick(60)
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYUP:
                if not is_jumping:
                    is_jumping = True

        # 공룡 위치
        if leg_swap:
            screen.blit(image_dino1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(image_dino2, (dino_x, dino_y))
            leg_swap = True

        if is_jumping:
            dino_y = dino_y - (jumping_speed * tick)
            if dino_y <= max_jumping_height:
                is_jumping = False
        else:
            dino_y = dino_y + (jumping_speed * tick)
            if dino_y >= dino_bottom:
                dino_y = dino_bottom

        tree_x = tree_x - (tree_move_speed * tick)
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        screen.blit(image_tree, (tree_x, tree_y))

        pygame.display.update()



if __name__ == '__main__':
    main()
