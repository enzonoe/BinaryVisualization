import matplotlib.pyplot as plt
import random
import math

def visualize_binary(file_path):
    # Read binary data
    with open(file_path, "rb") as file:
        binary_data = file.read()

    # Initialize a figure
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis("off")  # Turn off the axes
    
    # Initialize starting coordinates (arbitrary starting point)
    x, y = 0, 0
    prev_x, prev_y = 0, 0

    # Convert binary data into a list of binary strings
    binary_list = createList(binary_data)

    print("Calculating values...")

    for binary_str in binary_list:
        # Calculate the angle from the binary string (0 to 360 degrees)
        angle = int(binary_str, 2) % 360  # Map the binary string to an angle

        # Calculate the starting position using the binary string
        # We can improve this by creating a more varied mapping
        x = (int(binary_str[:4], 2) % 500)  # Use the first 4 bits for horizontal position
        y = (int(binary_str[4:], 2) * 5 % 500)  # Use the last 4 bits for vertical position

        # Use the sum of bits for line length to create variation
        length = sum(int(bit) for bit in binary_str) * 10

        # Convert angle to radians for trigonometric functions
        angle_rad = (angle * math.pi) / 180

        # Calculate new position based on the angle
        #x_new = x + length * math.cos(angle_rad)
        #y_new = y + length * math.sin(angle_rad)

        # Generate a unique color based on the binary string (full byte for RGB)
        color = generate_unique_color(binary_str)

        # Draw the line
        ax.plot([x, prev_x], [y, prev_y], color=color, linewidth=2)

        # Update coordinates for the next iteration
        prev_x, prev_y = x, y
    
    print("Displaying...")

    # Save or display the visualization
    plt.savefig("binary_visualization.jpg", dpi=300)
    plt.show()

def createList(data):
    print("Converting into list...")
    binary_str_list = []
    for byte in data:
        # Convert byte to binary (8-bit string)
        binary_str = f"{byte:08b}"
        binary_str_list.append(binary_str)
    return binary_str_list

def generate_unique_color(binary_str):
    # Use the entire byte (8 bits) to generate an RGB color
    r = int(binary_str[:3], 2) / 7  # First 3 bits for red (0-7)
    g = int(binary_str[3:6], 2) / 7  # Next 3 bits for green (0-7)
    b = int(binary_str[6:], 2) / 3  # Last 2 bits for blue (0-3)

    # You can also scale the values further to get a broader range of color combinations
    return [r, g, b]  # Return the RGB color value

# Example usage
visualize_binary("akita.jpg")
