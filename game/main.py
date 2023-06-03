import pygame

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1068, 530))
pygame.display.set_caption("Marouska's game")
icon = pygame.image.load('images/icon.png').convert_alpha()
pygame.display.set_icon(icon)

bg = pygame.image.load('images/bg.png').convert_alpha()
walk_right = [
    pygame.image.load('images/2.png').convert_alpha(),
    pygame.image.load('images/3.png').convert_alpha(),
    pygame.image.load('images/4.png').convert_alpha(),
    pygame.image.load('images/5.png').convert_alpha(),
    pygame.image.load('images/6.png').convert_alpha(),
    pygame.image.load('images/5.png').convert_alpha()
]

ghost = pygame.image.load('images/ghost.png').convert_alpha()
ghost_list_in_game = []

player_anim_count =0
bg_x = 0

player_speed = 5
player_x = 150
player_y = 295

is_jump = False
jump_count = 9

# bg_sound = pygame.mixer.Sound('sounds/bg.mp3')
# bg_sound.play()

ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 4000)

label = pygame.font.Font('fonts/Roboto-Italic.ttf', 40)
lose_label = label.render('Вы проиграли!', True, (193,196,199))
restart_label = label.render('Играть заново',True, (115,132,148))
restart_label_rect = restart_label.get_rect(topleft=(400,300))

gameplay = True

running = True
while running:

    screen.blit(bg, (bg_x, 0))
    screen.blit(bg, (bg_x + 1068, 0))

    if gameplay:

        player_rect = walk_right[0].get_rect(topleft=(player_x, player_y))

        if ghost_list_in_game:
            for (i, el) in enumerate(ghost_list_in_game):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < -10:
                    ghost_list_in_game.pop(i)

                if player_rect.colliderect(el):
                    gameplay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))
        else:
            screen.blit(walk_right[player_anim_count], (player_x, player_y))

        if keys[pygame.K_LEFT] and player_x > 50:
            player_x -= player_speed
        elif keys[pygame.K_RIGHT] and player_x < 600:
            player_x += player_speed

        if not is_jump:
            if keys[pygame.K_UP]:
                is_jump = True
        else:
            if jump_count >= -9:
                if jump_count > 0:
                    player_y -= (jump_count ** 2) / 1.5
                else:
                    player_y += (jump_count ** 2) / 1.5
                jump_count -= 1
            else:
                is_jump = False
                jump_count = 9

        if player_anim_count == 5:
            player_anim_count = 0
        else:
            player_anim_count += 1

        bg_x -= 3
        if bg_x == -1068:
            bg_x = 0

    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (400, 200 ))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            player_x = 150
            ghost_list_in_game.clear()

    pygame.display.update()
    clock.tick(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_in_game.append(ghost.get_rect(topleft=(1100, 330)))
