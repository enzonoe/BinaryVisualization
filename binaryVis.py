import matplotlib.pyplot as plt
import random

#import os
#print(os.getcwd())

def visualize_binary(file_path):
    # Read binary data
    with open(file_path, "rb") as file:
        binary_data = file.read()

    # Initialize a figure
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.axis("off")  # Turn off the axes
    
    # Start coordinates for lines
    x, y = 0, 0
    
    for byte in binary_data:
        # Convert byte to binary (8-bit string)
        binary_str = f"{byte:08b}"
        
        # Use the sum of bits for line length
        length = sum(int(bit) for bit in binary_str) * 10

        # Random angle for the line
        angle = random.randint(0, 360)
        x_new = x + length * random.uniform(-1, 1)
        y_new = y + length * random.uniform(-1, 1)

        # Pick a random color
        color = [random.random() for _ in range(3)]

        # Draw the line
        ax.plot([x, x_new], [y, y_new], color=color, linewidth=2)

        # Update coordinates
        x, y = x_new, y_new
    
    # Save or display the visualization
    plt.savefig("binary_visualization.jpg", dpi=300)
    plt.show()

# Example usage
visualize_binary("bohemian_forest.jpg")
