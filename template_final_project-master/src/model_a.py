class Pet:
    def __init__(self, name, x, y, img_file):
        """
        Initializes the pet object
        args:
        - name: str - name of the pet
        - x: int - x-coordinate position
        - y: int - y-coordinate position
        - img_file: str - path to the image representing the pet
        """
        self.name = name
        self.x = x
        self.y = y
        self.img_file = img_file
        self.hunger = 0
        self.happiness = 100

    def move(self, dx, dy):
        """
        Moves the pet by a certain amount
        args:
        - dx: int - change in x-coordinate
        - dy: int - change in y-coordinate
        return: None
        """
        self.x += dx
        self.y += dy

    def feed(self):
        """
        Reduces hunger level
        args: None
        return: None
        """
        self.hunger = max(self.hunger - 10, 0)

    def play(self):
        """
        Increases happiness level
        args: None
        return: None
        """
        self.happiness = min(self.happiness + 10, 100)
