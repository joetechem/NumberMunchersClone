#!/usr/bin/python
import pygame
from gi.repository import Gtk

class Button:

    def __init__(self, screen, x, y, width, height):
        self.screen = screen

        self.hovered = False
        self.pressed = False

        self.staticColor = (255,0,0)
        self.hoveredColor = (0,255,0)
        self.pressedColor = (0,0,255)
        self.currentColor = self.staticColor

        self.rect = (x,y,width,height)

    def events(self, event):
        pos = event.pos
        button = 0

        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            button = event.button

        if pos[0] > self.rect[0] and pos[0] < self.rect[0] + self.rect[2] and pos[1] > self.rect[1] and pos[1] < self.rect[1] + self.rect[3]:
            self.currentColor = self.hoveredColor
            if button == 1:
                self.currentColor = self.pressedColor
        else:
            self.currentColor = self.staticColor

    def draw(self):
        pygame.draw.rect(self.screen, self.currentColor, self.rect)

class Menu:

    def __init__(self, screen):
        self.screen = screen

        startButton = Button(screen, 200,200,100,100)

        self.buttons = [startButton]

    def events(self, event):
        for button in self.buttons:
            button.events(event)

    def draw(self):
        for button in self.buttons:
            button.draw()

class NumberMunchersGame:

    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

	    #Create the screen
        self.screen = pygame.display.get_surface()

        self.menu = Menu(self.screen)

        self.paused = False

    def set_paused(self, paused):
        self.paused = paused

    # Called to save the state of the game to the Journal.
    def write_file(self, file_path):
        pass

    # Called to load the state of the game from the Journal.
    def read_file(self, file_path):
        pass

    #Event handling and logic goes here
    def events(self):
        # Pump PyGame messages.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.VIDEORESIZE:
                pygame.display.set_mode(event.size, pygame.RESIZABLE)

            #elif event.type == pygame.KEYDOWN:

            elif event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
                self.menu.events(event)

    #Update logic goes here
    def update(self):
        # Move the ball
        if not self.paused:
            return

    #Rendering logic goes here
    def draw(self):
        # Clear Display
        self.screen.fill((255, 255, 255))  # 255 for white

        # Draw the menu
        self.menu.draw()

        # Draw the ball
        pygame.draw.circle(self.screen, (255, 0, 0), (100, 100), 100)

        # Flip Display
        pygame.display.flip()

    # The main game loop.
    def run(self):
        self.running = True

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            #Handle events
            self.events()

            #Handle game logic
            self.update()

	        #Handle rendering
            self.draw()

            # Try to stay at 30 FPS
            self.clock.tick(30)


# This function is called when the game is run directly from the command line:
# ./NumberMunchersGame.py
def main():
    pygame.init()
    pygame.display.set_mode((600, 480), pygame.RESIZABLE)
    game = NumberMunchersGame()
    game.run()

if __name__ == '__main__':
    main()
