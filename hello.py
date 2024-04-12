import pygame
from gpiozero import MCP3008

pot = MCP3008(channel=0)

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(16)

# Set the size of the window
screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Load audio files
audio_files = {
    pygame.K_a: pygame.mixer.Sound("light-rain.mp3"),
    pygame.K_b: pygame.mixer.Sound("stream.mp3"),
    pygame.K_c: pygame.mixer.Sound("waves.mp3"),
    pygame.K_d: pygame.mixer.Sound("fire.mp3"),
    pygame.K_e: pygame.mixer.Sound("thunder-2.mp3"),
    pygame.K_f: pygame.mixer.Sound("wind.mp3"),
    pygame.K_g: pygame.mixer.Sound("birds.mp3"),
    pygame.K_h: pygame.mixer.Sound("cricket.mp3"),
    pygame.K_i: pygame.mixer.Sound("bowl.mp3"),
    pygame.K_j: pygame.mixer.Sound("cafe.mp3"),
    pygame.K_k: pygame.mixer.Sound("train.mp3"),
    pygame.K_l: pygame.mixer.Sound("Instrument of Surrender.mp3")
}

# Titles for display
titles = [
    "rain", "stream", "waves",
    "fire", "thunder", "wind",
    "birds", "cricket", "bell",
    "cafe", "train", "world"
]

# Map titles to keys for volume display
title_keys = list(audio_files.keys())

# Initialize font
font = pygame.font.Font(None, 24)

# Initialize volumes for display
volumes_for_display = {key: 0 for key in audio_files}  # All volumes start at 0%

# Function to draw the matrix
def draw_matrix(screen, titles, volumes_for_display, current_key):
    screen.fill(BLACK)
    spacing_x = screen_width // 3
    spacing_y = screen_height // 4

    for i, title in enumerate(titles):
        x = (i % 3) * spacing_x + 10  # Position titles in columns
        y = (i // 3) * spacing_y + 10  # Position titles in rows

        # Get the corresponding key for the title
        key = title_keys[i]
        
        # Display volume only for the current active track
        volume_display = volumes_for_display[key] if key == current_key else 0
        
        # Create the label for each sound
        label = font.render(f"{title}: {volume_display}%", True, WHITE)

        # Draw the label on the screen
        screen.blit(label, (x, y))

# Variable to keep track of which audio key is currently being volume-controlled
current_audio_key = None
current_audio = None  # Variable to keep track of the currently playing audio

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key in audio_files:
                current_audio_key = event.key  # Update the current key
                if current_audio is not audio_files[event.key]:  # If a new audio is selected
                    if current_audio:
                        current_audio.stop()  # Stop the previous audio
                    current_audio = audio_files[event.key]
                    current_audio.play(-1)  # Play the selected audio in a loop

    # Continuously update the volume of the currently selected audio
    if current_audio and current_audio_key is not None:
        new_volume = int(pot.value * 100)  # Convert potentiometer value to percentage
        volumes_for_display[current_audio_key] = new_volume  # Update only the current audio's volume for display
        current_audio.set_volume(pot.value)  # Set the actual volume

    # Redraw the GUI with updated volume
    draw_matrix(screen, titles, volumes_for_display, current_audio_key)
    pygame.display.flip()

pygame.quit()
