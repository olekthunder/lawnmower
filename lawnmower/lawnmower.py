from . import sprites
from .engine import Engine
from .fuel_tank import FuelTank
from .sprite_base import AnimatedSprite


class LawnMower(AnimatedSprite):
    IMAGES = (sprites.LAWNMOVER_DEFAULT, sprites.LAWNMOVER_WORKING)
    DEFAULT_IMAGE = sprites.LAWNMOVER_DEFAULT

    def __init__(self, screen, engine, fuel_tank, *args, **kwargs):
        super().__init__(screen, *args, images=self.IMAGES, **kwargs)
        self.screen = screen
        self.engine = engine
        self.fuel_tank = fuel_tank
        self.parts = [engine, fuel_tank]

    @property
    def acceleration(self):
        return self.engine.acceleration

    @property
    def speed(self):
        return self.engine.speed

    @property
    def working(self):
        return self.engine.working

    @property
    def fuel_consumption(self):
        return self.engine.fuel_consumption

    def turn_on(self):
        print(self.fuel_tank.fuel_left)
        if self.fuel_tank.empty:
            self.engine.turn_on()

    def turn_off(self):
        self.engine.turn_off()
        self.stop_animation()

    def stop(self):
        self.engine.speed = 0

    def increase_speed(self):
        self.engine.increase_speed()

    def decrease_speed(self):
        self.engine.decrease_speed()

    def should_switch_sprite(self, *args, **kwargs):
        return super().should_switch_sprite(*args, **kwargs) and self.working

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        if self.working:
            self.fuel_tank.use(self.fuel_consumption)
        for part in self.parts:
            part.update(*args, **kwargs)
        self.move(self.speed, 0)

    def toggle(self):
        if self.working:
            self.turn_off()
        else:
            self.turn_on()


def get_lawn_mower(screen, *args, **kwargs):
    return LawnMower(
        screen,
        engine=Engine(screen, fuel_consumption=0.1),
        fuel_tank=FuelTank(screen),
        *args, **kwargs
    )
