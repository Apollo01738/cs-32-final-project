import pygame, random

def ball_movement(ball, screen_height, screen_width, player, opponent, ball_speed_x, ball_speed_y, player_score, opponent_score):
	
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
	
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

	# Player Score
    if ball.left <= 0: 
        ball, ball_speed_x, ball_speed_y = ball_start(ball, screen_width, screen_height, ball_speed_x, ball_speed_y)
        player_score += 1
                
    # Opponent Score
    if ball.right >= screen_width:
        ball, ball_speed_x, ball_speed_y = ball_start(ball, screen_width, screen_height, ball_speed_x, ball_speed_y)
        opponent_score += 1
    return ball_speed_x, ball_speed_y, ball, player_score, opponent_score

    
    

def player_movement(player, player_speed, screen_height):
    player.y += player_speed

    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
    return player, player_speed

def opponent_movement(opponent, opponent_speed, ball, screen_height):
    if opponent.top < ball.y:
        opponent.y += opponent_speed
    if opponent.bottom > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height
    return opponent, opponent_speed

def ball_start(ball, screen_width, screen_height, ball_speed_x, ball_speed_y):
    ball.center = (screen_width/2, screen_height/2)
    ball_speed_y *= random.choice((1,-1))
    ball_speed_x *= random.choice((1,-1))
    return ball, ball_speed_x, ball_speed_y


def tennis_main():
    # General setup
    pygame.init()
    clock = pygame.time.Clock()

    # Main Window
    screen_width = 1280
    screen_height = 760
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Tennis')

    # Colors
    dark_grey = (75,75,75)
    background_color = pygame.Color('cyan4')

    # Game Rectangles (all the objects: ball, paddles)
    ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
    player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
    opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)

    # Game Variables
    ball_speed_x = 7 * random.choice((1,-1))
    ball_speed_y = 7 * random.choice((1,-1))
    player_speed = 0
    opponent_speed = 15

    # Score Text
    player_score = 0
    opponent_score = 0
    basic_font = pygame.font.Font('freesansbold.ttf', 32)

    # To keep the code and the window running
    running = True

    # To track when to cause the game to wait before playing
    wait_counter = 1

    # To determine how many coins to give the player
    won = False

    # The game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False       
            while player_score < 5 and opponent_score < 5 and running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_UP:
                            player_speed -= 6
                        if event.key == pygame.K_DOWN:
                            player_speed += 6
                    if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                            player_speed += 6
                        if event.key == pygame.K_DOWN:
                            player_speed -= 6
                
                #Game Play Systems
                ball_speed_x, ball_speed_y, ball, player_score, opponent_score = ball_movement(ball, screen_height, screen_width, player, opponent, ball_speed_x, ball_speed_y, player_score, opponent_score)
                player, player_speed = player_movement(player, player_speed, screen_height)
                opponent, opponent_speed = opponent_movement(opponent, opponent_speed, ball, screen_height)

                #Objects/animations
                screen.fill(background_color)
                pygame.draw.rect(screen, dark_grey, player)
                pygame.draw.rect(screen, dark_grey, opponent)
                pygame.draw.ellipse(screen, dark_grey, ball)
                pygame.draw.aaline(screen, dark_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))

                # Win directions
                instruction_text = basic_font.render(f'{"First to 5 wins!!!"}',False,dark_grey)
                screen.blit(instruction_text,(520,70))
                
                # Showing scores
                player_text = basic_font.render(f'{player_score}',False,dark_grey)
                screen.blit(player_text,(660,470))

                opponent_text = basic_font.render(f'{opponent_score}',False,dark_grey)
                screen.blit(opponent_text,(600,470))

                #Showing what's on the terminal
                pygame.display.flip()
                clock.tick(80)

                if wait_counter == 1:
                    # To delay the start for a bit while user acclimates
                    pygame.time.delay(1500)
                    wait_counter += 1
            

            if player_score == 5:
                # Resets the screen to show winner, but mimics the game visuals
                screen = pygame.display.set_mode((screen_width,screen_height))
                pygame.display.set_caption('Tennis')
                screen.fill(background_color)
                ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
                player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
                opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)
                pygame.draw.rect(screen, dark_grey, player)
                pygame.draw.rect(screen, dark_grey, opponent)
                pygame.draw.ellipse(screen, dark_grey, ball)
                pygame.draw.aaline(screen, (115,115,115), (screen_width / 2, 0),(screen_width / 2, screen_height))
                
                # Celebratory Text
                win_text = basic_font.render(f'{"YOU WIN!!!!"}',False,dark_grey)
                screen.blit(win_text,(550,70))
                pygame.display.flip()
                clock.tick(80)
                player_score += 1

                # Change the result variable to player winning
                won = True
                

            if opponent_score == 5:
                # Resets the screen to show that you lost, but mimics the game visuals
                screen = pygame.display.set_mode((screen_width,screen_height))
                pygame.display.set_caption('Tennis')
                screen.fill(background_color)
                ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
                player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
                opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)
                pygame.draw.rect(screen, dark_grey, player)
                pygame.draw.rect(screen, dark_grey, opponent)
                pygame.draw.ellipse(screen, dark_grey, ball)
                pygame.draw.aaline(screen, (115,115,115), (screen_width / 2, 0),(screen_width / 2, screen_height))
                
                # Loss Text
                loss_text = basic_font.render(f'{"Sorry champ, you lost :("}',False,dark_grey)
                screen.blit(loss_text,(450,70))
                pygame.display.flip()
                clock.tick(80)
                opponent_score += 1

    pygame.quit()
    return won



        
        

if __name__ == '__main__':
    tennis_main()
