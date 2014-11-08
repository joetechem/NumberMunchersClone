#!/usr/bin/python
import pygame
from gi.repository import Gtk


class NumberMunchersGame:
    def __init__(self):
        # Set up a clock for managing the frame rate.
        self.clock = pygame.time.Clock()

        self.x = -100
        self.y = 100

        self.vx = 10
        self.vy = 0

        self.paused = False
        self.direction = 1

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
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = -1
                elif event.key == pygame.K_RIGHT:
                    self.direction = 1

    #Update logic goes here
    def update(self, screen):
        # Move the ball
        if not self.paused:
        
            if self.direction == 1 and self.x > screen.get_width() + 100:
                self.x = -100

            elif self.direction == -1 and self.x < -100:
                self.x = screen.get_width() + 100

            if self.y > screen.get_height() - 100:
                self.y = screen.get_height() - 100
                self.vy = -self.vy
            
            self.vy += 5

            self.y += self.vy
            self.x += self.vx * self.direction

    #Rendering logic goes here
    def draw(self, screen):
        # Clear Display
        screen.fill((255, 255, 255))  # 255 for white

        # Draw the ball
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

        # Flip Display
        pygame.display.flip()

    # The main game loop.
    def run(self):
        self.running = True

        screen = pygame.display.get_surface()
	pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), 100)

        while self.running:
            # Pump GTK messages.
            while Gtk.events_pending():
                Gtk.main_iteration()

            #Handle events
            self.events()
            
	    #Handle game logic
            self.update(screen)

	    #Handle rendering
            self.draw(screen)

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
