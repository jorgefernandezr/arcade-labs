# JUEGO DE COMER MOSCAS

import arcade
import random

# Constantes
ESCALAR_RANA = 0.1
ESCALAR_MOSCAS = 0.05
ESCALAR_AGUILAS = 0.4

CONTADOR_MOSCAS = 100
NUMERO_AGUILAS = 2

muerto = 0
ALTURA_PANTALLA = 600
ANCHURA_PANTALLA = 800

class Aguila(arcade.Sprite):

    def update(self):
        self.center_x += 4

        if self.center_x > 800:
            self.center_x = 0


class Mosca(arcade.Sprite):

    def update(self):
        self.center_y -= 1

        if self.center_y < 0:
            self.center_y = ALTURA_PANTALLA


class MyGame(arcade.Window):
    """Clase window"""

    def __init__(self):
        """Inicia"""
        super().__init__(ANCHURA_PANTALLA, ALTURA_PANTALLA, "Juego de la rana")

        # Variable de listas
        self.rana_lista = None
        self.moscas_lista = None
        self.aguila_lista = None

        # Informacion del jugador
        self.rana_sprite = None
        self.aguila_sprite = None
        self.score = 0

        # Para quitar el cusor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def setup(self, y=-150):
        """Inicializa las variables y arranca el juego"""

        # Las listas de los sprites
        self.rana_lista = arcade.SpriteList()
        self.moscas_lista = arcade.SpriteList()
        self.aguila_lista = arcade.SpriteList()

        # Marcador
        self.score = 0

        # Creacion de la rana
        self.rana_sprite = arcade.Sprite("Rana.png", ESCALAR_RANA)  # Para abrir el archivo
        self.rana_sprite.center_y = 50
        self.rana_sprite.center_x = 50
        self.rana_lista.append(self.rana_sprite)  # Para añadir a la rana a la lista

        # Creacion de las moscas
        # Se va a utilizar bucle for para dibujar las 40 moscas
        for i in range(CONTADOR_MOSCAS):
            # Creamos aqui la mosca
            mosca = Mosca("Mosca.png", ESCALAR_MOSCAS)

            # Posicion mosca
            mosca.center_x = random.randrange(ANCHURA_PANTALLA)
            mosca.center_y = random.randrange(ALTURA_PANTALLA)

            # Se añade la mosca a la lista de moscas
            self.moscas_lista.append(mosca)

        # Creacion aguila
        # Se va a utilizar un bucle para dibujar 2 aguilas
        for i in range(NUMERO_AGUILAS):
            aguila = Aguila("Aguila.png", ESCALAR_AGUILAS)

            y += 300
            # Posicion aguila
            aguila.center_x = 0
            aguila.center_y = y

            self.aguila_lista.append(aguila)

    def on_draw(self):
        arcade.start_render()

        # Aqui se pintan las listas
        self.moscas_lista.draw()
        self.rana_lista.draw()
        self.aguila_lista.draw()

        # Texto en la pantalla
        texto = f"Score: {self.score}"
        arcade.draw_text(texto, 10, 20, arcade.color.WHITE, 14)

        if self.score == 100:
            texto = f" HAS GANADO "
            arcade.draw_text(texto, 200, 300, arcade.color.WHITE, 50)
            Aguila.center_x = 0

        if self.muerto == 1:
            texto = f" HAS PERDIDO "
            arcade.draw_text(texto, 200, 300, arcade.color.WHITE, 50)
            Aguila.center_x = 0
            Mosca.center_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        # Para mover la rana
        self.rana_sprite.center_y = y
        self.rana_sprite.center_x = x

    def update(self, delta_time):
        self.moscas_lista.update()
        self.aguila_lista.update()

        # Generar listas para las moscas que chocan con la rana
        moscas_abatidas_lista = arcade.check_for_collision_with_list(self.rana_sprite, self.moscas_lista)
        rana_muerta = arcade.check_for_collision_with_list(self.rana_sprite, self.aguila_lista)
        # Bucle de la mosca añadiendo puntuacion, y quitandola de la lista
        for mosca in moscas_abatidas_lista:
            mosca.remove_from_sprite_lists()
            self.score += 1

        for self.aguila_sprite in rana_muerta:
            self.rana_sprite.remove_from_sprite_lists()
            self.muerto = 1


def main():
    """Metodo Main"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
