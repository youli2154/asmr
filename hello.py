import pygame
from gpiozero import MCP3008

pot = MCP3008(channel=0)

# Initialize Pygame and mixer
pygame.init()
pygame.mixer.init()
pygame.mixer.set_num_channels(24)  # Set more channels than the number of sounds

# Set the size of the window
screen_width = 1200
screen_height = 960
screen = pygame.display.set_mode((screen_width, screen_height))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize font
font = pygame.font.Font(None, 40)

# Define two sets of sounds and associate channels for each sound
sound_sets = {
    'O': {
        pygame.K_a: pygame.mixer.Sound("light-rain.mp3"),
        pygame.K_b: pygame.mixer.Sound("waves.mp3"),
        pygame.K_c: pygame.mixer.Sound("underwater.mp3"),
        pygame.K_d: pygame.mixer.Sound("fire.mp3"),
        pygame.K_e: pygame.mixer.Sound("thunder.mp3"),
        pygame.K_f: pygame.mixer.Sound("wind.mp3"),
        pygame.K_g: pygame.mixer.Sound("birds.mp3"),
        pygame.K_h: pygame.mixer.Sound("cricket.mp3"),
        pygame.K_i: pygame.mixer.Sound("frog.mp3"),
        pygame.K_j: pygame.mixer.Sound("cat.mp3"),
        pygame.K_k: pygame.mixer.Sound("temple.mp3"),
        pygame.K_l: pygame.mixer.Sound("muyu.mp3")
    },
    'P': {
        pygame.K_a: pygame.mixer.Sound("cafe.mp3"),
        pygame.K_b: pygame.mixer.Sound("train.mp3"),
        pygame.K_c: pygame.mixer.Sound("bar.mp3"),
        pygame.K_d: pygame.mixer.Sound("typewriter.mp3"),
        pygame.K_e: pygame.mixer.Sound("pencil.mp3"),
        pygame.K_f: pygame.mixer.Sound("clock.mp3"),
        pygame.K_g: pygame.mixer.Sound("subway.mp3"),
        pygame.K_h: pygame.mixer.Sound("arcade.mp3"),
        pygame.K_i: pygame.mixer.Sound("conveniencestore.mp3"),
        pygame.K_j: pygame.mixer.Sound("chimes.mp3"),
        pygame.K_k: pygame.mixer.Sound("footstep.mp3"),
        pygame.K_l: pygame.mixer.Sound("muyu.mp3")
    }
}

# Titles for display based on the sound set
titles_sets = {
    'O': [
        "Rain", "Waves", "Underwater",
        "Fire", "Thunder", "Wind",
        "Bird", "Cricket", "Frog",
        "Cat", "Temple", "Wooden Fish"
    ],
    'P': [
        "Cafe", "Train", "Bar",
        "Typewriter", "Pencil", "Clock",
        "Subway", "Arcade", "711",
        "Chimes", "Footstep", "Wooden Fish"
    ]
}

current_set = 'O'
current_sounds = sound_sets[current_set]
channels = {key: pygame.mixer.Channel(i) for i, key in enumerate(current_sounds.keys())}
current_titles = titles_sets[current_set]
current_audio_key = None

# Initialize volumes for display
volumes_for_display = {key: 0 for key in current_sounds}

# Function to draw the matrix with margin
def draw_matrix(screen, titles, current_key):
    screen.fill(BLACK)
    margin = 20  # Margin of 20 pixels
    grid_width = (screen_width - 2 * margin) // 3
    grid_height = (screen_height - 2 * margin) // 4
    for i, key in enumerate(current_sounds.keys()):
        x = margin + (i % 3) * grid_width + 10
        y = margin + (i // 3) * grid_height + 10
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
                current_titles = titles_sets[current_set]
                channels = {key: pygame.mixer.Channel(i) for i, key in enumerate(current_sounds.keys())}
                volumes_for_display = {key: 0 for key in current_sounds}  # Reset volumes
            if event.key in current_sounds:
                current_audio_key = event.key
                channel = channels[current_audio_key]
                channel.play(current_sounds[current_audio_key], loops=-1)

    if current_audio_key and pot.is_active:
        new_volume = int(pot.value * 100)
        volumes_for_display[current_audio_key] = new_volume
        channels[current_audio_key].set_volume(pot.value)

    # Redraw the GUI with updated volume
    draw_matrix(screen, current_titles, current_audio_key)
    pygame.display.flip()

pygame.quit()
