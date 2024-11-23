import arcade

# Set up the window
window_width = 800
window_height = 600
window = arcade.Window(window_width, window_height, "Simple Rectangle")

# Define a function to handle the drawing
def on_draw():
    arcade.start_render()  # Start the drawing process
    # Draw a red rectangle (x, y, width, height)
    arcade.draw_rectangle_filled(400, 300, 200, 100, arcade.color.RED)

# Set the function to handle the drawing when the window is refreshed
window.on_draw = on_draw

# Start the arcade application
arcade.run()
