# VirtuPets
## CS110 B1 Final Project  Semester 1, 2024

## Team Members

Jordan Lee

***

## Project Description

This project is a pet simulator game where players care for a virtual pet by managing its needs like hunger, energy, and happiness. Players can interact with the pet through activities like feeding, playing, and letting it rest.

***    

## GUI Design

### Initial Design

![initial gui](assets/gui.jpg)

### Final Design

![final gui](assets/finalgui.jpg)

## Program Design

### Features

1. Start Menu
2. Movable Pet Character
3. Interaction Buttons (Feed, Play, Sleep)
4. Stat Display (hunger, happiness, energy)
5. Game Over screen (if the pet’s health declines too much)

### Classes
#### **Pet Class**
Attributes:
- `name`: str - the pet's name
- `x`: int - x-coordinate position
- `y`: int - y-coordinate position
- `img_file`: str - image representing the pet
- `hunger`: int - hunger level of the pet
- `happiness`: int - happiness level of the pet

Methods:
- `__init__(name, x, y, img_file)`
- `move(dx, dy)`
- `feed()`
- `play()`

#### **Food Class**
Attributes:
- `x`: int - x-coordinate position
- `y`: int - y-coordinate position
- `img_file`: str - image representing the food

Methods:
- `__init__(x, y, img_file)`
- `is_eaten(pet_x, pet_y)`

## ATP

### **Test Case 1: Pet Status Updates**  
Test Description: Verify that the pet's status (e.g., hunger, happiness, energy) updates correctly based on user interactions.  

Test Steps: 
1. Start the game and select a pet.  
2. Feed the pet.  
3. Confirm that the hunger level decreases.  
4. Play with the pet and check happiness level.  

Expected Outcome:
The pet's status updates correctly after each interaction.

### **Test Case 2: Pet Interaction (Activity Options)**  
Test Description: Ensure that each pet activity (e.g., feeding, playing, resting) functions as expected.

Test Steps:
1. Start the game and select the Feed option.
2. Confirm that the pet eats and hunger decreases.
3. Select the Play option.
4. Confirm that the pet plays and happiness increases.
5. Select the Rest option.
6. Confirm that the pet rests and energy increases.

Expected Outcome:
Each activity should trigger the corresponding pet behavior and update the appropriate status attributes.


### **Test Case 3: Pet Evolution or Growth**
Test Description: Verify that the pet evolves or grows after reaching specific milestones.

Test Steps:
1. Start the game and interact with the pet until it reaches a certain level or status threshold.
2. Check if the pet evolves or grows to the next stage.
3. Verify that the new appearance or abilities are displayed.

Expected Outcome:
The pet should evolve or grow based on specific milestones, and its appearance or behavior should change accordingly.


### **Test Case 4: Menu Navigation**
Test Description: Test navigation through the game's main and sub-menus.

Test Steps:
1. Start the game and access the main menu.
2. Navigate through options (e.g., Start Game, Settings, Exit).
3. Verify that each option is selectable and leads to the correct screen or action.

Expected Outcome:
All menu options should be accessible, functional, and lead to the expected outcome without errors.


### **Test Case 5: Saving and Loading Progress**
Test Description: Ensure that the pet's progress is saved and can be loaded correctly.

Test Steps:
1. Start the game and interact with the pet (e.g., increase happiness or decrease hunger).
2. Save the game progress.
3. Exit the game and restart it.
4. Load the saved game.
5. Verify that the pet's status reflects the previously saved state.

Expected Outcome:
The game should save and load progress correctly, maintaining all pet status data.