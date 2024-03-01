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

# Variable to track which audio key is pressed
current_audio = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                current_audio = audio_a
            elif event.key == pygame.K_b:
                current_audio = audio_b
            elif event.key == pygame.K_c:
                current_audio = audio_c
            elif event.key == pygame.K_d:
                current_audio = audio_d
                
            elif event.key == pygame.K_z:
                audio_a.set_volume(0)
                audio_b.set_volume(0)
                audio_c.set_volume(0)
                current_audio = None

    # Update volume of the current audio based on potentiometer value
    if current_audio is not None:
        current_audio.set_volume(pot.value)

# Quit Pygame
pygame.quit()
