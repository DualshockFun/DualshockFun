import pygame
import time

pygame.init()

pygame.joystick.init()

joystick_count = pygame.joystick.get_count()

if joystick_count == 0:
    pygame.quit()
    quit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Using joystick: {joystick.get_name()}")
print(f"Number of axes: {joystick.get_numaxes()}")
print(f"Number of buttons: {joystick.get_numbuttons()}")
print(f"Number of hats: {joystick.get_numhats()}")

try:
    joystick.rumble(0.0, 0.0, 100)
    print("Rumble is supported")
except AttributeError:
    print("Rumble is not supported on this controller")
    pygame.quit()
    quit()
except Exception as e:
    print(f"An error occurred: {e}")
    pygame.quit()
    quit()

def rumble_controller():
    try:
        joystick.rumble(1.0, 1.0, 1000)
        print("Rumble started at max strength")
    except Exception as e:
        print(f"Failed to rumble: {e}")

try:
    while True:
        rumble_controller()
        time.sleep(0.9)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                raise KeyboardInterrupt

except KeyboardInterrupt:
    joystick.stop_rumble()
    pygame.quit()
    print("Rumble stopped and Pygame quit.")
