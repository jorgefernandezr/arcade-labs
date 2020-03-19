import arcade


class Juego:
    def __init__(self, position_x, position_y):

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y


    def persona(self):
        arcade.draw_lrtb_rectangle_filled(self.position_x, self.position_x + 1, self.position_y + 25, self.position_y - 25, arcade.color.BLACK)
        arcade.draw_rectangle_filled(self.position_x + 11, self.position_y + 15, 25, 2, arcade.color.BLACK, 330)
        arcade.draw_rectangle_filled(self.position_x - 11, self.position_y + 15, 25, 2, arcade.color.BLACK, 30)
        arcade.draw_rectangle_filled(self.position_x + 6, self.position_y - 36, 25, 2, arcade.color.BLACK, 300)
        arcade.draw_rectangle_filled(self.position_x - 6, self.position_y - 36, 25, 2, arcade.color.BLACK, 60)
        arcade.draw_circle_filled(self.position_x, self.position_y + 29, 8, arcade.color.BLACK)


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        # Create our ball
        self.juego = Juego(0,0)

    def cesped(self):
        # Cesped
        arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.GREEN)

    def casa(self):
        # Casa
        arcade.draw_lrtb_rectangle_filled(100, 400, 400, 150, arcade.color.SAND)  # Estructura de la casa
        arcade.draw_lrtb_rectangle_filled(350, 400, 500, 400, arcade.color.SAND)
        arcade.draw_triangle_filled(50, 400, 450, 400, 250, 550, arcade.color.RED)
        arcade.draw_lrtb_rectangle_filled(335, 415, 525, 500, arcade.color.SAND)

        # Ventana izquierda
        arcade.draw_lrtb_rectangle_filled(150, 200, 350, 300, arcade.color.LIGHT_GRAY)
        arcade.draw_lrtb_rectangle_filled(149, 151, 350, 300, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(199, 201, 350, 300, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(150, 200, 351, 349, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(150, 200, 301, 299, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(173, 177, 350, 300, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(150, 200, 327, 323, arcade.color.BROWN)

        # Ventana derecha
        arcade.draw_lrtb_rectangle_filled(300, 350, 350, 300, arcade.color.LIGHT_GRAY)
        arcade.draw_lrtb_rectangle_filled(299, 301, 350, 300, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(349, 351, 350, 300, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(300, 350, 351, 349, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(300, 350, 301, 299, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(300, 350, 327, 323, arcade.color.BROWN)
        arcade.draw_lrtb_rectangle_filled(323, 327, 350, 300, arcade.color.BROWN)

        # Puerta
        arcade.draw_lrtb_rectangle_filled(200, 250, 250, 150, arcade.color.BROWN)
        arcade.draw_circle_filled(205, 200, 3, arcade.color.YELLOW)

    def sol(self):
        arcade.draw_circle_filled(700, 500, 25, arcade.color.YELLOW)


    def on_draw(self):
        arcade.start_render()

        self.cesped()
        self.sol()  # Sol
        self.casa()

        self.juego.persona()


    def on_mouse_motion(self, x, y, dx, dy):
        self.juego.position_x = x
        self.juego.position_y = y


def main():
    window = MyGame(800, 600, "La Casa")
    arcade.run()


main()