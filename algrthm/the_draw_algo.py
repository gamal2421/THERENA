import math
import subprocess
import pyautogui
import time

def open_print():
    subprocess.Popen("mspaint.exe")

def draw_rectangle():
    open_print()
    time.sleep(5)  # Wait for Paint to open

    # Starting coordinates for the top-left corner of the rectangle
    x_start, y_start = 500, 300
    width, height = 200, 100  # Width and height of the rectangle

    # Draw the rectangle
    pyautogui.moveTo(x_start, y_start)
    pyautogui.dragTo(x_start + width, y_start, duration=0.1)       # Top side
    pyautogui.dragTo(x_start + width, y_start + height, duration=0.1)  # Right side
    pyautogui.dragTo(x_start, y_start + height, duration=0.1)      # Bottom side
    pyautogui.dragTo(x_start, y_start, duration=0.1)               # Left side
    

def draw_triangle():
    open_print()
    time.sleep(5)  # Wait for Paint to open

    # Define the starting vertex and side length
    x1, y1 = 500, 400  # Starting point
    side_length1 = 150  # First side length
    side_length2 = 100  # Second side length
    angle = -90  # Angle in degrees between the two sides

    x2 = x1 + side_length1
    y2 = y1 

    # Calculate the third vertex based on the angle and side_length2
    angle_radians = math.radians(angle)  # Convert angle to radians
    x3 = x1 + side_length2 * math.cos(angle_radians)
    y3 = y1 + side_length2 * math.sin(angle_radians)

    # Move to the first vertex
    pyautogui.moveTo(x1, y1)

    # Draw each side of the triangle
    pyautogui.dragTo(x2, y2, duration=0.1)  # First side
    pyautogui.dragTo(x3, y3, duration=0.1)  # Second side
    pyautogui.dragTo(x1, y1, duration=0.1)  # Third side to complete the triangle

def draw_nrm_cube():
    open_print()
    time.sleep(5)  # Wait for Paint to open

    # Starting coordinates for the cube
    x_start, y_start = 500, 300
    side_length = 100  # Length of the cube's sides

    # Draw the front square of the cube
    pyautogui.moveTo(x_start, y_start)
    pyautogui.dragTo(x_start + side_length, y_start, duration=0.1)  # Top line
    pyautogui.dragTo(x_start + side_length, y_start + side_length, duration=0.1)  # Right line
    pyautogui.dragTo(x_start, y_start + side_length, duration=0.1)  # Bottom line
    pyautogui.dragTo(x_start, y_start, duration=0.1)  # Left line

    # Draw the back square of the cube, slightly offset
    offset = 30  # Offset for the 3D effect
    pyautogui.moveTo(x_start + offset, y_start - offset)
    pyautogui.dragTo(x_start + side_length + offset, y_start - offset, duration=0.1)  # Top line
    pyautogui.dragTo(x_start + side_length + offset, y_start + side_length - offset, duration=0.1)  # Right line
    pyautogui.dragTo(x_start + offset, y_start + side_length - offset, duration=0.1)  # Bottom line
    pyautogui.dragTo(x_start + offset, y_start - offset, duration=0.1)  # Left line

    # Connect the corners to complete the cube
    pyautogui.moveTo(x_start, y_start)
    pyautogui.dragTo(x_start + offset, y_start - offset, duration=0.1)  # Top-left corner

    pyautogui.moveTo(x_start + side_length, y_start)
    pyautogui.dragTo(x_start + side_length + offset, y_start - offset, duration=0.1)  # Top-right corner

    pyautogui.moveTo(x_start + side_length, y_start + side_length)
    pyautogui.dragTo(x_start + side_length + offset, y_start + side_length - offset, duration=0.1)  # Bottom-right corner

    pyautogui.moveTo(x_start, y_start + side_length)
    pyautogui.dragTo(x_start + offset, y_start + side_length - offset, duration=0.1)  # Bottom-left corner
#def reco_of_your_drw(arr[]):
#    x ,y = 0,0
