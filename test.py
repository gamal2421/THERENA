import tkinter as tk
from PIL import Image, ImageDraw, ImageTk

def create_wave_image(size, wave_color, bg_color):
    # Create a new image with a transparent background
    image = Image.new('RGBA', size, bg_color)
    draw = ImageDraw.Draw(image)

    # Calculate the center and radius
    center_x, center_y = size[0] // 2, size[1] // 2
    max_radius = min(center_x, center_y)

    # Draw waves
    for radius in range(max_radius, 0, -20):
        alpha = int(255 * (max_radius - radius) / max_radius)
        fill_color = wave_color + (alpha,)
        draw.ellipse((center_x - radius, center_y - radius, center_x + radius, center_y + radius), fill=fill_color)

    return image

def on_button_click():
    print("Button clicked!")

# Create the main window
root = tk.Tk()
root.title("Gemini UI")

# Create a canvas
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# Create the wave image
wave_image = create_wave_image((400, 400), wave_color=(0, 0, 255), bg_color=(255, 255, 255, 0))
wave_image_tk = ImageTk.PhotoImage(wave_image)
canvas.create_image(200, 200, image=wave_image_tk)

# Create a circular button
button = tk.Button(root, text="Click Me", command=on_button_click)
button.place(x=170, y=170, width=60, height=60)
button.config(bg="blue", fg="white")

# Start the main event loop
root.mainloop()
