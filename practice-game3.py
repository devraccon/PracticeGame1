import sys

import pygame

pygame.init()
pygame.display.set_caption("데브라쿤 파이썬게임 연습1")
MAX_WIDTH = 800
MAX_HEIGHT = 400


def main():
    # 게임 화면의 사이즈 설정
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

    # #공룡 이미지 로드
    ㅊ
    image_dino2 = pygame.image.load("images/dino2.png")
    dino_height = image_dino1.get_size()[1]
    # 공룡이 바닥에 붙어 있는 모양을 만들고 싶음
    dino_bottom = MAX_HEIGHT - dino_height

    # 공룡 좌표
    dino_x = 50
    dino_y = dino_bottom

    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.blit(image_dino1, (dino_x, dino_y))

        pygame.display.update()



if __name__ == '__main__':
    main()
