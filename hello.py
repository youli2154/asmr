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

# Flags to track which key was pressed last and whether the audio is playing
last_key_pressed = None
audio_playing = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            # Update last_key_pressed only if it's not already set
            if last_key_pressed is None:
                last_key_pressed = event.key
                if event.key == pygame.K_a:
                    audio_playing = audio_a
                    audio_a.play(-1)
                elif event.key == pygame.K_b:
                    audio_playing = audio_b
                    audio_b.play(-1)
                elif event.key == pygame.K_c:
                    audio_playing = audio_c
                    audio_c.play(-1)
                elif event.key == pygame.K_d:
                    audio_playing = audio_d
                    audio_d.play(-1)

    # Update volume of the playing audio based on potentiometer value only if its corresponding key is pressed
    if audio_playing:
        if last_key_pressed == pygame.K_a:
            volume_a = pot.value
            audio_a.set_volume(volume_a)
        elif last_key_pressed == pygame.K_b:
            volume_b = pot.value
            audio_b.set_volume(volume_b)
        elif last_key_pressed == pygame.K_c:
            volume_c = pot.value
            audio_c.set_volume(volume_c)
        elif last_key_pressed == pygame.K_d:
            volume_d = pot.value
            audio_d.set_volume(volume_d)

    # Check if any key is pressed to stop updating volume
    keys = pygame.key.get_pressed()
    if any(keys):
        last_key_pressed = None

# Quit Pygame
pygame.quit()
