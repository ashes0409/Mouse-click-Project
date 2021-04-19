import pygame
import random
from math import hypot, floor
from gradients import horizontal

# Initialize
pygame.init()
screen = pygame.display.set_mode((1080, 780))
pygame.display.set_caption("Mouse Reaction Test")

# Start values
x, y = 450, 450
color = (32, 64, 128)
screen_color = (255, 255, 255)
start_check, running, end_check = True, True, False
total_time, avg_time, count, fastest_time = 0, 0, 0, 0
start_time, last_click_time, this_click_time, this_click_time_taken = 0, 0, 0, 0
no_mistakes, force, hard_to_find = False, False, False
font = pygame.font.Font('gadugib.ttf', 25)
start_font = pygame.font.Font('gadugi.ttf', 60)
start_button_text = start_font.render("Start", True, (63, 127, 255))
restart_button_text = start_font.render("Restart", True, (63, 127, 255))
mode_font = pygame.font.Font('gadugib.ttf', 35)
reset_text = font.render("To stop click outside boundaries", True, (32, 64, 128))
no_mistakes_button_text_true = mode_font.render("No mistakes: ON", True, (32, 64, 128))
no_mistakes_button_text_false = mode_font.render("No mistakes: OFF", True, (32, 64, 128))
force_button_text_true = mode_font.render("Force: ON", True, (32, 64, 128))
force_button_text_false = mode_font.render("Force: OFF", True, (32, 64, 128))
hard_mode_button_text_true = mode_font.render("Hard mode: ON", True, (32, 64, 128))
hard_mode_button_text_false = mode_font.render("Hard mode: OFF", True, (32, 64, 128))
force_type = 0


def reset():
    global total_time, avg_time, count, fastest_time
    global start_time, last_click_time, this_click_time, this_click_time_taken
    global no_mistakes, force, hard_to_find
    total_time, avg_time, count, fastest_time = 0, 0, 0, 0
    start_time, last_click_time, this_click_time, this_click_time_taken = 0, 0, 0, 0
    no_mistakes, force, hard_to_find = False, False, False


def set_circle_properties():
    global screen_color, color, x, y, force_type
    color = (random.randint(0, 128), random.randint(0, 255), random.randint(128, 255))
    screen_color = (9 * color[0] // 10, 9 * color[1] // 10, 9 * color[2] // 10)
    x, y = random.randint(100, 950), random.randint(100, 650)
    force_type = random.randint(-1, 1)


def hard_to_find_mode():
    pygame.draw.rect(screen, screen_color, (60, 60, 960, 660))


def force_mode():
    global y
    if force_type == 1 or force_type == -1:
        time = pygame.time.get_ticks() - last_click_time
        y += force_type * floor(time * time * 0.000005)
        if force_type == 1:
            y = min(y, 695)
        if force_type == -1:
            y = max(y, 85)


def show_base_screen():
    screen.blit(horizontal((1100, 780), (200, 245, 255, 100), (255, 245, 255, 100)), (0, 0))
    pygame.draw.lines(screen, (0, 0, 0), True, [(60, 60), (1020, 60), (1020, 720), (60, 720)], 5)
    show_average_card = font.render("Average time : " + str(avg_time) + "ms", True, (32, 64, 128))
    show_min_card = font.render("Fastest time : " + str(fastest_time) + "ms", True, (32, 64, 128))
    show_count_card = font.render("Count : " + str(count), True, (32, 64, 128))
    show_last_click_time_card = font.render("Last : " + str(this_click_time_taken) + "ms", True, (32, 64, 128))
    screen.blit(show_average_card, (60, 25))
    screen.blit(show_min_card, (360, 25))
    screen.blit(show_count_card, (660, 25))
    screen.blit(show_last_click_time_card, (860, 25))


def no_mistakes_box():
    pygame.draw.rect(screen, (200, 255, 100), (370, 230, 340, 65))
    if no_mistakes:
        screen.blit(no_mistakes_button_text_true, (395, 237))
    else:
        screen.blit(no_mistakes_button_text_false, (395, 237))


def force_box():
    pygame.draw.rect(screen, (200, 255, 100), (370, 300, 340, 65))
    if force:
        screen.blit(force_button_text_true, (395, 307))
    else:
        screen.blit(force_button_text_false, (395, 307))


def hard_to_find_box():
    pygame.draw.rect(screen, (200, 255, 100), (370, 370, 340, 65))
    if hard_to_find:
        screen.blit(hard_mode_button_text_true, (395, 377))
    else:
        screen.blit(hard_mode_button_text_false, (395, 377))


def show_start_screen():
    show_base_screen()
    pygame.draw.rect(screen, (155, 255, 0), (470, 160, 140, 65))
    screen.blit(start_button_text, (475, 150))
    no_mistakes_box()
    force_box()
    hard_to_find_box()


def show_end_screen():
    show_base_screen()
    pygame.draw.rect(screen, (155, 255, 0), (440, 360, 200, 65))
    screen.blit(restart_button_text, (445, 350))


def show_running_screen():
    show_base_screen()
    screen.blit(reset_text, (340, 730))
    if hard_to_find:
        hard_to_find_mode()
    if force:
        force_mode()
    pygame.draw.circle(screen, color, (x, y), 25)


while running:
    if start_check:
        show_start_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 475 < mouse_x < 605 and 165 < mouse_y < 220:
                        start_check = False
                        end_check = False
                        set_circle_properties()
                        start_time = pygame.time.get_ticks()
                        last_click_time = start_time
                    elif 375 < mouse_x < 705 and 235 < mouse_y < 290:
                        no_mistakes = not no_mistakes
                    elif 375 < mouse_x < 705 and 305 < mouse_y < 360:
                        force = not force
                    elif 375 < mouse_x < 705 and 375 < mouse_y < 430:
                        hard_to_find = not hard_to_find

    elif end_check:
        show_end_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if 445 < mouse_x < 795 and 365 < mouse_y < 420:
                        start_check = True
                        reset()

    else:
        show_running_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if hypot(mouse_x - x, mouse_y - y) < 25:
                        this_click_time = pygame.time.get_ticks()
                        count += 1
                        avg_time = floor((this_click_time - start_time) / count)
                        this_click_time_taken = this_click_time - last_click_time
                        if fastest_time == 0:
                            fastest_time = this_click_time_taken
                        else:
                            fastest_time = min(fastest_time, this_click_time_taken)
                        last_click_time = this_click_time
                        set_circle_properties()
                    elif no_mistakes is True:
                        end_check = True
                    elif mouse_x > 1020 or mouse_x < 60 or mouse_y < 60 or mouse_y > 720:
                        end_check = True

    pygame.display.update()
