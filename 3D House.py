
import cairo

# Set up the surface and context
WIDTH, HEIGHT = 600, 400
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Set the background color
context.set_source_rgb(1, 1, 1)  # White
context.paint()

# Set line width for the edges
context.set_line_width(1)  # Thin black stroke

# Draw the left wall (angled for 3D effect)
context.move_to(220, 150)
context.line_to(220, 280)
context.line_to(160, 250)
context.line_to(160, 160)
context.close_path()
context.set_source_rgb(0.8, 0.8, 0.8)  # Light grey
context.fill_preserve()  # Fill but preserve path for stroking
context.set_source_rgb(0, 0, 0)  # Black color for the stroke
context.stroke()

# Draw the front wall
context.move_to(220, 150)
context.line_to(220, 280)
context.line_to(400, 270)
context.line_to(400, 150)
context.line_to(310, 80)
context.close_path()
context.set_source_rgb(0.7, 0.7, 0.7)  # Slightly darker grey
context.fill_preserve()  # Fill but preserve path for stroking
context.set_source_rgb(0, 0, 0)  # Black color for the stroke
context.stroke()

door_color = (0.4, 0.2, 0)  # brown
outline_color = (0,0,0) #black

# Door
context.set_source_rgb(*door_color)
context.rectangle(230, 198, 40, 80)
context.fill_preserve()
context.set_source_rgb(*outline_color)
context.stroke()

# Door handle
context.arc(240, 240, 3, 0, 2 * 3.1416)
context.set_source_rgb(*outline_color)
context.fill()

# Colors
frame_color = (0.4, 0.2, 0.1)    # Brown for the window frame
pane_color = (0.5, 0.8, 1)       # Light blue for window panes

# Draw the outer frame
context.set_source_rgb(*frame_color)
context.rectangle(290, 170, 100, 80)
context.fill()


# Draw the left window pane
context.set_source_rgb(*pane_color)
context.rectangle(295, 175, 40, 70)
context.fill()

# Draw the right window pane
context.rectangle(345, 175, 40, 70)
context.fill()


# Add the outline of the frame
context.set_line_width(3)
context.set_source_rgb(*frame_color)
context.rectangle(290, 170, 100, 80)
context.stroke()

# Draw slanted zigzag line on the door with reduced slant, increased length, and wavelength
context.set_source_rgb(0, 0, 0)  # Black color for the zigzag line
context.set_line_width(3)

door_x=230
door_y=198
door_width=40

# Starting point of the slanted zigzag (closer to the upper part of the door)
zigzag_start_x = door_x + door_width / 2  # Start near the center of the door width
zigzag_start_y = door_y + 5  # Start closer to the top part of the door

# Parameters for the zigzag line with further reduced slant, increased length, and wavelength
num_zigs = 6  # Increased number of zigs to lengthen the zigzag
zigzag_spacing = 10  # Increased spacing to lengthen the wavelength
zigzag_amplitude = 20 # Increased amplitude to make peaks higher and wider
slant_offset = 2  # Further reduced slant for a more vertical zigzag pattern

# Move to starting point
context.move_to(zigzag_start_x, zigzag_start_y)

# Draw a slanted, high-amplitude zigzag pattern using curves
for i in range(num_zigs):
    # Calculate the x position for each wave (increasing to slant it to the right)
    zigzag_x = zigzag_start_x + i * slant_offset
    control_y = zigzag_start_y + (i + 0.6) * zigzag_spacing
    end_y = zigzag_start_y + (i + 2) * zigzag_spacing

    if i % 2 == 0:
        # Curve to the left with higher amplitude
        context.curve_to(zigzag_x + zigzag_amplitude, control_y,
                         zigzag_x + zigzag_amplitude, control_y,
                         zigzag_x, end_y)
    else:
        # Curve to the right with higher amplitude
        context.curve_to(zigzag_x + zigzag_amplitude, control_y,
                         zigzag_x + zigzag_amplitude, control_y,
                         zigzag_x, end_y)

context.stroke()




# Save the result
surface.write_to_png("3D_walls.png")
print("3D house image with perspective saved as '3D_house_with_strokes.png'")
