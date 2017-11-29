"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Angel Rivera.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()

def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.txt  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------

    window = rg.RoseWindow(600, 400, "Two Circles")

    center_point1 = rg.Point(200, 100)
    center_point2 = rg.Point(400, 200)

    radius1 = 50
    radius2 = 70

    circle1 = rg.Circle(center_point1, radius1)
    circle2 = rg.Circle(center_point2, radius2)

    circle1.fill_color = 'gold4'

    circle1.attach_to(window)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(600, 400, "Circle and Rectangle")

    center_point = rg.Point(100, 100)
    radius = 50
    just_a_circle = rg.Circle(center_point, radius)
    just_a_circle.fill_color = 'blue'
    just_a_circle.attach_to(window)
    print(just_a_circle.outline_thickness)
    print(just_a_circle.fill_color)
    print(just_a_circle.center)
    print(center_point.x)
    print(center_point.y)

    point1 = rg.Point(300, 150)
    point2 = rg.Point(400, 50)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.attach_to(window)
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.get_center())
    print((point1.x + point2.x) / 2)
    print((point1.y + point2.y) / 2)

    window.render()
    window.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 4. Implement and test this function.
    # ------------------------------------------------------------------
    window = rg.RoseWindow(600, 500, "Lines")

    point1 = rg.Point(100, 200)
    point2 = rg.Point(200, 300)
    zoint1 = rg.Point(400, 200)
    zoint2 = rg.Point(300, 200)

    lines = rg.Line(point1, point2)
    zines = rg.Line(zoint1, zoint2)

    zines.thickness = 10

    print(lines.get_midpoint())
    print((point1.x + point2.x) / 2)
    print((point1.y + point2.y) / 2)

    print(zines.get_midpoint())
    print((zoint1.x + zoint2.x) / 2)
    print((zoint1.y + zoint2.y) / 2)

    lines.attach_to(window)
    zines.attach_to(window)

    window.render()
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
