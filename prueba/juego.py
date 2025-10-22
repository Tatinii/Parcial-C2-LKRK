import arcade
import math

# --- Constantes del Juego ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Lleva el Círculo al Objetivo"

PLAYER_RADIUS = 25
TARGET_RADIUS = 50

PLAYER_SPEED = 20  # Velocidad de movimiento del jugador

# --- Clases del Juego ---


class Game(arcade.Window):
    """
    Clase principal del juego.
    """

    def __init__(self, width, height, title):
        """ Inicializador de la ventana """
        super().__init__(width, height, title)

        arcade.set_background_color((0, 0, 0))  

        # Variables para la posición del jugador
        self.player_x = SCREEN_WIDTH // 4
        self.player_y = SCREEN_HEIGHT // 2

        # Posición del círculo objetivo (fijo)
        self.target_x = SCREEN_WIDTH - (SCREEN_WIDTH // 4)
        self.target_y = SCREEN_HEIGHT // 2

        # Estado del juego
        self.game_over = False

    def on_draw(self):
        """
        Método para dibujar en la pantalla.
        """
        self.clear()

        # Dibuja el círculo del jugador (relleno)
        arcade.draw_circle_filled(
            self.player_x,
            self.player_y,
            PLAYER_RADIUS,
            (255,255,255),
        )

        # Dibuja el círculo objetivo (solo borde)
        arcade.draw_circle_outline(
            self.target_x,
            self.target_y,
            TARGET_RADIUS,
            arcade.color.BLUE,
            border_width=3,  # Ancho del borde
        )

        # Si el juego ha terminado, muestra el mensaje de victoria
        if self.game_over:
            arcade.draw_text(
                "¡Ganaste!",
                SCREEN_WIDTH / 2,
                SCREEN_HEIGHT / 1.2,
                (0,255,0),
                font_size=50,
                anchor_x="center",
                anchor_y="center",
            )

    def on_update(self, delta_time):
        """
        Lógica de actualización del juego. Se ejecuta 60 veces por segundo.
        delta_time: tiempo transcurrido desde la última actualización.
        """
        if self.game_over:
            return  # Si el juego terminó, no actualizamos nada más

        # Limitar la posición del jugador dentro de la pantalla
        self.player_x = max(PLAYER_RADIUS, min(self.player_x, SCREEN_WIDTH - PLAYER_RADIUS))
        self.player_y = max(PLAYER_RADIUS, min(self.player_y, SCREEN_HEIGHT - PLAYER_RADIUS))

        # Comprobar colisión entre el jugador y el objetivo
        # Usamos la fórmula de distancia: raíz_cuadrada((x2-x1)^2 + (y2-y1)^2)
        delta_x = self.player_x - self.target_x
        delta_y = self.player_y - self.target_y
        distance = math.sqrt(delta_x ** 2 + delta_y ** 2)

        # Si la distancia entre los centros es menor o igual a la suma de sus radios, hay colisión
        if distance <= (PLAYER_RADIUS + TARGET_RADIUS):
            self.game_over = True  # ¡El jugador ganó!

    def on_key_press(self, key, modifiers):
        """
        Se llama cuando el usuario presiona una tecla.
        """
        if self.game_over:
            return

        if key == arcade.key.W or key == arcade.key.UP:
            self.player_y += PLAYER_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.player_y -= PLAYER_SPEED
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.player_x -= PLAYER_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.player_x += PLAYER_SPEED
        elif key == arcade.key.ESCAPE:
            arcade.close_window()

# --- Ejecución del Juego ---
game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
