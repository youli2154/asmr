import pygame
from gpiozero import MCP3008

pot = MCP3008(channel=0)

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()

# Load audio files
audio_files = {
    pygame.K_a: pygame.mixer.Sound("light-rain.mp3"),
    pygame.K_b: pygame.mixer.Sound("stream.mp3"),
    pygame.K_c: pygame.mixer.Sound("wave.mp3"),
    pygame.K_d: pygame.mixer.Sound("fire.mp3"),
    pygame.K_e: pygame.mixer.Sound("thunder-2.mp3"),
    pygame.K_f: pygame.mixer.Sound("wind.mp3"),
    pygame.K_g: pygame.mixer.Sound("birds.mp3"),
    pygame.K_h: pygame.mixer.Sound("cricket.mp3"),
    pygame.K_i: pygame.mixer.Sound("train.mp3"),
    pygame.K_d: pygame.mixer.Sound("Instrument of Surrender.mp3")

}

# Set initial volumes
initial_volume = 0.5  # Example initial volume
for sound in audio_files.values():
    sound.set_volume(initial_volume)

# Variable to keep track of which audio is currently being volume-controlled
current_audio = None

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in audio_files:
                if current_audio is not audio_files[event.key]:  # If a new audio is selected
                    current_audio = audio_files[event.key]
                    current_audio.play(-1)  # Play the selected audio in a loop

    # Continuously update the volume of the currently selected audio
    if current_audio:
        new_volume = pot.value  # Read potentiometer value
        current_audio.set_volume(new_volume)

pygame.quit()
