import pyautogui as auto
import os

##Error configuration
auto.useImageNotFoundException()

IMAGE_PATH = ".\\img"

image_list = os.listdir(IMAGE_PATH) 
dino_path = ".\\dino.png"

while True:
    #Iterate through the images in the img folder
    for image in image_list:
        #Get the path of each image one by one
        image_path = os.path.join(IMAGE_PATH, image)
        #If the image is not found on the screen, pyautogui raises an error
        #That’s why we use the try block
        try:
            dino_position = auto.locateOnScreen(dino_path, confidence=0.6)
            cactus_position = auto.locateOnScreen(image_path, confidence=0.8)
        #Instead of the program crashing, we catch the error and
        #Assign None to cactus_position and dino_position
        except auto.ImageNotFoundException:
            cactus_position = None
            dino_position = None
        #If there was no error (both images were found)
        else:
            px_dino = dino_position.left
            px_cactus = cactus_position.left

            if px_cactus - px_dino <= 150:
                auto.press("space")
                auto.keyDown("space")
        
        #TO DO:
        # - Identify pterodactyl
        # - Identify night mode (TEACHER’S THOUGHT: maybe use GRAYSCALE)