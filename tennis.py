import pygame, sys, random

def ball_movement():
	global ball_speed_x, ball_speed_y, player_score, opponent_score
	
	ball.x += ball_speed_x
	ball.y += ball_speed_y

	if ball.top <= 0 or ball.bottom >= screen_height:
		ball_speed_y *= -1
	
	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1

	# Player Score
	if ball.left <= 0: 
		ball_start()
		player_score += 1

	# Opponent Score
	if ball.right >= screen_width:
		ball_start()
		opponent_score += 1

def player_movement():
	player.y += player_speed

	if player.top <= 0:
		player.top = 0
	if player.bottom >= screen_height:
		player.bottom = screen_height

def opponent_movement():
	if opponent.top < ball.y:
		opponent.y += opponent_speed
	if opponent.bottom > ball.y:
		opponent.y -= opponent_speed

	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= screen_height:
		opponent.bottom = screen_height

def ball_start():
	global ball_speed_x, ball_speed_y

	ball.center = (screen_width/2, screen_height/2)
	ball_speed_y *= random.choice((1,-1))
	ball_speed_x *= random.choice((1,-1))

# General setup
pygame.init()
clock = pygame.time.Clock()

# Main Window
screen_width = 1280
screen_height = 960
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
opponent_speed = 7

# Score Text
player_score = 0
opponent_score = 0
basic_font = pygame.font.Font('freesansbold.ttf', 32)

# Game Status
game_over = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	while player_score < 5 and opponent_score < 5:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
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
		ball_movement()
		player_movement()
		opponent_movement()

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
		clock.tick(60)
	
	while game_over == False:
		# Resets the screen, but to mimic the game visuals
		screen = pygame.display.set_mode((screen_width,screen_height))
		pygame.display.set_caption('Tennis')
		screen.fill(background_color)
		ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
		player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10,140)
		opponent = pygame.Rect(10, screen_height / 2 - 70, 10,140)
		pygame.draw.rect(screen, dark_grey, player)
		pygame.draw.rect(screen, dark_grey, opponent)
		pygame.draw.ellipse(screen, dark_grey, ball)
		pygame.draw.aaline(screen, dark_grey, (screen_width / 2, 0),(screen_width / 2, screen_height))
		
		# Endgame Text
		end_text = basic_font.render(f'{"Game over"}',False,dark_grey)
		screen.blit(end_text,(550,70))
		pygame.display.flip()
		clock.tick(60)
		game_over = True


