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
        self.snake = [pygame.math.Vector2(7, 12), pygame.math.Vector2(8, 12), pygame.math.Vector2(9, 12)]
        self.movement = pygame.math.Vector2(-1, 0)
        self.new_snake_body = False
        self.bite = pygame.mixer.Sound('Bite.wav')
        
        
        
    def drawing_the_snake(self):
        for pixel in self.snake:
            pixel_draw = pygame.Rect(pixel.x * grid_block, pixel.y * grid_block, grid_block, grid_block)
            pygame.draw.rect(screen, (0, 255, 0), pixel_draw)     
                                 
    def moving_the_snake(self):        
        if self.new_snake_body == True:
            snake_move = self.snake[:]
            snake_move.insert(0, snake_move[0] + self.movement)
            self.snake = snake_move[:]
            self.new_snake_body = False
        else:
            snake_move = self.snake[:-1]
            snake_move.insert(0, snake_move[0] + self.movement)
            self.snake = snake_move[:]
         
    def play_bite(self):       
        self.bite.play()
    
    def add_new_body(self):        
        self.new_snake_body = True
    
class Game:    
    def __init__(self):
        
        self.spaw_snake = Snake()
        self.spaw_apple = Apple()
        mixer.music.load('industry_matic.wav')
        mixer.music.play(-1)
        
        
    def snake_and_apple(self):
        
        self.spaw_apple.drawing_the_apple()
        self.spaw_snake.drawing_the_snake()
        self.score()
  
    def move(self):
        
        self.spaw_snake.moving_the_snake()
        self.eating_the_apple()
        self.boundaries()
         
    def eating_the_apple(self):
        
        if self.spaw_snake.snake[0] == self.spaw_apple.apple_pos:
            self.spaw_apple.spawing_new_apple()
            self.spaw_snake.add_new_body()
            self.spaw_snake.play_bite()
            
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
        
