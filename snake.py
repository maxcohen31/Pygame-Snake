import pygame
from pygame import mixer
import random

# Making the class Apple
class Apple:
    
    def __init__(self):
        self.appleX = random.randint(0, grid_block2 - 1) # X_coord.
        self.appleY = random.randint(0, grid_block2 - 1) # Y_coord.
        self.apple_pos = pygame.math.Vector2(self.appleX, self.appleY)

    # Method to draw the apple    
    def drawing_the_apple(self):
        
        apple = pygame.Rect(int(self.appleX * grid_block), int(self.appleY * grid_block), grid_block, grid_block)
        pygame.draw.rect(screen, (255, 0, 0), apple)
    
    # Method to spaw the apple on the board
    def spawing_new_apple(self):
        
        self.appleX = random.randint(0, grid_block2 - 1) # random x coord.
        self.appleY = random.randint(0, grid_block2 - 1) # random y coord.
        self.apple_pos = pygame.math.Vector2(self.appleX, self.appleY)
        
class Snake:
    
    def __init__(self):
        self.snake = [pygame.math.Vector2(7, 12), pygame.math.Vector2(8, 12), pygame.math.Vector2(9, 12)] # Blocks of the snake
        self.movement = pygame.math.Vector2(-1, 0) # Right movement
        self.new_snake_body = False # Variable to add blocks to the snake
        self.bite = pygame.mixer.Sound('Bite.wav')
        
        
        
    def drawing_the_snake(self):
        for pixel in self.snake: # Looping through the blocks of the snake
            pixel_draw = pygame.Rect(pixel.x * grid_block, pixel.y * grid_block, grid_block, grid_block) # making the blocks (x, y, height, width)
            pygame.draw.rect(screen, (0, 255, 0), pixel_draw) # Drawing the blocks
    
    # Method to move the snake
    def moving_the_snake(self):        
        if self.new_snake_body == True:
            snake_move = self.snake[:] # Select all the snake body
            snake_move.insert(0, snake_move[0] + self.movement) # 
            self.snake = snake_move[:]
            self.new_snake_body = False # Turn the variable new_snake_body to False
        else:
            snake_move = self.snake[:-1] # Select the first two elements of the snake body
            snake_move.insert(0, snake_move[0] + self.movement) # Insert at the start of the list the snake_move value
            self.snake = snake_move[:]
    
    # Method to play the bite
    def play_bite(self):       
        self.bite.play()
        
    # Method to add the block to the snake
    def add_new_body(self):        
        self.new_snake_body = True # If True a new block will be add to the snake body
    
class Game:    
    def __init__(self):
        
        self.spaw_snake = Snake()
        self.spaw_apple = Apple()
        mixer.music.load('industry_matic.wav')
        mixer.music.play(-1)
        
        
    def snake_and_apple(self):
        self.spaw_apple.drawing_the_apple() # Spawn apple
        self.spaw_snake.drawing_the_snake() # Spawn snake
        self.score()
  
    def move(self):
        self.spaw_snake.moving_the_snake()
        self.eating_the_apple()
        self.boundaries()
         
    # Method that allows the snake to eat the apple        
    def eating_the_apple(self):  
        if self.spaw_snake.snake[0] == self.spaw_apple.apple_pos: # check if the head of the snake(first block) has the same position of the apple
            self.spaw_apple.spawing_new_apple() # A new apple wil be spawned
            self.spaw_snake.add_new_body() # A new block to add to the snake body
            self.spaw_snake.play_bite() # Sound
     
    # Method that bound the snake into the grid 
    def boundaries(self):
        if self.spaw_snake.snake[0].x < 0:
            pygame.quit()
        elif self.spaw_snake.snake[0].x > grid_block2:
            pygame.quit()
        elif self.spaw_snake.snake[0].y < 0:
            pygame.quit()
        elif self.spaw_snake.snake[0].y > grid_block2:
            pygame.quit()            
        
        for pixel in self.spaw_snake.snake[1:]:
            if pixel == self.spaw_snake.snake[0]:
                pygame.quit()
               
    def score(self):
        textX = 550
        textY = 550
        score = str(len(self.spaw_snake.snake) - 3)
        show_score = font.render(score, True, (255, 255, 255))
        rectangle_of_score = show_score.get_rect(center = (textX, textY))
        screen.blit(show_score, rectangle_of_score)
            
pygame.init()
pygame.display.set_caption('Snake')
icon = pygame.image.load('snake.png')
get_icon = pygame.display.set_icon(icon)
grid_block = 30
grid_block2 = 20
font = pygame.font.Font('freesansbold.ttf', 20)
screen = pygame.display.set_mode((grid_block * grid_block2, grid_block * grid_block2))
g = Game()

SCREEN_MOVEMENT = pygame.USEREVENT
pygame.time.set_timer(SCREEN_MOVEMENT, 90)

game_on = True
while game_on:
    
    screen.fill((0,0,0,))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        if event.type == SCREEN_MOVEMENT:
            g.move()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                g.spaw_snake.movement = pygame.math.Vector2(0, -1) 
            if event.key == pygame.K_LEFT:
                g.spaw_snake.movement = pygame.math.Vector2(-1, 0)      
            if event.key == pygame.K_DOWN:
                g.spaw_snake.movement = pygame.math.Vector2(0, 1)
            if event.key == pygame.K_RIGHT:
                g.spaw_snake.movement = pygame.math.Vector2(1, 0)
            
      
    g.snake_and_apple()
    pygame.display.update()   
        
