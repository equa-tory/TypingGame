import random
import sys

import pygame


def select_word():
    word_list = [
        'apple',
        'banana',
        'cherry',
        'melon',
        'orange'
    ]

    num_of_elements = len(word_list)
    i = random.randint(0, num_of_elements - 1)
    return word_list[i]


def cut_head_char(word):
    return word[1:]


def is_empty_word(word):
    return not word

def run_game():
    pygame.init()
    

    screen = pygame.display.set_mode((720, 480))
    font_big = pygame.font.SysFont(None, 64)
    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    word = select_word()
    max_score = 0
    score = 0
    pos_x = -150
    pos_y = random.randint(200, 400)
    speed = 0.2


    f = open('save.data', 'r')
    max_score = int(f.read())
    f.close()

    while True:
        screen.fill((200, 200, 200))

        score_text = my_font.render(f'Score: {score}', False, (0, 0, 0))
        screen.blit(score_text, (0,20))
        max_score_text = my_font.render(f'Max Score: {max_score}', False, (0, 0, 0))
        screen.blit(max_score_text, (0,0))

        sf_word = font_big.render(word, True, (0, 0, 0))
        center_x = screen.get_rect().width / 2 - sf_word.get_rect().width / 2
        screen.blit(sf_word, (pos_x, pos_y))
        
        if(pos_x<0): pos_x += 0.6
        elif(pos_x>750):
            score -= 1
            pos_y = random.randint(200, 400)
            pos_x = -150
            speed -= 0.02
            word = select_word()
        else: pos_x += speed

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()


                    f = open('save.data', 'w+')
                    f.write(str(max_score))
                    f.close()
                    return
                
            if event.type == pygame.KEYDOWN:
                if chr(event.key) == word[0]:
                    word = cut_head_char(word)
                    if is_empty_word(word):
                        if(score>=max_score): max_score+=1
                        score+=1
                        pos_y = random.randint(200, 400)
                        pos_x = -150
                        speed += 0.02
                        word = select_word()

run_game()
