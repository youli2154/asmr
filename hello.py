import pygame
from gpiozero import MCP3008

pot = MCP3008(0)

# Initialize Pygame
pygame.init()

# Set up the screen - not necessary for audio but helpful for input handling
screen = pygame.display.set_mode((400, 300))

# Load audio files
audio_a = pygame.mixer.Sound("light-rain.mp3")
audio_b = pygame.mixer.Sound("campfire.mp3")
audio_c = pygame.mixer.Sound("thunder-2.mp3")
audio_d = pygame.mixer.Sound("Instrument of Surrender.mp3")

# Set initial volumes
volume_a = 0.5
volume_b = 0.5
volume_c = 0.2
volume_d = 0.5
audio_a.set_volume(volume_a)
audio_b.set_volume(volume_b)
audio_c.set_volume(volume_c)
audio_d.set_volume(volume_d)

# Flags to track which key was pressed last
key_a_pressed = False
key_b_pressed = False
key_c_pressed = False
key_d_pressed = False

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Update key pressed flags
            key_a_pressed = event.key == pygame.K_a
            key_b_pressed = event.key == pygame.K_b
            key_c_pressed = event.key == pygame.K_c
            key_d_pressed = event.key == pygame.K_d

    # Update volume of each audio based on potentiometer value only if its corresponding key is pressed
    if key_a_pressed:
        volume_a = pot.value
        audio_a.set_volume(volume_a)
    elif key_b_pressed:
        volume_b = pot.value
        audio_b.set_volume(volume_b)
    elif key_c_pressed:
        volume_c = pot.value
        audio_c.set_volume(volume_c)
    elif key_d_pressed:
        volume_d = pot.value
        audio_d.set_volume(volume_d)

# Quit Pygame
pygame.quit()
