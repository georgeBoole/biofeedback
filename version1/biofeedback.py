from mindcontrol.userbrain import Brain, brain_parameters
import pygame
from pygame.locals import *
from time import sleep

#Initialize pygame and font.
pygame.init()
pygame.font.init()
font = pygame.font.Font(None,32)
white = (255,255,255)
black = (0,0,0)
red = (255,102,73)
green = (107,255,113)
blue = (58,167,255)
magenta = (147,112,219)
yellow = (255,244,65)
default_color = yellow
#Initialize the display surface
RESOLUTION = (SCREEN_WIDTH,SCREEN_HEIGHT) = (600,800)
screen = pygame.display.set_mode(RESOLUTION)
bg = pygame.Surface((SCREEN_WIDTH,SCREEN_HEIGHT))
#logo = util.Load_Image('logo.png',-1)
pygame.display.set_caption('EEG Biofeedback')
def upperBound(headset_attr):
	if headset_attr == 'attention' or headset_attr == 'meditation':
		return 100.0
	elif headset_attr == 'poorSignalLevel':
		return 200.0
	if headset_attr == 'blinkStrength':
		return 255.0

def draw_progress_bar(SURFACE = screen,COLOR = default_color,MAX_WIDTH = 500,MAX_QUANTITY = 1000,LOAD_QUANTITY = 1000,LOCATION = (50,450),HEIGHT = 125,BORDER_COLOR = (30,0,0)): #V
    PROGRESS = LOAD_QUANTITY/MAX_QUANTITY
    CURRENT_WIDTH = MAX_WIDTH * PROGRESS
    BAR_RECT = pygame.Rect(LOCATION[0],LOCATION[1],CURRENT_WIDTH,HEIGHT)
    BORDER_RECT = pygame.Rect(LOCATION[0],LOCATION[1],MAX_WIDTH,HEIGHT)
    pygame.draw.rect(SURFACE,(90,90,90),BORDER_RECT)
    pygame.draw.rect(SURFACE,COLOR,BAR_RECT)
    BAR_BORDER_THICKNESS = 5
    pygame.draw.rect(SURFACE,BORDER_COLOR,BORDER_RECT,BAR_BORDER_THICKNESS)

def renderBG():
	screen.blit(bg,(0,0))
	
def draw_loading_screen():
	renderBG()
	connecting_message = 'Attempting to connect to user\'s brain...'
	msgview = font.render(connecting_message, True, red)
	screen.blit(msgview, (SCREEN_WIDTH/6.0, SCREEN_HEIGHT/1.5))
	pygame.display.flip()

feedback_property = 'meditation'
def draw_main_screen(user_brain):
	renderBG()
	max_quantity = 100.0
	#current_quantity = 800.0
	waveName = font.render(feedback_property, True, red)
	draw_progress_bar(MAX_QUANTITY=max_quantity, LOAD_QUANTITY=user_brain.getProperty(feedback_property))
	screen.blit(waveName, (SCREEN_WIDTH/2.75,SCREEN_HEIGHT/1.2))
	pygame.display.flip()

def main():
	user_brain = Brain()
	while not user_brain.isConnected():
		# display the loading/connecting screen
		draw_loading_screen()
	running = True
	while running:
		draw_main_screen(user_brain)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				pygame.quit()
	
if __name__ == '__main__':
	main()