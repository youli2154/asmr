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

# Set initial volumes
initial_volume = 0.5  # Example initial volume
for sound in audio_files.values():
    sound.set_volume(initial_volume)

# Initialize font
font = pygame.font.Font(None, 24)

# Function to draw the matrix
def draw_matrix(screen, titles):
    screen.fill(BLACK)
    spacing_x = screen_width // 3
    spacing_y = screen_height // 4

    for i, title in enumerate(titles):
        x = (i % 3) * spacing_x + 10  # Position titles in columns
        y = (i // 3) * spacing_y + 10  # Position titles in rows

        # Create the label for each sound
        label = font.render(f"{title}: {int(pot.value * 100)}%", True, WHITE)

        # Draw the label on the screen
        screen.blit(label, (x, y))

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

    # Redraw the GUI with updated volume
    draw_matrix(screen, titles)
    pygame.display.flip()

pygame.quit()
