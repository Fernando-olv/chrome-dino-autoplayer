import pyautogui as auto
from pathlib import Path

# Error configuration
auto.useImageNotFoundException()

# Get the absolute path to the Automacao directory
BASE_PATH = Path(__file__).parent / "Automacao"
IMAGE_PATH = BASE_PATH / "img"
DINO_PATH = BASE_PATH / "dino.png"

# Get list of obstacle images
image_list = list(IMAGE_PATH.glob("*.png"))

while True:
    # Iterate through the images in the img folder
    for image in image_list:
        # If the image is not found on the screen, pyautogui raises an error
        # That's why we use the try block
        try:
            dino_position = auto.locateOnScreen(str(DINO_PATH), confidence=0.6)
            cactus_position = auto.locateOnScreen(str(image), confidence=0.8)
        # Instead of the program crashing, we catch the error and
        # assign None to cactus_position and dino_position
        except auto.ImageNotFoundException:
            cactus_position = None
            dino_position = None
        # If there was no error (both images were found)
        else:
            if dino_position is not None and cactus_position is not None:
                px_dino = dino_position.left
                px_cactus = cactus_position.left

                if px_cactus - px_dino <= 150:
                    auto.press("space")
                    auto.keyDown("space")
        
        # TODO:
        # - Detect pterodactyl (flying obstacle)
        # - Adapt to night mode (grayscale detection idea)
