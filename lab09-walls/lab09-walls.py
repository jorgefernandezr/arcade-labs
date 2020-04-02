# Imports
import arcade
import random
import os

# Declaracion de variables

ANCHURA_PANTALLA = 800
ALTURA_PANTALLA = 800
TITULO = "El juego de los Muros"

# Movimiento del personaje
MOVIMIENTO = 8

# Margen del jugador para moverse y verle
MARGEN = 40
MUERTE = 0

# Escalar monedas
ESCALAR_MONEDA = 0.2

# Numero de monedas
NUMERO_MONEDAS = 75
PINCHOS_X = 50
PINCHOS_Y = 50


class MyGame(arcade.Window):
    """Clase principal del programa"""

    def __init__(self, anchura, altura, titulo):
        # Inicia el programa
        # Constructor
        super().__init__(anchura, altura, titulo)

        self.lista_pinchos = arcade.SpriteList()
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Lista de Sprite
        self.lista_moneda = None
        self.lista_muro = None
        self.lista_jugador = None
        self.lista_moneda = None

        # Iniciar al jugador
        self.sprite_jugador = None
        self.fisicas = None
        self.contador = 0

        # Iniciamos el comando view
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        # Listas de Sprite, iniciar
        self.lista_jugador = arcade.SpriteList()
        self.lista_muro = arcade.SpriteList()
        self.lista_moneda = arcade.SpriteList()
        self.lista_pinchos = arcade.SpriteList()
        self.sonido_moneda = arcade.load_sound("SonidoMoneda.m4a")
        self.sonido_perder = arcade.load_sound("perdedor.mp3")
        self.sonido_ganar = arcade.load_sound("ganador.mp3")

        # Iniciar al jugador
        self.sprite_jugador = arcade.Sprite("persona.png", 0.5)

        # Posicion del jugador y se añade a la lista
        self.sprite_jugador.center_x = 120
        self.sprite_jugador.center_y = 120
        self.lista_jugador.append(self.sprite_jugador)

        # Creacion de los muros
        # En horizontal
        x = -3000
        for y in range(0, 2):
            x += 3000
            for y in range(0, 3064, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = x
                self.lista_muro.append(muro)

            for y in range(0, 3064, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = x
                muro.center_y = y
                self.lista_muro.append(muro)
        x2 = -1200
        for y in range(0, 3):
            x2 += 1200
            for y in range(0, 1024, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = 300 + x2
                self.lista_muro.append(muro)
            for y in range(1100, 3064, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = 300 + x2
                self.lista_muro.append(muro)
            for y in range(0, 2014, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = 600 + x2
                self.lista_muro.append(muro)
            for y in range(2124, 3064, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = 600 + x2
                self.lista_muro.append(muro)
            for y in range(0, 760, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = 900 + x2
                self.lista_muro.append(muro)
            for y in range(860, 3064, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = 900 + x2
                self.lista_muro.append(muro)
            for y in range(0, 2450, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = 1200 + x2
                self.lista_muro.append(muro)
            for y in range(2550, 3064, 64):
                muro = arcade.Sprite("muros.jpg", 0.04)
                muro.center_x = y
                muro.center_y = 1200 + x2
                self.lista_muro.append(muro)

        # Colocacion de pinchos
        j = 0
        for i in range (0, 9):
            j += 300
            z = 0
            for y in range(0, 6):
                z += 500
                for y in range(0, 1024, 64):
                    self.pincho = arcade.Sprite("estalagnitas.png", 0.08)
                    self.pincho.center_x = -100 + z
                    self.pincho.center_y = 50 + j
                    self.lista_pinchos.append(self.pincho)
                for y in range(0, 1024, 64):
                    self.pincho = arcade.Sprite("estalactitas.png", 0.08)
                    self.pincho.center_x = -300 + z
                    self.pincho.center_y = 250 + j
                    self.lista_pinchos.append(self.pincho)

        # Colocacion de monedas
        for i in range(NUMERO_MONEDAS):

            moneda = arcade.Sprite("moneda.png",ESCALAR_MONEDA)

            moneda_bien_colocada = False
            while not moneda_bien_colocada:
                moneda.center_x = random.randrange(3000)
                moneda.center_y = random.randrange(3000)

                moneda_choca_moneda = arcade.check_for_collision_with_list(moneda, self.lista_moneda)
                muro_choca_moneda = arcade.check_for_collision_with_list(moneda, self.lista_muro)
                moneda_choca_pincho = arcade.check_for_collision_with_list(moneda, self.lista_pinchos)

                if len(muro_choca_moneda) == 0 and len(moneda_choca_moneda) == 0 and len(moneda_choca_pincho) == 0:
                    moneda_bien_colocada = True


            self.lista_moneda.append(moneda)

        # Son las fisicas del juego por el cual el personaje no puede
        # atravesar los muros
        self.fisicas = arcade.PhysicsEngineSimple(self.sprite_jugador, self.lista_muro)

        # Color de fondo
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):

        # Renderiza
        arcade.start_render()

        # Hace el dibujo
        self.lista_muro.draw()
        self.lista_jugador.draw()
        self.lista_moneda.draw()
        self.lista_pinchos.draw()

        if self.contador == 75:
            texto = f" HAS GANADO "
            arcade.draw_text(texto, 0, 2000, arcade.color.WHITE, 400)
            texto = f"Contador:  {self.contador}"
            arcade.draw_text(texto, 50, 1000, arcade.color.WHITE, 400)
            arcade.play_sound(self.sonido_ganar)

        if self.MUERTE == 1:
            texto =f" HAS PERDIDO "
            arcade.draw_text(texto, 0, 2000, arcade.color.WHITE, 400)
            texto = f"Contador:  {self.contador}"
            arcade.draw_text(texto, 50, 1000, arcade.color.WHITE, 400)
            arcade.set_viewport(0, 3000, 0, 3000)

    def on_key_press(self, tecla, modificador):
        """Pulsar tecla para moverse"""

        # La tecla que pulsas hace este movimiento
        if tecla == arcade.key.UP:
            self.sprite_jugador.change_y = MOVIMIENTO
        if tecla == arcade.key.DOWN:
            self.sprite_jugador.change_y = -MOVIMIENTO
        if tecla == arcade.key.LEFT:
            self.sprite_jugador.change_x = -MOVIMIENTO
        if tecla == arcade.key.RIGHT:
            self.sprite_jugador.change_x = MOVIMIENTO

    def on_key_release(self, tecla, modificacion):

        # Cuando el jugador suelta la tecla para que no se produzca movimiento
        if tecla == arcade.key.UP or tecla == arcade.key.DOWN:
            self.sprite_jugador.change_y = 0
        elif tecla == arcade.key.LEFT or tecla == arcade.key.RIGHT:
            self.sprite_jugador.change_x = 0

    def on_update(self, delta_time):

        # Actualiza
        self.fisicas.update()

        persona_choca_pincho = arcade.check_for_collision_with_list(self.sprite_jugador, self.lista_pinchos)
        monedas_conseguidas = arcade.check_for_collision_with_list(self.sprite_jugador, self.lista_moneda)
        for moneda in monedas_conseguidas:
            moneda.remove_from_sprite_lists()
            self.contador += 1
            arcade.play_sound(self.sonido_moneda)

        for self.pincho in persona_choca_pincho:
            self.sprite_jugador.remove_from_sprite_lists()
            self.sprite_jugador.change_x = 0
            self.sprite_jugador.change_y = 0
            self.MUERTE = 1

        cambio = False

        # Scroll left
        borde_izquierdo = self.view_left + MARGEN
        if self.sprite_jugador.left < borde_izquierdo:
            self.view_left -= borde_izquierdo - self.sprite_jugador.left
            cambio = True

        # Scroll right
        borde_derecho = self.view_left + ANCHURA_PANTALLA - MARGEN
        if self.sprite_jugador.right > borde_derecho:
            self.view_left += self.sprite_jugador.right - borde_derecho
            cambio = True

        # Scroll up
        borde_arriba = self.view_bottom + ALTURA_PANTALLA - MARGEN
        if self.sprite_jugador.top > borde_arriba:
            self.view_bottom += self.sprite_jugador.top - borde_arriba
            cambio = True

        # Scroll down
        borde_abajo = self.view_bottom + MARGEN
        if self.sprite_jugador.bottom < borde_abajo:
            self.view_bottom -= borde_abajo - self.sprite_jugador.bottom
            cambio = True

        self.view_left = int(self.view_left)
        self.view_bottom = int(self.view_bottom)

        # If we changed the boundary values, update the view port to match

        """arcade.set_viewport(0, 3000, 0, 3000)"""

        if cambio and self.contador < 75 and MUERTE == 0:
            arcade.set_viewport(self.view_left,
                                ANCHURA_PANTALLA + self.view_left - 1,
                                self.view_bottom,
                                ALTURA_PANTALLA + self.view_bottom - 1)

        if cambio and self.contador == 75:
            arcade.set_viewport(0, 3000, 0, 3000)
        if cambio and MUERTE==1:
            arcade.set_viewport(0, 3000, 0, 3000)



def main():
    """Metodo main"""
    window = MyGame(ANCHURA_PANTALLA, ALTURA_PANTALLA, TITULO)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
