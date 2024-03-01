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

# Main loop
running = True
while running:
    #print(pot.value)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                audio_a.play(-1)
                audio_a.set_volume(volume_a)
            elif event.key == pygame.K_b:
                audio_b.play(-1)
            elif event.key == pygame.K_c:
                audio_c.play(-1)
            elif event.key == pygame.K_d:
                audio_d.play(-1)
                
            elif event.key == pygame.K_i:
                volume_a = pot.value
                audio_a.set_volume(volume_a)
                print(volume_a)
            elif event.key == pygame.K_j:
                volume_a = max(0.0, volume_a - 0.05)
                audio_a.set_volume(volume_a)

            elif event.key == pygame.K_m:
                volume_b = min(1.0, volume_b + 0.05)
                audio_b.set_volume(volume_b)
            elif event.key == pygame.K_n:
                volume_b = min(1.0, volume_b - 0.05)
                audio_b.set_volume(volume_b)

            elif event.key == pygame.K_t:
                volume_c = min(1.0, volume_c + 0.05)
                audio_c.set_volume(volume_c)
            elif event.key == pygame.K_y:
                volume_c = max(0.0, volume_c - 0.05)
                audio_c.set_volume(volume_c)

            elif event.key == pygame.K_u:
                volume_d = min(1.0, volume_d + 0.05)
                audio_d.set_volume(volume_d)
            elif event.key == pygame.K_v:
                volume_d = max(0.0, volume_d - 0.05)
                audio_d.set_volume(volume_d)

            elif event.key == pygame.K_z:
                audio_a.set_volume(0)
                audio_b.set_volume(0)
                audio_c.set_volume(0)

# Quit Pygame
pygame.quit()
