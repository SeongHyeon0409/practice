import pygame

class Snake:
  def __init__(self, position):
    self.position = pygame.Rect(position, (10, 10))
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]

  def create_snake(self):
    for i in range(10):
      self.segments.append(pygame.Rect(self.position, (10, 10)))

  def move(self, direction):
    if direction == "left":
      self.position.x -= 10
    elif direction == "right":
      self.position.x += 10
    elif direction == "up":
      self.position.y -= 10
    elif direction == "down":
      self.position.y += 10

  def draw(self, screen):
    for segment in self.segments:
      pygame.draw.rect(screen, (0, 255, 0), segment)

def main():
  pygame.init()
  screen = pygame.display.set_mode((600, 400))
  snake = Snake((300, 200))

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()

    direction = None
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        direction = "left"
      elif event.key == pygame.K_RIGHT:
        direction = "right"
      elif event.key == pygame.K_UP:
        direction = "up"
      elif event.key == pygame.K_DOWN:
        direction = "down"

    if direction is not None:
      snake.move(direction)

    screen.fill((0, 0, 0))
    snake.draw(screen)
    pygame.display.update()
if __name__ == "__main__":
  main()