import time
import cv2
import numpy as np
import pyautogui
import pytesseract


# Convert PIL color image to OpenCV gray scale image
def get_cv2_grayscaled_image(image):
    return cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)


# Wait for the game to start
def wait_helper_function() -> None:
    """
    Helper function to wait for website load
    :return:
    """
    while True:
        if pyautogui.pixelMatchesColor(380, 350, (0, 225, 105)):
            break


# Check if must stop
def isOver() -> bool:
    """
    Check if must stop
    :return: True if must stop, False otherwise
    """
    return pyautogui.locateOnScreen('StopSignal.jpg') is not None


if __name__ == '__main__':
    is_over = False
    while not is_over:
        print("Waiting for game to start...")
        # Wait for the game to start
        wait_helper_function()

        print("Game started")
        # Get the game screen
        im = pyautogui.screenshot(region=(370, 340, 920, 60))
        im = get_cv2_grayscaled_image(im)

        # Adding custom options
        custom_config = r'--oem 3 --psm 6'

        # Get the text from the image
        ocr = pytesseract.image_to_string(im, config=custom_config)
        # Type the text
        # for i in ocr:
        pyautogui.write(ocr + ' ')
        time.sleep(0.0001)
        is_over = isOver()
