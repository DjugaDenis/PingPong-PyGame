import pygame
import sys

class Game:
    def play():
        pygame.init()

        SCREEN_WIDTH = 800
        SCREEN_HEIGHT = 600
        WINDOW_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)

        screen = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
        BACKGROUND_IMAGE = pygame.image.load('images/background.png')

        pygame.display.set_caption('PingPong')

        surface = pygame.display.get_surface()

        racket_pos_1 = SCREEN_HEIGHT / 2 - (SCREEN_HEIGHT * 0.05)
        racket_h_1 = SCREEN_HEIGHT * 0.1
        racket_pos_2 = SCREEN_HEIGHT / 2 - (SCREEN_HEIGHT * 0.05)
        racket_h_2 = SCREEN_HEIGHT * 0.1
        speed_rkt = SCREEN_HEIGHT * 0.025

        ball_x = SCREEN_WIDTH / 2
        ball_y = SCREEN_HEIGHT / 2
        ball_r = SCREEN_WIDTH * SCREEN_HEIGHT * 0.00003

        ball_speed_x = SCREEN_WIDTH * 0.007
        ball_speed_y = ball_speed_x
        ball_rigth = True

        UP = "up"
        DOWN = "down"
        STOP = "stop"
        motion_1 = STOP
        motion_2 = STOP

        point_1 = 0
        point_2 = 0

        win_1 = False
        win_2 = False

        touch_racket = 0

        font1 = pygame.font.SysFont(None, 72, True, False)

        FPS = 60
        clock = pygame.time.Clock()

        while True:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.VIDEORESIZE:
                    WINDOW_SIZE = (surface.get_width(), surface.get_height())
                    SCREEN_WIDTH = surface.get_width()
                    SCREEN_HEIGHT = surface.get_height()

                    ball_speed_x = SCREEN_WIDTH * 0.007
                    ball_speed_y = ball_speed_x
                    racket_h_1 = SCREEN_HEIGHT * 0.1
                    racket_h_2 = SCREEN_HEIGHT * 0.1
                    ball_r = SCREEN_WIDTH * SCREEN_HEIGHT * 0.00003

                    BACKGROUND_IMAGE = pygame.transform.scale(BACKGROUND_IMAGE, WINDOW_SIZE)
        
                # Control player 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        motion_1 = UP
                    if event.key == pygame.K_DOWN:
                        motion_1 = DOWN
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_UP, pygame.K_DOWN]:
                        motion_1 = STOP
                # Control player 2
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        motion_2 = UP
                    if event.key == pygame.K_s:
                        motion_2 = DOWN
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_w, pygame.K_s]:
                        motion_2 = STOP
        
            if motion_1 == UP:
                if racket_pos_1 > 0:
                    racket_pos_1 -= speed_rkt
            if motion_1 == DOWN:
                if (racket_pos_1 + racket_h_1) < SCREEN_HEIGHT:
                    racket_pos_1 += speed_rkt
            if motion_2 == UP:
                if racket_pos_2 > 0:
                    racket_pos_2 -= speed_rkt
            if motion_2 == DOWN:
                if (racket_pos_2 + racket_h_2) < SCREEN_HEIGHT:
                    racket_pos_2 += speed_rkt

            if ball_x + ball_r >= SCREEN_WIDTH:
                ball_speed_x = -ball_speed_x
                ball_x = SCREEN_WIDTH / 2
                ball_y = SCREEN_HEIGHT / 2
                racket_pos_1 = SCREEN_HEIGHT / 2 - (SCREEN_HEIGHT * 0.05)
                racket_pos_2 = SCREEN_HEIGHT / 2 - (SCREEN_HEIGHT * 0.05)
                ball_speed_x = -SCREEN_WIDTH * 0.007
                ball_speed_y = ball_speed_x
                touch_racket = 0
                point_1 += 1
            if ball_x - ball_r <= 0:
                ball_speed_x = -ball_speed_x
                ball_x = SCREEN_WIDTH / 2
                ball_y = SCREEN_HEIGHT / 2
                racket_pos_1 = SCREEN_HEIGHT / 2 - (SCREEN_HEIGHT * 0.05)
                racket_pos_2 = SCREEN_HEIGHT / 2 - (SCREEN_HEIGHT * 0.05)
                ball_speed_x = SCREEN_WIDTH * 0.007
                ball_speed_y = ball_speed_x
                touch_racket = 0
                point_2 += 1

            if ball_y + ball_r >= SCREEN_HEIGHT:
                ball_speed_y = -ball_speed_y
            if ball_y - ball_r <= 0:
                ball_speed_y = -ball_speed_y

            if (ball_x + ball_r) > SCREEN_WIDTH - (SCREEN_WIDTH * 0.02) and (ball_y > racket_pos_1 and ball_y < racket_pos_1 + racket_h_1):
                ball_speed_x = -ball_speed_x
                touch_racket += 1
            if (ball_x - ball_r) < SCREEN_WIDTH * 0.02 and (ball_y > racket_pos_2 and ball_y + ball_r < racket_pos_2 + racket_h_2):
                ball_speed_x = -ball_speed_x
                touch_racket += 1

            if touch_racket >= 5:
                ball_speed_x = SCREEN_WIDTH * 0.01
                ball_speed_y = ball_speed_x

            if point_1 == 5:
                return 1
            if point_2 == 5:
                return 2

            ball_x = ball_x + ball_speed_x
            ball_y = ball_y + ball_speed_y

            text = f"{point_1} : {point_2}"
            text_r = font1.render(text, True, (0, 0, 0))
            text_width, text_height = font1.size(text)
            screen.fill([0, 0, 0])
            screen.blit(BACKGROUND_IMAGE, (0, 0))
            screen.blit(text_r, (SCREEN_WIDTH / 2 - text_width / 2, 10))
            pygame.draw.rect(screen, (0, 0, 0), [SCREEN_WIDTH - (SCREEN_WIDTH * 0.02), racket_pos_1, SCREEN_WIDTH * 0.02, racket_h_1])
            pygame.draw.rect(screen, (0, 0, 0), [0, racket_pos_2, SCREEN_WIDTH * 0.02, racket_h_2])
            pygame.draw.circle(screen, (255, 255, 0), [ball_x, ball_y], ball_r)

            pygame.display.flip()