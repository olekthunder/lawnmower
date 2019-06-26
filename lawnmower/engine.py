from .sprite_base import SpriteBase


class Engine(SpriteBase):
    MAX_SPEED = 32

    def __init__(self, screen, fuel_consumption, *args, **kwargs):
        super().__init__(screen, *args, **kwargs)
        self.working = False
        self.fuel_consumption = fuel_consumption
        self.speed = 0
        self.acceleration = 2

    def turn_on(self):
        self.working = True

    def turn_off(self):
        self.working = False

    def stop(self):
        self.speed = 0

    def increase_speed(self):
        new_speed = self.speed + self.acceleration
        if new_speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED
        else:
            self.speed = new_speed

    def decrease_speed(self):
        new_speed = self.speed - self.acceleration
        if new_speed < -self.MAX_SPEED:
            self.speed = -self.MAX_SPEED
        else:
            self.speed = new_speed
