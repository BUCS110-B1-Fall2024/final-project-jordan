class Food:
    def __init__(self, x, y, img_file):
        """
        Initializes the food object
        args:
        - x: int - x-coordinate position
        - y: int - y-coordinate position
        - img_file: str - path to the image representing the food
        """
        self.x = x
        self.y = y
        self.img_file = img_file

    def is_eaten(self, pet_x, pet_y):
        """
        Checks if the pet has eaten the food
        args:
        - pet_x: int - x-coordinate of the pet
        - pet_y: int - y-coordinate of the pet
        return: bool - True if eaten, False otherwise
        """
        return abs(self.x - pet_x) < 10 and abs(self.y - pet_y) < 10
