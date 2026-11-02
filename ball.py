from pico2d import get_canvas_width, load_image


class Ball:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.image = load_image('ball21x21.png')
        self.is_out = False

    def update(self):
        self.x += self.direction * 10
        self.is_out = self.x < -11 or self.x > get_canvas_width() + 11

    def draw(self):
        self.image.draw(self.x, self.y, 21, 21)
