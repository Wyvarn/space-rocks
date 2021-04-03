import pygame
from utils.asset_utils import load_sprite
from utils.game_utils import get_random_position, print_text
from models.spaceship import Spaceship
from models.asteroid import Asteroid


class SpaceRocks:
    """
    Defines our game
    MIN_ASTEROID_DISTANCE: constant representing an area that has to remain empty.A value of 250 pixels should be enough
    """

    MIN_ASTEROID_DISTANCE = 250

    def __init__(self):
        """
        Initialize the game
        :ivar clock: This allows the speed of the game to be controlled and made constant across all processors &
        machines. This allows us to run with a fixed FPS(Frames Per Second) avoiding a situation where the game is
        harder on some machines & easier on others because the speed of objects is different.

        Bullets are stored in the main game object, represented by the SpaceRocks class. However, the shooting logic
        should be determined by the spaceship. It’s the spaceship that knows how to create a new bullet,
        but it’s the game that stores and later animates the bullets. The Spaceship class needs a way to inform the S
        paceRocks class that a bullet has been created and should be tracked.

        To fix this, a callback function is added to the Spaceship class. That function will be provided by the
        SpaceRocks class when the spaceship is initialized. Every time the spaceship creates a bullet, it will
        initialize a Bullet object and then call the callback. The callback will add the bullet to the list of all
        bullets stored by the game.
        """
        self._init_game()
        self.screen = pygame.display.set_mode((800, 600))
        self.background = load_sprite("space", False)
        self.font = pygame.font.Font(None, 64)
        self.message = ""
        self.clock = pygame.time.Clock()
        self.asteroids = []
        self.bullets = []
        self.spaceship = Spaceship((400, 300), self.bullets.append)

        for _ in range(6):
            while True:
                position = get_random_position(self.screen)

                # if the position of an asteroid is larger than the minimal asteroid distance.
                if position.distance_to(self.spaceship.position) > self.MIN_ASTEROID_DISTANCE:
                    break

            self.asteroids.append(Asteroid(position))

    def _init_game(self):
        pygame.init()
        pygame.display.set_caption("Space Rocks")

    def start_game(self):
        """
        This will start the game.
        Each iteration of this loop(game loop) will generate a single frame of the game.
        Performs:

        1. input handling. Inputs is gathered & handled here, button presses, mouse movements
        2. game engine. Game mechanics/logic/engine. Rules of physics are applied, collisions are detected and handled,
        AI does its thing, etc.
        This part is also responsible for checking if the player has won or lost the game.
        3. drawing. If the game hasn’t ended yet, then this is where the frame will be drawn on screen. 
        It will include all the items that are currently in the game and are visible to the player.
        """
        while True:
            self._handle_input()
            self._game_engine()
            self._draw()

    def _handle_input(self):
        # in each event loop in the game, we get the current event and perform actions based on the event.
        # pygame.event.get() allows us to get events in each frame of the game.
        # These can be used to process any type of event. In this case we exit the game if the user process the
        # ESC button on their keyboard or they exit by closing the game, the X button in the window or pressing
        # ALT + F4 on Windows or Linux or Cmd+W on MacOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            elif self.spaceship and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                self.spaceship.shoot()

        is_key_pressed = pygame.key.get_pressed()

        if self.spaceship:
            if is_key_pressed[pygame.K_RIGHT]:
                self.spaceship.rotate(clockwise=True)
            elif is_key_pressed[pygame.K_LEFT]:
                self.spaceship.rotate(clockwise=False)

            if is_key_pressed[pygame.K_UP]:
                self.spaceship.accelerate()

    def _game_engine(self):
        """
        Handles the game logic
        """

        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.spaceship:
            for asteroid in self.asteroids:
                # If any of the asteroids collides with the spaceship, then the spaceship is destroyed.
                # this setting is represented self.spaceship to None.
                if asteroid.collides_with(self.spaceship):
                    self.spaceship = None
                    self.message = "You lost!"
                    break

        # Notice that instead of using the original list, self.bullets, we create a copy of it using self.bullets[:]
        # That’s because removing elements from a list while iterating over it can cause errors.
        for bullet in self.bullets[:]:
            for asteroid in self.asteroids[:]:
                if asteroid.collides_with(bullet):
                    self.asteroids.remove(asteroid)
                    self.bullets.remove(bullet)
                    break

        for bullet in self.bullets[:]:
            # Surfaces in Pygame have a get_rect() method that returns a rectangle representing their area.
            # That rectangle, in turn, has a collidepoint() method that returns True if a point is included in the
            # rectangle and False otherwise. Using these two methods, you can check if the bullet has left the screen,
            # and if so, remove it from the list.
            if not self.screen.get_rect().collidepoint(bullet.position):
                self.bullets.remove(bullet)

        if not self.asteroids and self.spaceship:
            self.message = "You won!"

    def _draw(self):
        """
        Draws the content on the screen. It is called on every frame to draw the content on the screen.
        self.screen.fill takes a tuple with three values, representing three base colors: red, green, and blue. 
        Each color value ranges between 0 and 255, representing its intensity.
        therefore a tuple of (0, 0, 255) means that the color will consist only of blue, with no traces of red or green

        pygame.display.flip() updates the content of the screen. Because the game will eventually display moving objects
        this method is called on every frame to update the display. Because of this, the screen needs to be filled with
        color every frame,
        as the method will clear the contents generated during the previous frame.
        """
        # use this if you want to fill the background with a color
        # self.screen.fill((0,0, 255))

        # this takes in the surface to draw on & the x,y coordinates to draw on
        # In Pygame, the coordinate system starts in the top-left corner. 
        # The x-axis goes from left to right, and the y-axis goes from top to bottom
        #     -------------> x
        #     ________________________
        #  | |                        |
        #  | |                        |
        #  | |                        |
        #  | |                        |
        #  Y |                        |
        #    |________________________|
        #
        # The UP vector, pointing upwards, will have a negative y-coordinate.
        # The coordinates passed to blit() are given as two values: X and Y. 
        # 
        # They represent the point where the top-left corner of the surface will be located after the operation
        #     ________________________
        #    |         | Big Surface  |
        #    |         |              |
        #    |         | Y            |
        #    | ----> X  ______        |
        #    |         |      |       | 
        #    |         |      |       | 
        #    |         |______|       | 
        #    |        Small surface   |
        #    |________________________|
        # 
        # The top-left corner is moved by the blit coordinates to calculate the correct position.
        # In this case, the new background has the same size as the screen (800 × 600 pixels), 
        # so the coordinates will be (0, 0), representing the top-left corner of the screen. 
        # That way, the background image will cover the entire screen.

        self.screen.blit(self.background, (0, 0))

        for game_object in self._get_game_objects():
            game_object.move(self.screen)

        if self.message:
            print_text(self.screen, self.message, self.font)

        pygame.display.flip()

        # This method will wait long enough to match the desired FPS value, passed as an argument.
        # will control the game and ensure that the game will run at a frame rate of 60 FPS
        self.clock.tick(60)

    def _get_game_objects(self):
        """
        Used by the drawing and moving logic which can later be used to introduce new types of game objects and modify
        only this single method, or you can exclude some objects from this group if necessary.
        """
        game_objects = [*self.asteroids, *self.bullets]

        if self.spaceship:
            game_objects.append(self.spaceship)

        return game_objects
