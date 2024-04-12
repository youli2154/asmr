import pygame
from gpiozero import MCP3008

pot = MCP3008(channel=0)

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(16)  # Ensure there are enough channels

# Set the size of the window
screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize font
font = pygame.font.Font(None, 24)

# Define two sets of sounds
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
        pygame.K_a: pygame.mixer.Sound("light-rain.mp3"),
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

# Titles for display
titles = [
    "rain", "stream", "waves",
    "fire", "thunder", "wind",
    "birds", "cricket", "bell",
    "cafe", "train", "world"
]

current_set = 'O'
current_sounds = sound_sets[current_set]
current_audio = None
current_audio_key = None

# Initialize volumes for display
volumes_for_display = {key: 0 for key in current_sounds}

# Function to draw the matrix
def draw_matrix(screen, titles, current_key):
    screen.fill(BLACK)
    for i, key in enumerate(current_sounds.keys()):
        x = (i % 3) * screen_width // 3 + 10
        y = (i // 3) * screen_height // 4 + 10
        volume_display = volumes_for_display[key]
        label = font.render(f"{titles[i]}: {volume_display}%", True, WHITE)
        screen.blit(label, (x, y))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_o or event.key == pygame.K_p:
                current_set = 'O' if event.key == pygame.K_o else 'P'
                current_sounds = sound_sets[current_set]
                current_audio = None
                current_audio_key = None
                volumes_for_display = {key: 0 for key in current_sounds}  # Reset volumes
            if event.key in current_sounds:
                current_audio_key = event.key
                if current_audio:
                    current_audio.stop()
                current_audio = current_sounds[current_audio_key]
                current_audio.play(-1)  # Play the selected audio in a loop

    # Update volume of the currently selected audio
    if current_audio and current_audio_key is not None:
        new_volume = int(pot.value * 100)
        volumes_for_display[current_audio_key] = new_volume
        current_audio.set_volume(pot.value)

    # Redraw the GUI with updated volume
    draw_matrix(screen, titles, current_audio_key)
    pygame.display.flip()

pygame.quit()
