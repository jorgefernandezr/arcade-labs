"""
Este es un dibujo
"""

import arcade
import random


def cesped():
    # Cesped
    arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.GREEN)


def casa():
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


def persona(x, y):
    arcade.draw_lrtb_rectangle_filled(600 + x, 601 + x, 225 + y, 175 + y, arcade.color.BLACK)
    arcade.draw_rectangle_filled(611 + x, 215 + y, 25, 2, arcade.color.BLACK, 330)
    arcade.draw_rectangle_filled(589 + x, 215 + y, 25, 2, arcade.color.BLACK, 30)
    arcade.draw_rectangle_filled(606 + x, 166 + y, 25, 2, arcade.color.BLACK, 300)
    arcade.draw_rectangle_filled(594 + x, 166 + y, 25, 2, arcade.color.BLACK, 60)
    arcade.draw_circle_filled(600 + x, 229 + y, 8, arcade.color.BLACK)


def sol(x, y):
    arcade.draw_circle_filled(-50 + x, 500 + y, 25, arcade.color.YELLOW)


def luna(x, y):
    arcade.draw_circle_filled(-50 + x, 500 + y, 25, arcade.color.WHITE)


def bucle_sol_luna():
    if dibujar.movimiento_luna == (850):
        dibujar.movimiento_sol = 0
        sol(dibujar.movimiento_sol, 0)

    elif dibujar.movimiento_sol == (850):
        dibujar.movimiento_luna = 0
        luna(dibujar.movimiento_luna, 0)


def dia_mediodia_noche():
    if dibujar.movimiento_sol == (000 or 800):
        arcade.set_background_color(arcade.color.ORANGE)

    elif dibujar.movimiento_sol == 50:
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    elif dibujar.movimiento_luna == 100:
        arcade.set_background_color(arcade.color.BLACK)

    elif dibujar.movimiento_luna == 800:
        arcade.set_background_color(arcade.color.ORANGE)


def dibujar(tiempo):
    arcade.start_render()

    sol(dibujar.movimiento_sol, 0)  # Sol
    luna(dibujar.movimiento_luna, 0)
    cesped()  # Cesped

    casa()  # Casa
    persona(dibujar.movimiento_persona, -10)  # Persona
    bucle_sol_luna()

    dia_mediodia_noche()

    dibujar.movimiento_sol += 10
    dibujar.movimiento_luna += 10
    dibujar.movimiento_persona += -3


def main():
    # Para abrir el programa
    arcade.open_window(800, 600, "Ejemplo")
    arcade.set_background_color(arcade.color.ORANGE)
    arcade.schedule(dibujar, 1 / 60)

    # Cierre
    arcade.finish_render()
    arcade.run()


# Programa principal
dibujar.movimiento_luna = -850
dibujar.movimiento_sol = 0
dibujar.movimiento_persona = 0
main()
