import matplotlib.pyplot as plt
import math

def visualize_binary(file_path):
    # Read binary data
    with open(file_path, "rb") as file:
        binary_data = file.read()

    # Initialize a figure
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis("off")  # Turn off the axes

    # Initialize starting coordinates and cumulative variables
    x, y = 250, 250  # Start near the center of the plot
    cumulative_sum = 0

    # Convert binary data into a list of binary strings
    binary_list = createList(binary_data)

    print("Calculating values...")

    for binary_str in binary_list:
        # Calculate a cumulative value from the binary string
        binary_value = int(binary_str, 2)
        cumulative_sum += binary_value  # Cascade effect

        # Map cumulative_sum to angle and step size
        angle = cumulative_sum % 360  # Angle in degrees
        step_size = (binary_value % 50) + 1  # Step size (1 to 50)

        # Convert angle to radians for trigonometric functions
        angle_rad = math.radians(angle)

        # Calculate new position based on angle and step size
        x_new = x + step_size * math.cos(angle_rad)
        y_new = y + step_size * math.sin(angle_rad)

        # Ensure positions remain within bounds (wrap-around effect)
        x_new %= 500
        y_new %= 500

        # Generate a unique color based on the binary string
        color = generate_unique_color(binary_str)

        # Draw the line
        ax.plot([x, x_new], [y, y_new], color=color, linewidth=2)

        # Update current position
        x, y = x_new, y_new

    print("Displaying...")

    # Save or display the visualization
    plt.savefig("./output/binary_visualization1.jpg", dpi=300)
    #plt.show() # currently doesn't work


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

    return [r, g, b]  # Return the RGB color value


# Example usage
visualize_binary("./input/testfile.txt")
