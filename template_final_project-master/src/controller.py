import pygame
from src.model_a import Pet
from src.model_b import Food

class Controller:
    def __init__(self):
        """
        Initializes objects and resources required to run the program
        """
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.pet = Pet("Fluffy", 100, 100, "assets/pet.png")
        self.food = Food(200, 200, "assets/food.png")

    def mainloop(self):
        """
        Main loop to handle events, update models, and redraw the screen
        """
        running = True
        while running:
            # 1. Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # 2. Detect collisions or update models
            if self.food.is_eaten(self.pet.x, self.pet.y):
                self.pet.feed()

            # 3. Redraw the screen
            self.screen.fill((255, 255, 255))  # Clear screen
            pygame.display.flip()

            # 4. Cap frame rate
            self.clock.tick(30)

        pygame.quit()

if __name__ == "__main__":
    controller = Controller()
    controller.mainloop()
