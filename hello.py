import pygame
from gpiozero import MCP3008

pot = MCP3008(channel=0)

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(16)  # Ensure enough channels for simultaneous playback

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
current_channels = {key: pygame.mixer.Channel(index) for index, key in enumerate(current_sounds.keys())}
current_audio = None
current_audio_key = None
title_keys = list(current_sounds.keys())

# Initialize volumes for display
volumes_for_display = {key: 0 for key in title_keys}

# Function to draw the matrix
def draw_matrix(screen, titles, current_key):
    screen.fill(BLACK)
    spacing_x = screen_width // 3
    spacing_y = screen_height // 4
    for i, title in enumerate(titles):
        x = (i % 3) * spacing_x + 10
        y = (i // 3) * spacing_y + 10
        key = title_keys[i]
        volume_display = volumes_for_display[key]
        label = font.render(f"{title}: {volume_display}%", True, WHITE)
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
                title_keys = list(current_sounds.keys())
                current_channels = {key: pygame.mixer.Channel(index) for index, key in enumerate(title_keys)}
            elif event.key in current_sounds:
                channel = current_channels[event.key]
                if not channel.get_busy():
                    channel.play(current_sounds[event.key], loops=-1)

    # Continuously update the volume of the currently selected audio
    new_volume = int(pot.value * 100)
    for key in current_sounds:
        channel = current_channels[key]
        if channel.get_busy():
            channel.set_volume(pot.value)
        volumes_for_display[key] = new_volume

    # Redraw the GUI with updated volume
    draw_matrix(screen, titles, current_set)
    pygame.display.flip()

pygame.quit()
