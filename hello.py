import pygame
from gpiozero import MCP3008

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

# Titles for display
titles = [
    "rain", "stream", "waves",
    "fire", "thunder", "wind",
    "birds", "cricket", "bell",
    "cafe", "train", "world"
]

# Map titles to keys for volume display
title_keys = list(sound_sets.keys())

# Initialize font
font = pygame.font.Font(None, 24)

# Define sound sets for O, P, Q
sound_sets = {
    'O': {
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
    },
    'P': {
        pygame.K_a: pygame.mixer.Sound("light-rain.mp3"),  # Replace 'a.mp3' with the actual sound paths for set P
        pygame.K_b: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_c: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_d: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_e: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_f: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_g: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_h: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_i: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_j: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_k: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_l: pygame.mixer.Sound("light-rain.mp3")
    },
    'Q': {
        pygame.K_a: pygame.mixer.Sound("light-rain.mp3"),  # Same placeholder sound files for set Q
        pygame.K_b: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_c: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_d: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_e: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_f: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_g: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_h: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_i: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_j: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_k: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_l: pygame.mixer.Sound("light-rain.mp3")
    }
}

# Current sound set, starting with 'O'
current_set = 'O'
current_sounds = sound_sets[current_set]
current_audio = None

# Function to draw the matrix
def draw_matrix(screen, titles, current_key):
    screen.fill(BLACK)
    spacing_x = screen_width // 3
    spacing_y = screen_height // 4

    for i, title in enumerate(titles):
        x = (i % 3) * spacing_x + 10  # Position titles in columns
        y = (i // 3) * spacing_y + 10  # Position titles in rows

        # Create the label for each sound
        label = font.render(f"{title}: {volumes_for_display[title_keys[i]]}%", True, WHITE)

        # Draw the label on the screen
        screen.blit(label, (x, y))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o:
                current_set = 'O'
                current_sounds = sound_sets[current_set]
            elif event.key == pygame.K_p:
                current_set = 'P'
                current_sounds = sound_sets[current_set]
            elif event.key == pygame.K_q:
                current_set = 'Q'
                current_sounds = sound_sets[current_set]

            # Check if the pressed key corresponds to a sound in the current set
            if event.key in current_sounds:
                if current_audio:
                    current_audio.stop()
                current_audio = current_sounds[event.key]
                current_audio.play(-1)  # Play the selected audio in a loop

    # Redraw the GUI with updated volume
    draw_matrix(screen, titles, current_audio_key)
    pygame.display.flip()

pygame.quit()
