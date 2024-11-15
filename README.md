# 3D House Drawing with Pycairo
This project uses Python and the Pycairo library to render a 2D representation of a house with a simulated 3D effect. The image includes details such as the main house structure, a slanted red roof, chimney, windows, and door, aiming to resemble the style shown in a reference image.

# Features
House Base: A light gray rectangular structure representing the main body of the house.
Roof: A red roof with depth, created by adding light red side panels to enhance the 3D effect.
Chimney: Two-tiered chimney on the roof.
Door: A brown door with a handle.
# Requirements
Python 3.x
Pycairo library
# To install Pycairo, run:

pip install pycairo
Clone or download this repository.

Navigate to the project directory where the 3D_house.py script is located.

Run the script to generate the house image.

Example Output
The generated image should resemble the reference image provided in the project, with a red slanted roof, chimney, and basic 3D-like features.

Troubleshooting
TypeError in Transformations: Ensure that you’re not directly passing multiple arguments to context.transform(). Check the function syntax to avoid transformation issues.
Pycairo Installation Issues: If Pycairo is difficult to install, make sure to have development tools on your system, as Pycairo may need them.
License
This project is licensed under the MIT License. See the LICENSE file for details.
