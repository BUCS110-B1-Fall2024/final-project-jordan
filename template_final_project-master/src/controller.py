import pygame
from model_a import Pet
from model_b import Food

class Controller:
    def __init__(self):
        """
        Initializes objects and resources required to run the program
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pet Simulator")
        self.clock = pygame.time.Clock()
        
        # Initialize models
        self.pet = Pet("Fluffy", 100, 100, "assets/pet.png")
        self.food = Food(200, 200, "assets/food.png")
        
        # Game state management
        self.state = "start"

    def mainloop(self):
        """
        Main loop to handle events, update models, and redraw the screen
        """
        running = True
        while running:
            if self.state == "start":
                self.display_start_screen()
            elif self.state == "game":
                running = self.handle_events()
                self.update_game_state()
                self.redraw_frame()
            elif self.state == "pause":
                self.display_pause_screen()
            elif self.state == "game_over":
                self.display_game_over_screen()

            self.clock.tick(30)  # Cap frame rate

        pygame.quit()

    def handle_events(self):
        """
        Handle user inputs and events
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False  # Exit game

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.pet.move_left()
        if keys[pygame.K_RIGHT]:
            self.pet.move_right()
        if keys[pygame.K_UP]:
            self.pet.move_up()
        if keys[pygame.K_DOWN]:
            self.pet.move_down()
        if keys[pygame.K_p]:  # Pause functionality
            self.state = "pause"
        return True

    def update_game_state(self):
        """
        Detect collisions and update game logic
        """
        if self.food.is_eaten(self.pet.x, self.pet.y):
            self.pet.feed()
            # Reset or move food to a new location
            self.food.respawn()  # Implement this in Food class

    def redraw_frame(self):
        """
        Redraw the screen and all objects
        """
        self.screen.fill((255, 255, 255))  # White background
        self.pet.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    # State-specific screens
    def display_start_screen(self):
        self.screen.fill((200, 200, 255))  # Light blue background
        # Add text or images here using pygame.font.Font
        pygame.display.flip()
        # Press any key to start
        if any(pygame.key.get_pressed()):
            self.state = "game"

    def display_pause_screen(self):
        self.screen.fill((100, 100, 100))  # Gray background
        # Pause screen message
        pygame.display.flip()
        # Resume on any key press
        if any(pygame.key.get_pressed()):
            self.state = "game"

    def display_game_over_screen(self):
        self.screen.fill((255, 0, 0))  # Red background
        # Add game-over text here
        pygame.display.flip()
        pygame.time.wait(3000)  # Pause for 3 seconds
        self.state = "start"  # Restart the game

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
