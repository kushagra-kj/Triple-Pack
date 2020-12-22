from colors import *
from images import *
import pygame
import random

pygame.init()

################################################# SCREEN SETTINGS ######################################################

window_width = 608
window_height = 704
game_disp = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Triple Pac(k)")
clock = pygame.time.Clock()


def draw_menuImg(menuImg_x, menuImg_y):
    game_disp.blit(menu_img, (menuImg_x, menuImg_y))


def write_text(text, scr, pos, fsize, fcol, fname, center=True):
    font = pygame.font.Font(fname, fsize)
    scrtext = font.render(text, False, fcol)
    textsize = scrtext.get_size()
    if center:
        pos[0] -= textsize[0] // 2
        pos[1] -= textsize[1] // 2
    scr.blit(scrtext, pos)


################################################## MENU SCREEN #########################################################

def menu_scr():
    global next_scr
    menuImg_x = (window_width * 0.45)
    menuImg_y = (window_height * 0.30)
    change_menu_x = 5
    change_menu_y = 0
    end = False

    while not end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    next_scr = "Tom & Jerry"
                    end = True
                elif event.key == pygame.K_2:
                    next_scr = "Christmas"
                    end = True
                elif event.key == pygame.K_3:
                    next_scr = "Halloween"
                    end = True

        game_disp.fill(navy_blue)
        draw_menuImg(menuImg_x, menuImg_y)
        menuImg_x += change_menu_x
        if menuImg_x > window_width - 128:
            change_menu_x = -5
        if menuImg_x < 0:
            change_menu_x = 5
        write_text("TRIPLE PAC(K)", game_disp, [window_width // 2, window_height // 6], 72, white, 'Sunday Morning.ttf')
        write_text("Tom & Jerry (PRESS 1)", game_disp, [window_width // 2, window_height // 2], 54, white, 'Bright Orchid.ttf')
        write_text("Christmas (PRESS 2)", game_disp, [window_width // 2, window_height // 2 + 70], 54, black, 'Bright Orchid.ttf')
        write_text("Halloween (PRESS 3)", game_disp, [window_width // 2, window_height // 2 + 140], 54, white,
                   'Bright Orchid.ttf')
        write_text("How to Play ?", game_disp, [window_width // 2, window_height // 2 + 210], 48, black,
                   'Bright Orchid.ttf')
        write_text("Developed by Kalash Kankaria, Kushagra Jain and Mann Jain", game_disp, [0, window_height - 20],
                   25, black, 'Almond Nougat.ttf', False)
        pygame.display.update()
        clock.tick(30)
    return next_scr

############################################### T&J INTRO SCREEN #######################################################

def t1_scr():
    global next_scr
    end = False
    while not end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    next_scr = "ghosts_3"
                    end = True
                elif event.key == pygame.K_2:
                    next_scr = "ghosts_4"
                    end = True

        game_disp.fill(grey)
        write_text("Tom & Jerry", game_disp, [window_width // 2, window_height // 6], 70, navy_blue,
                   'Sunday Morning.ttf')
        write_text("3 Ghosts (PRESS 1)", game_disp, [window_width // 2, window_height // 2], 54, black, 'Bright Orchid.ttf')
        write_text("4 Ghosts (PRESS 2)", game_disp, [window_width // 2, window_height // 2 + 140], 54, black, 'Bright Orchid.ttf')
        pygame.display.update()
        clock.tick(30)
    return next_scr

############################################ CHIRSTMAS INTRO SCREEN ####################################################

def t2_scr():
    global next_scr
    end = False
    while not end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    next_scr = "ghosts_3"
                    end = True
                elif event.key == pygame.K_2:
                    next_scr = "ghosts_4"
                    end = True

        game_disp.fill(salmon)
        write_text("Christmas", game_disp, [window_width // 2, window_height // 6], 70, white, 'Sunday Morning.ttf')
        write_text("3 Ghosts (PRESS 1)", game_disp, [window_width // 2, window_height // 2], 54, black, 'Bright Orchid.ttf')
        write_text("4 Ghosts (PRESS 2)", game_disp, [window_width // 2, window_height // 2 + 140], 54, black, 'Bright Orchid.ttf')
        pygame.display.update()
        clock.tick(30)
    return next_scr

############################################ HALLOWEEN INTRO SCREEN ####################################################

def t3_scr():
    global next_scr
    end = False
    while not end:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    next_scr = "ghosts_3"
                    end = True
                elif event.key == pygame.K_2:
                    next_scr = "ghosts_4"
                    end = True

        game_disp.fill(tom_jerry_bg)
        write_text("Halloween", game_disp, [window_width // 2, window_height // 6], 70, salmon, 'Sunday Morning.ttf')
        write_text("3 Ghosts (PRESS 1)", game_disp, [window_width // 2, window_height // 2], 54, black, 'Bright Orchid.ttf')
        write_text("4 Ghosts (PRESS 2)", game_disp, [window_width // 2, window_height // 2 + 140], 54, black, 'Bright Orchid.ttf')
        pygame.display.update()
        clock.tick(30)
    return next_scr

############################################ T&J 3GHOST PLAY SCREEN ####################################################

def tomjerry_ghosts_3():
    maze_matrix = [[1] * 19] * 22
    maze_row = 22
    maze_col = 19
    pixel_size = 32
    img_pixel = 24
    score = -10
    player_x = 9
    player_y = 16
    change_x = 0
    change_y = 0
    ghost1_x = 9
    ghost1_y = 9
    ghost1_x_change = 0
    ghost1_y_change = 2
    ghost2_x = 9
    ghost2_y = 9
    ghost3_x = 9
    ghost3_y = 9
    score_font = pygame.font.Font("Bright Orchid.ttf", 32)

    maze_matrix = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 2, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1],
        [1, 2, 2, 1, 0, 1, 2, 1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 2, 1],
        [1, 2, 2, 1, 0, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 2, 2, 1],
        [1, 2, 2, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 2, 1],
        [1, 2, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1],
        [1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    ######################################## FUNCTIONS ########################################

    def draw_character(name, coor):
        game_disp.blit(name, coor)

    def get_dimensional_coordinates(x, y):
        x = x * pixel_size + int((pixel_size - img_pixel) / 2)
        y = y * pixel_size + int((pixel_size - img_pixel) / 2)
        return (x, y)

    def draw_maze():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 1:
                    game_disp.blit(wall_tj, (j * pixel_size, i * pixel_size))

    def draw_corners():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 3:
                    game_disp.blit(corner_tj, (j * pixel_size, i * pixel_size))

    def draw_item():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    game_disp.blit(item_tj, (get_dimensional_coordinates(j, i)))

    def calculate_score(score, x, y):
        if maze_matrix[y][x] == 0:
            score = score + 10
            maze_matrix[y][x] = 2
        return score

    def isObstacle(x, y):
        if maze_matrix[y][x] == 0 or maze_matrix[y][x] == 2:
            return False
        return True

    def position_valid(x, y):
        if isObstacle(x, y):
            return False
        elif x < 1 or x > maze_col:
            return False
        elif y < 1 or y > maze_row:
            return False
        return True

    def print_score(score):
        scorecard = score_font.render("Score : " + str(score), True, white)
        game_disp.blit(scorecard, (0, 0))

    def kill(ghost1_x, ghost1_y, player_x, player_y):
        if ghost1_x == player_x and ghost1_y == player_y:
            return True
        else:
            return False

    def win_condition():
        global result
        flag = 0
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    flag = 1
                    result = False
                    break
        if flag == 0:
            result = True
        return result

    ######################################## ENEMIES ########################################

    ###################### GHOST1 ######################

    def ghost1(ghost1_x, ghost1_y, kill=False):
        global ghost1_x_change, ghost1_y_change
        if kill:
            return ghost1_x, ghost1_y
        move = random.randint(1, 4)

        if move == 1:
            ghost1_y_change = 0
            ghost1_x_change = -1
        elif move == 2:
            ghost1_y_change = 0
            ghost1_x_change = 1
        elif move == 3:
            ghost1_x_change = 0
            ghost1_y_change = -1
        elif move == 4:
            ghost1_x_change = 0
            ghost1_y_change = 1

        if not position_valid(ghost1_x + ghost1_x_change, ghost1_y + ghost1_y_change):
            ghost1_x_change = 0
            ghost1_y_change = 0
        ghost1_x += ghost1_x_change
        ghost1_y += ghost1_y_change

        return ghost1_x, ghost1_y

    ######################################## GAME LOOP ########################################

    end = False
    while not end:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -1
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = 1
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_x = 0
                    change_y = -1
                elif event.key == pygame.K_DOWN:
                    change_x = 0
                    change_y = 1

        game_disp.fill(green)
        draw_maze()
        draw_item()
        draw_corners()
        draw_character(player_tj, get_dimensional_coordinates(player_x, player_y))
        draw_character(ghost1_img_tj, get_dimensional_coordinates(ghost1_x, ghost1_y))
        draw_character(ghost2_img_tj, get_dimensional_coordinates(ghost2_x, ghost2_y))
        draw_character(ghost3_img_tj, get_dimensional_coordinates(ghost3_x, ghost3_y))
        ghost1_x, ghost1_y = ghost1(ghost1_x, ghost1_y, kill(ghost1_x, ghost1_y, player_x, player_y))
        ghost2_x, ghost2_y = ghost1(ghost2_x, ghost2_y, kill(ghost2_x, ghost2_y, player_x, player_y))
        ghost3_x, ghost3_y = ghost1(ghost3_x, ghost3_y, kill(ghost3_x, ghost3_y, player_x, player_y))

        if not position_valid(player_x + change_x, player_y + change_y):
            change_x = 0
            change_y = 0
        player_x += change_x
        player_y += change_y
        if kill(ghost1_x, ghost1_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, black, 'Bright Orchid.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if kill(ghost2_x, ghost2_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, black, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if kill(ghost3_x, ghost3_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, black, 'Sunday Morning.ttf')

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if win_condition():
            write_text("YOU WIN !", game_disp, [window_width // 2, window_height // 2], 90, red, 'Bright Orchid.ttf')

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        score = calculate_score(score, player_x, player_y)
        print_score(score)
        pygame.display.update()
        clock.tick(8)

############################################ T&J 4GHOST PLAY SCREEN ####################################################

def tomjerry_ghosts_4():
    maze_matrix = [[1] * 19] * 22
    maze_row = 22
    maze_col = 19
    pixel_size = 32
    img_pixel = 24
    score = -10
    player_x = 9
    player_y = 16
    change_x = 0
    change_y = 0
    ghost1_x = 9
    ghost1_y = 9
    ghost1_x_change = 0
    ghost1_y_change = 2
    ghost2_x = 9
    ghost2_y = 9
    ghost3_x = 9
    ghost3_y = 9
    ghost4_x = 9
    ghost4_y = 9
    score_font = pygame.font.Font("Bright Orchid.ttf", 32)

    maze_matrix = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 2, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1],
        [1, 2, 2, 1, 0, 1, 2, 1, 1, 2, 1, 1, 2, 1, 0, 1, 2, 2, 1],
        [1, 2, 2, 1, 0, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 1, 2, 2, 1],
        [1, 2, 2, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 2, 2, 1],
        [1, 2, 2, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 1],
        [1, 1, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    ######################################## FUNCTIONS ########################################

    def draw_character(name, coor):
        game_disp.blit(name, coor)

    def get_dimensional_coordinates(x, y):
        x = x * pixel_size + int((pixel_size - img_pixel) / 2)
        y = y * pixel_size + int((pixel_size - img_pixel) / 2)
        return (x, y)

    def draw_maze():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 1:
                    game_disp.blit(wall_tj, (j * pixel_size, i * pixel_size))

    def draw_corners():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 3:
                    game_disp.blit(corner_tj, (j * pixel_size, i * pixel_size))

    def draw_item():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    game_disp.blit(item_tj, (get_dimensional_coordinates(j, i)))

    def calculate_score(score, x, y):
        if maze_matrix[y][x] == 0:
            score = score + 10
            maze_matrix[y][x] = 2
        return score

    def isObstacle(x, y):
        if maze_matrix[y][x] == 0 or maze_matrix[y][x] == 2:
            return False
        return True

    def position_valid(x, y):
        if isObstacle(x, y):
            return False
        elif x < 1 or x > maze_col:
            return False
        elif y < 1 or y > maze_row:
            return False
        return True

    def print_score(score):
        scorecard = score_font.render("Score : " + str(score), True, white)
        game_disp.blit(scorecard, (0, 0))

    def kill(ghost1_x, ghost1_y, player_x, player_y):
        if ghost1_x == player_x and ghost1_y == player_y:
            return True
        else:
            return False

    def win_condition():
        global result
        flag = 0
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    flag = 1
                    result = False
                    break
        if flag == 0:
            result = True
        return result

    ######################################## ENEMIES ########################################

    ###################### GHOST1 ######################

    def ghost1(ghost1_x, ghost1_y, kill=False):
        global ghost1_x_change, ghost1_y_change
        if kill:
            return ghost1_x, ghost1_y
        move = random.randint(1, 4)

        if move == 1:
            ghost1_y_change = 0
            ghost1_x_change = -1
        elif move == 2:
            ghost1_y_change = 0
            ghost1_x_change = 1
        elif move == 3:
            ghost1_x_change = 0
            ghost1_y_change = -1
        elif move == 4:
            ghost1_x_change = 0
            ghost1_y_change = 1

        if not position_valid(ghost1_x + ghost1_x_change, ghost1_y + ghost1_y_change):
            ghost1_x_change = 0
            ghost1_y_change = 0
        ghost1_x += ghost1_x_change
        ghost1_y += ghost1_y_change

        return ghost1_x, ghost1_y

    ######################################## GAME LOOP ########################################

    end = False
    while not end:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -1
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = 1
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_x = 0
                    change_y = -1
                elif event.key == pygame.K_DOWN:
                    change_x = 0
                    change_y = 1

        game_disp.fill(green)
        draw_maze()
        draw_item()
        draw_corners()
        draw_character(player_tj, get_dimensional_coordinates(player_x, player_y))
        draw_character(ghost1_img_tj, get_dimensional_coordinates(ghost1_x, ghost1_y))
        draw_character(ghost2_img_tj, get_dimensional_coordinates(ghost2_x, ghost2_y))
        draw_character(ghost3_img_tj, get_dimensional_coordinates(ghost3_x, ghost3_y))
        draw_character(ghost4_img_tj, get_dimensional_coordinates(ghost4_x, ghost4_y))
        ghost1_x, ghost1_y = ghost1(ghost1_x, ghost1_y, kill(ghost1_x, ghost1_y, player_x, player_y))
        ghost2_x, ghost2_y = ghost1(ghost2_x, ghost2_y, kill(ghost2_x, ghost2_y, player_x, player_y))
        ghost3_x, ghost3_y = ghost1(ghost3_x, ghost3_y, kill(ghost3_x, ghost3_y, player_x, player_y))
        ghost4_x, ghost4_y = ghost1(ghost4_x, ghost4_y, kill(ghost4_x, ghost4_y, player_x, player_y))

        if not position_valid(player_x + change_x, player_y + change_y):
            change_x = 0
            change_y = 0
        player_x += change_x
        player_y += change_y
        if kill(ghost1_x, ghost1_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, black, 'Bright Orchid.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if kill(ghost2_x, ghost2_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, black, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if kill(ghost3_x, ghost3_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, black, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if kill(ghost4_x, ghost4_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, black, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if win_condition():
            write_text("YOU WIN !", game_disp, [window_width // 2, window_height // 2], 90, red, 'Bright Orchid.ttf')

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        score = calculate_score(score, player_x, player_y)
        print_score(score)
        pygame.display.update()
        clock.tick(60)

######################################### CHRISTMAS 3GHOST PLAY SCREEN #################################################

def christmas_ghosts_3():
    maze_matrix = [[1] * 19] * 22
    maze_row = 22
    maze_col = 19
    pixel_size = 32
    img_pixel = 24
    score = -10
    player_x = 9
    player_y = 16
    change_x = 0
    change_y = 0
    ghost1_x = 9
    ghost1_y = 10
    ghost1_x_change = 0
    ghost1_y_change = 2
    ghost2_x = 9
    ghost2_y = 10
    ghost3_x = 9
    ghost3_y = 10
    score_font = pygame.font.Font("Bright Orchid.ttf", 32)

    maze_matrix = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    ######################################## FUNCTIONS ########################################

    def draw_character(name, coor):
        game_disp.blit(name, coor)

    def get_dimensional_coordinates(x, y):
        x = x * pixel_size + int((pixel_size - img_pixel) / 2)
        y = y * pixel_size + int((pixel_size - img_pixel) / 2)
        return (x, y)

    def draw_maze():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 1:
                    game_disp.blit(wall_christmas, (j * pixel_size, i * pixel_size))

    def draw_corners():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 3:
                    game_disp.blit(corner_christmas, (j * pixel_size, i * pixel_size))

    def draw_item():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    game_disp.blit(item_christmas, (get_dimensional_coordinates(j, i)))

    def calculate_score(score, x, y):
        if maze_matrix[y][x] == 0:
            score = score + 10
            maze_matrix[y][x] = 2
        return score

    def isObstacle(x, y):
        if maze_matrix[y][x] == 0 or maze_matrix[y][x] == 2:
            return False
        return True

    def position_valid(x, y):
        if isObstacle(x, y):
            return False
        elif x < 1 or x > maze_col:
            return False
        elif y < 1 or y > maze_row:
            return False
        return True

    def print_score(score):
        scorecard = score_font.render("Score : " + str(score), True, white)
        game_disp.blit(scorecard, (0, 0))

    def kill(ghost1_x, ghost1_y, player_x, player_y):
        if ghost1_x == player_x and ghost1_y == player_y:
            return True
        else:
            return False

    def win_condition():
        global result
        flag = 0
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    flag = 1
                    result = False
                    break
        if flag == 0:
            result = True
        return result

    ######################################## ENEMIES ########################################

    ###################### GHOST1 ######################

    def ghost1(ghost1_x, ghost1_y, kill=False):
        global ghost1_x_change, ghost1_y_change
        if kill:
            return ghost1_x, ghost1_y
        move = random.randint(1, 4)

        if move == 1:
            ghost1_y_change = 0
            ghost1_x_change = -1
        elif move == 2:
            ghost1_y_change = 0
            ghost1_x_change = 1
        elif move == 3:
            ghost1_x_change = 0
            ghost1_y_change = -1
        elif move == 4:
            ghost1_x_change = 0
            ghost1_y_change = 1

        if not position_valid(ghost1_x + ghost1_x_change, ghost1_y + ghost1_y_change):
            ghost1_x_change = 0
            ghost1_y_change = 0
        ghost1_x += ghost1_x_change
        ghost1_y += ghost1_y_change

        return ghost1_x, ghost1_y

    ######################################## GAME LOOP ########################################

    end = False
    while not end:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -1
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = 1
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_x = 0
                    change_y = -1
                elif event.key == pygame.K_DOWN:
                    change_x = 0
                    change_y = 1

        game_disp.fill(black)
        draw_maze()
        draw_item()
        draw_corners()
        draw_character(player_christmas, get_dimensional_coordinates(player_x, player_y))
        draw_character(ghost1_img_christmas, get_dimensional_coordinates(ghost1_x, ghost1_y))
        draw_character(ghost2_img_christmas, get_dimensional_coordinates(ghost2_x, ghost2_y))
        draw_character(ghost3_img_christmas, get_dimensional_coordinates(ghost3_x, ghost3_y))
        ghost1_x, ghost1_y = ghost1(ghost1_x, ghost1_y, kill(ghost1_x, ghost1_y, player_x, player_y))
        ghost2_x, ghost2_y = ghost1(ghost2_x, ghost2_y, kill(ghost2_x, ghost2_y, player_x, player_y))
        ghost3_x, ghost3_y = ghost1(ghost3_x, ghost3_y, kill(ghost3_x, ghost3_y, player_x, player_y))

        if not position_valid(player_x + change_x, player_y + change_y):
            change_x = 0
            change_y = 0
        player_x += change_x
        player_y += change_y
        if kill(ghost1_x, ghost1_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, white, 'Sunday Morning.ttf')
        if kill(ghost2_x, ghost2_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, white, 'Sunday Morning.ttf')
        if kill(ghost3_x, ghost3_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, white, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if win_condition():
            write_text("YOU WIN !", game_disp, [window_width // 2, window_height // 2], 90, white, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        score = calculate_score(score, player_x, player_y)
        print_score(score)
        pygame.display.update()
        clock.tick(8)

######################################### CHRISTMAS 4GHOST PLAY SCREEN #################################################

def christmas_ghosts_4():
    maze_matrix = [[1] * 19] * 22
    maze_row = 22
    maze_col = 19
    pixel_size = 32
    img_pixel = 24
    score = -10
    player_x = 9
    player_y = 16
    change_x = 0
    change_y = 0
    ghost1_x = 9
    ghost1_y = 10
    ghost1_x_change = 0
    ghost1_y_change = 2
    ghost2_x = 9
    ghost2_y = 10
    ghost3_x = 9
    ghost3_y = 10
    ghost4_x = 9
    ghost4_y = 10
    score_font = pygame.font.Font("Bright Orchid.ttf", 32)

    maze_matrix = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    ######################################## FUNCTIONS ########################################

    def draw_character(name, coor):
        game_disp.blit(name, coor)

    def get_dimensional_coordinates(x, y):
        x = x * pixel_size + int((pixel_size - img_pixel) / 2)
        y = y * pixel_size + int((pixel_size - img_pixel) / 2)
        return (x, y)

    def draw_maze():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 1:
                    game_disp.blit(wall_christmas, (j * pixel_size, i * pixel_size))

    def draw_corners():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 3:
                    game_disp.blit(corner_christmas, (j * pixel_size, i * pixel_size))

    def draw_item():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    game_disp.blit(item_christmas, (get_dimensional_coordinates(j, i)))

    def calculate_score(score, x, y):
        if maze_matrix[y][x] == 0:
            score = score + 10
            maze_matrix[y][x] = 2
        return score

    def isObstacle(x, y):
        if maze_matrix[y][x] == 0 or maze_matrix[y][x] == 2:
            return False
        return True

    def position_valid(x, y):
        if isObstacle(x, y):
            return False
        elif x < 1 or x > maze_col:
            return False
        elif y < 1 or y > maze_row:
            return False
        return True

    def print_score(score):
        scorecard = score_font.render("Score : " + str(score), True, white)
        game_disp.blit(scorecard, (0, 0))

    def kill(ghost1_x, ghost1_y, player_x, player_y):
        if ghost1_x == player_x and ghost1_y == player_y:
            return True
        else:
            return False

    def win_condition():
        global result
        flag = 0
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    flag = 1
                    result = False
                    break
        if flag == 0:
            result = True
        return result

    ######################################## ENEMIES ########################################

    ###################### GHOST1 ######################

    def ghost1(ghost1_x, ghost1_y, kill=False):
        global ghost1_x_change, ghost1_y_change
        if kill:
            return ghost1_x, ghost1_y
        move = random.randint(1, 4)

        if move == 1:
            ghost1_y_change = 0
            ghost1_x_change = -1
        elif move == 2:
            ghost1_y_change = 0
            ghost1_x_change = 1
        elif move == 3:
            ghost1_x_change = 0
            ghost1_y_change = -1
        elif move == 4:
            ghost1_x_change = 0
            ghost1_y_change = 1

        if not position_valid(ghost1_x + ghost1_x_change, ghost1_y + ghost1_y_change):
            ghost1_x_change = 0
            ghost1_y_change = 0
        ghost1_x += ghost1_x_change
        ghost1_y += ghost1_y_change

        return ghost1_x, ghost1_y

    ######################################## GAME LOOP ########################################

    end = False
    while not end:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -1
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = 1
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_x = 0
                    change_y = -1
                elif event.key == pygame.K_DOWN:
                    change_x = 0
                    change_y = 1

        game_disp.fill(black)
        draw_maze()
        draw_item()
        draw_corners()
        draw_character(player_christmas, get_dimensional_coordinates(player_x, player_y))
        draw_character(ghost1_img_christmas, get_dimensional_coordinates(ghost1_x, ghost1_y))
        draw_character(ghost2_img_christmas, get_dimensional_coordinates(ghost2_x, ghost2_y))
        draw_character(ghost3_img_christmas, get_dimensional_coordinates(ghost3_x, ghost3_y))
        draw_character(ghost4_img_christmas, get_dimensional_coordinates(ghost4_x, ghost4_y))
        ghost1_x, ghost1_y = ghost1(ghost1_x, ghost1_y, kill(ghost1_x, ghost1_y, player_x, player_y))
        ghost2_x, ghost2_y = ghost1(ghost2_x, ghost2_y, kill(ghost2_x, ghost2_y, player_x, player_y))
        ghost3_x, ghost3_y = ghost1(ghost3_x, ghost3_y, kill(ghost3_x, ghost3_y, player_x, player_y))
        ghost4_x, ghost4_y = ghost1(ghost4_x, ghost4_y, kill(ghost4_x, ghost4_y, player_x, player_y))

        if not position_valid(player_x + change_x, player_y + change_y):
            change_x = 0
            change_y = 0
        player_x += change_x
        player_y += change_y
        if kill(ghost1_x, ghost1_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, white, 'Sunday Morning.ttf')
        if kill(ghost2_x, ghost2_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, white, 'Sunday Morning.ttf')
        if kill(ghost3_x, ghost3_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, white, 'Sunday Morning.ttf')

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if win_condition():
            write_text("YOU WIN !", game_disp, [window_width // 2, window_height // 2], 90, white, 'Sunday Morning.ttf')

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        score = calculate_score(score, player_x, player_y)
        print_score(score)
        pygame.display.update()
        clock.tick(8)

######################################### HALLOWEEN 3GHOST PLAY SCREEN #################################################

def halloween_ghosts_3():
    maze_matrix = [[1] * 19] * 22
    maze_row = 22
    maze_col = 19
    pixel_size = 32
    img_pixel = 24
    score = -10
    player_x = 9
    player_y = 16
    change_x = 0
    change_y = 0
    ghost1_x = 9
    ghost1_y = 9
    ghost1_x_change = 0
    ghost1_y_change = 2
    ghost2_x = 9
    ghost2_y = 9
    ghost3_x = 9
    ghost3_y = 9
    score_font = pygame.font.Font("Bright Orchid.ttf", 32)

    maze_matrix = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 1, 1, 2, 1, 1, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    ######################################## FUNCTIONS ########################################

    def draw_character(name, coor):
        game_disp.blit(name, coor)

    def get_dimensional_coordinates(x, y):
        x = x * pixel_size + int((pixel_size - img_pixel) / 2)
        y = y * pixel_size + int((pixel_size - img_pixel) / 2)
        return (x, y)

    def draw_maze():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 1:
                    game_disp.blit(wall_halloween, (j * pixel_size, i * pixel_size))

    def draw_corners():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 3:
                    game_disp.blit(corner_halloween, (j * pixel_size, i * pixel_size))

    def draw_item():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    game_disp.blit(item_halloween, (get_dimensional_coordinates(j, i)))

    def calculate_score(score, x, y):
        if maze_matrix[y][x] == 0:
            score = score + 10
            maze_matrix[y][x] = 2
        return score

    def isObstacle(x, y):
        if maze_matrix[y][x] == 0 or maze_matrix[y][x] == 2:
            return False
        return True

    def position_valid(x, y):
        if isObstacle(x, y):
            return False
        elif x < 1 or x > maze_col:
            return False
        elif y < 1 or y > maze_row:
            return False
        return True

    def print_score(score):
        scorecard = score_font.render("Score : " + str(score), True, white)
        game_disp.blit(scorecard, (0, 0))

    def kill(ghost1_x, ghost1_y, player_x, player_y):
        if ghost1_x == player_x and ghost1_y == player_y:
            return True
        else:
            return False

    def win_condition():
        global result
        flag = 0
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    flag = 1
                    result = False
                    break
        if flag == 0:
            result = True
        return result

    ######################################## ENEMIES ########################################

    ###################### GHOST1 ######################

    def ghost1(ghost1_x, ghost1_y, kill=False):
        global ghost1_x_change, ghost1_y_change
        if kill:
            return ghost1_x, ghost1_y
        move = random.randint(1, 4)

        if move == 1:
            ghost1_y_change = 0
            ghost1_x_change = -1
        elif move == 2:
            ghost1_y_change = 0
            ghost1_x_change = 1
        elif move == 3:
            ghost1_x_change = 0
            ghost1_y_change = -1
        elif move == 4:
            ghost1_x_change = 0
            ghost1_y_change = 1

        if not position_valid(ghost1_x + ghost1_x_change, ghost1_y + ghost1_y_change):
            ghost1_x_change = 0
            ghost1_y_change = 0
        ghost1_x += ghost1_x_change
        ghost1_y += ghost1_y_change

        return ghost1_x, ghost1_y

    ######################################## GAME LOOP ########################################

    end = False
    while not end:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -1
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = 1
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_x = 0
                    change_y = -1
                elif event.key == pygame.K_DOWN:
                    change_x = 0
                    change_y = 1

        game_disp.fill(black)
        draw_maze()
        draw_item()
        draw_corners()
        draw_character(player_halloween, get_dimensional_coordinates(player_x, player_y))
        draw_character(ghost1_img_halloween, get_dimensional_coordinates(ghost1_x, ghost1_y))
        draw_character(ghost2_img_halloween, get_dimensional_coordinates(ghost2_x, ghost2_y))
        draw_character(ghost3_img_halloween, get_dimensional_coordinates(ghost3_x, ghost3_y))
        ghost1_x, ghost1_y = ghost1(ghost1_x, ghost1_y, kill(ghost1_x, ghost1_y, player_x, player_y))
        ghost2_x, ghost2_y = ghost1(ghost2_x, ghost2_y, kill(ghost2_x, ghost2_y, player_x, player_y))
        ghost3_x, ghost3_y = ghost1(ghost3_x, ghost3_y, kill(ghost3_x, ghost3_y, player_x, player_y))

        if not position_valid(player_x + change_x, player_y + change_y):
            change_x = 0
            change_y = 0
        player_x += change_x
        player_y += change_y
        if kill(ghost1_x, ghost1_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, red, 'Sunday Morning.ttf')
        if kill(ghost2_x, ghost2_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, red, 'Sunday Morning.ttf')
        if kill(ghost3_x, ghost3_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, red, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if win_condition():
            write_text("YOU WIN !", game_disp, [window_width // 2, window_height // 2], 90, red, 'Bright Orchid.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        score = calculate_score(score, player_x, player_y)
        print_score(score)
        pygame.display.update()
        clock.tick(8)

######################################### HALLOWEEN 4GHOST PLAY SCREEN #################################################

def halloween_ghosts_4():
    maze_matrix = [[1] * 19] * 22
    maze_row = 22
    maze_col = 19
    pixel_size = 32
    img_pixel = 24
    score = -10
    player_x = 9
    player_y = 16
    change_x = 0
    change_y = 0
    ghost1_x = 9
    ghost1_y = 9
    ghost1_x_change = 0
    ghost1_y_change = 2
    ghost2_x = 9
    ghost2_y = 9
    ghost3_x = 9
    ghost3_y = 9
    ghost4_x = 9
    ghost4_y = 9
    score_font = pygame.font.Font("Bright Orchid.ttf", 32)

    maze_matrix = [
        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 2, 2, 1, 2, 2, 2, 1, 2, 2, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 2, 1, 1, 2, 1, 1, 2, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 2, 1, 1, 1, 1, 1, 2, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]

    ######################################## FUNCTIONS ########################################

    def draw_character(name, coor):
        game_disp.blit(name, coor)

    def get_dimensional_coordinates(x, y):
        x = x * pixel_size + int((pixel_size - img_pixel) / 2)
        y = y * pixel_size + int((pixel_size - img_pixel) / 2)
        return (x, y)

    def draw_maze():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 1:
                    game_disp.blit(wall_halloween, (j * pixel_size, i * pixel_size))

    def draw_corners():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 3:
                    game_disp.blit(corner_halloween, (j * pixel_size, i * pixel_size))

    def draw_item():
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    game_disp.blit(item_halloween, (get_dimensional_coordinates(j, i)))

    def calculate_score(score, x, y):
        if maze_matrix[y][x] == 0:
            score = score + 10
            maze_matrix[y][x] = 2
        return score

    def isObstacle(x, y):
        if maze_matrix[y][x] == 0 or maze_matrix[y][x] == 2:
            return False
        return True

    def position_valid(x, y):
        if isObstacle(x, y):
            return False
        elif x < 1 or x > maze_col:
            return False
        elif y < 1 or y > maze_row:
            return False
        return True

    def print_score(score):
        scorecard = score_font.render("Score : " + str(score), True, white)
        game_disp.blit(scorecard, (0, 0))

    def kill(ghost1_x, ghost1_y, player_x, player_y):
        if ghost1_x == player_x and ghost1_y == player_y:
            return True
        else:
            return False

    def win_condition():
        global result
        flag = 0
        for i in range(maze_row):
            for j in range(maze_col):
                if maze_matrix[i][j] == 0:
                    flag = 1
                    result = False
                    break
        if flag == 0:
            result = True
        return result

    ######################################## ENEMIES ########################################

    ###################### GHOST1 ######################

    def ghost1(ghost1_x, ghost1_y, kill=False):
        global ghost1_x_change, ghost1_y_change
        if kill:
            return ghost1_x, ghost1_y
        move = random.randint(1, 4)

        if move == 1:
            ghost1_y_change = 0
            ghost1_x_change = -1
        elif move == 2:
            ghost1_y_change = 0
            ghost1_x_change = 1
        elif move == 3:
            ghost1_x_change = 0
            ghost1_y_change = -1
        elif move == 4:
            ghost1_x_change = 0
            ghost1_y_change = 1

        if not position_valid(ghost1_x + ghost1_x_change, ghost1_y + ghost1_y_change):
            ghost1_x_change = 0
            ghost1_y_change = 0
        ghost1_x += ghost1_x_change
        ghost1_y += ghost1_y_change

        return ghost1_x, ghost1_y

    ######################################## GAME LOOP ########################################

    end = False
    while not end:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    change_x = -1
                    change_y = 0
                elif event.key == pygame.K_RIGHT:
                    change_x = 1
                    change_y = 0
                elif event.key == pygame.K_UP:
                    change_x = 0
                    change_y = -1
                elif event.key == pygame.K_DOWN:
                    change_x = 0
                    change_y = 1

        game_disp.fill(black)
        draw_maze()
        draw_item()
        draw_corners()
        draw_character(player_halloween, get_dimensional_coordinates(player_x, player_y))
        draw_character(ghost1_img_halloween, get_dimensional_coordinates(ghost1_x, ghost1_y))
        draw_character(ghost2_img_halloween, get_dimensional_coordinates(ghost2_x, ghost2_y))
        draw_character(ghost3_img_halloween, get_dimensional_coordinates(ghost3_x, ghost3_y))
        draw_character(ghost4_img_halloween, get_dimensional_coordinates(ghost4_x, ghost4_y))
        ghost1_x, ghost1_y = ghost1(ghost1_x, ghost1_y, kill(ghost1_x, ghost1_y, player_x, player_y))
        ghost2_x, ghost2_y = ghost1(ghost2_x, ghost2_y, kill(ghost2_x, ghost2_y, player_x, player_y))
        ghost3_x, ghost3_y = ghost1(ghost3_x, ghost3_y, kill(ghost3_x, ghost3_y, player_x, player_y))
        ghost4_x, ghost4_y = ghost1(ghost4_x, ghost4_y, kill(ghost4_x, ghost4_y, player_x, player_y))

        if not position_valid(player_x + change_x, player_y + change_y):
            change_x = 0
            change_y = 0
        player_x += change_x
        player_y += change_y
        if kill(ghost1_x, ghost1_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, red, 'Sunday Morning.ttf')
        if kill(ghost2_x, ghost2_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, red, 'Sunday Morning.ttf')
        if kill(ghost3_x, ghost3_y, player_x, player_y):
            write_text("GAME OVER", game_disp, [window_width // 2, window_height // 2], 90, black, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        if win_condition():
            write_text("YOU WIN !", game_disp, [window_width // 2, window_height // 2], 90, red, 'Sunday Morning.ttf')
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            change_x = 0
            change_y = 0
        score = calculate_score(score, player_x, player_y)
        print_score(score)
        pygame.display.update()
        clock.tick(8)


################################################## MAIN BODY ###########################################################

next_scr = menu_scr()
if next_scr == "Tom & Jerry":
    next_scr = t1_scr()
    if next_scr == "ghosts_3":
        tomjerry_ghosts_3()
    elif next_scr == "ghosts_4":
        tomjerry_ghosts_4()
elif next_scr == "Christmas":
    next_scr = t2_scr()
    if next_scr == "ghosts_3":
        christmas_ghosts_3()
    elif next_scr == "ghosts_4":
        christmas_ghosts_4()
elif next_scr == "Halloween":
    next_scr = t3_scr()
    if next_scr == "ghosts_3":
        halloween_ghosts_3()
    elif next_scr == "ghosts_4":
        halloween_ghosts_4()