import pygame
MAX_WIDTH = 800
MAX_HEIGHT = 400
def main():
    #게임 화면의 사이즈 설정
    screen = pygame.display.set_mode((MAX_WIDTH , MAX_HEIGHT))
    #게임 화면의 프레임 설정 ( 1초의 몇번을 깜빡일것인가)
    fps = pygame.time.Clock()
    #공룡 이미지 로드
    image_dino1 = pygame.image.load("images/dino1.png")
    image_dino2 = pygame.image.load("images/dino2.png")
    dino_height = image_dino1.get_size()[1]
    dino_bottom = MAX_HEIGHT - dino_height

if __name__ == '__main__':
    main()