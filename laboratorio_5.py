import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    x=-5
    for row in range(30):
        x += 10
        y = -5
        for column in range(30):
            y += 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_2():
    x = -5 + 300
    for row in range(30):
        x += 10
        y = -5
        if row % 2 == 0:
            for column in range(30):
                y += 10
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)
        elif row % 2 != 0:
            for column in range(30):
                y += 10
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_3():
    x = -5 + 600
    for row in range(30):
        x += 10
        y = -5
        for column in range(30):
            y += 10
            if column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_4():
    x = -5 + 900
    for row in range(30):
        x += 10
        y = -5
        for column in range(30):
            y += 10
            if row % 2 != 0 and column % 2 == 0:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK)


def draw_section_5():
    x=-5
    for row in range(30):
        x += 10
        y = -5 + 300
        for column in range(row):
            y += 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_6():
    x = 15 + 600
    for row in range(31):
        x -= 10
        y = 300 - 5
        for column in range(row):
            y += 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)

def draw_section_7():
    x = 15 + 900
    for row in range(31):
        x -= 10
        y = 600 + 5
        for column in range(row):
            y -= 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def draw_section_8():
    x = -15 + 900
    for row in range(31):
        x += 10
        y = 600 + 5
        for column in range(row):
            y -= 10
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()