import pygame
from gpiozero import MCP3008

pot = MCP3008(channel=0)

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(24)  # Adjust number of channels based on need

# Set the size of the window
screen_width = 600
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize font
font = pygame.font.Font(None, 24)

# Define two sets of sounds and create channels for each sound
sound_sets = {
    'O': {key: pygame.mixer.Sound(sound_file) for key, sound_file in zip(
        [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l],
        ["light-rain.mp3", "stream.mp3", "waves.mp3", "fire.mp3", "thunder-2.mp3", "wind.mp3", "birds.mp3", "cricket.mp3", "bowl.mp3", "cafe.mp3", "train.mp3", "Instrument of Surrender.mp3"])},
    'P': {key: pygame.mixer.Sound("light-rain.mp3") for key in
          [pygame.K_a, pygame.K_b, pygame.K_c, pygame.K_d, pygame.K_e, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_i, pygame.K_j, pygame.K_k, pygame.K_l]}
}

# Map of keys to channels
channels = {key: pygame.mixer.Channel(index) for index, key in enumerate(sound_sets['O'])}

# Titles for display
titles = [
    "rain", "stream", "waves",
    "fire", "thunder", "wind",
    "birds", "cricket", "bell",
    "cafe", "train", "world"
]

current_set = 'O'
current_sounds = sound_sets[current_set]
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
                channels = {key: pygame.mixer.Channel(index) for index, key in enumerate(current_sounds)}  # Reset channels
                volumes_for_display = {key: 0 for key in current_sounds}  # Reset volumes
            elif event.key in current_sounds:
                current_audio_key = event.key
                channel = channels[current_audio_key]
                if not channel.get_busy():
                    channel.play(current_sounds[current_audio_key], -1)

    # Update volume of the currently selected audio
    if current_audio_key and event.type == pygame.KEYDOWN and event.key in current_sounds:
        channel = channels[current_audio_key]
        new_volume = int(pot.value * 100)
        volumes_for_display[current_audio_key] = new_volume
        channel.set_volume(pot.value)

    # Redraw the GUI with updated volume
    draw_matrix(screen, titles, current_audio_key)
    pygame.display.flip()

pygame.quit()
