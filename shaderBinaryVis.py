import arcade

# Set up the window
window_width = 500
window_height = 500
window = arcade.Window(window_width, window_height, "Simple Rectangle")
# set background 
arcade.set_background_color(arcade.color.WHITE) 

# Define a function to handle the drawing
def on_draw():
    arcade.start_render()  # Start the drawing process
    # Draw primitive
    #arcade.draw_rectangle_outline(250,250,500,500,arcade.color.AERO_BLUE,10)
    #arcade.draw_rectangle_filled(250, 250, 250, 250, arcade.color.RED)
    #arcade.draw_arc_filled(250,250,250,250, arcade.color.RED,0,150)
    #arcade.draw_parabola_outline(0, -250, 500, 300, arcade.color.GREEN, 10, 0) 

# Set the function to handle the drawing when the window is refreshed
window.on_draw = on_draw

# Start the arcade application
arcade.run()
