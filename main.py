import time
import argparse
import pygame
import os

# Window configuration
WINDOW_WIDTH, WINDOW_HEIGHT = 600, 300
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def set_window_position():
    """
    Positions the window to the bottom right corner of the screen.
    """

    x = 1920 - WINDOW_WIDTH - 10
    y = 1080 - WINDOW_HEIGHT - 50
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{x},{y}"

def play_audio_with_control(music_file, screen, font, clock):
    """
    Plays the audio file with control to stop (S) or quit (Q).
    """

    pygame.mixer.init()
    pygame.mixer.music.load(os.path.join(os.getcwd(), "music", music_file))
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    pygame.mixer.music.stop()
                    return True
                if event.key == pygame.K_q:
                    pygame.mixer.music.stop()
                    return False

        screen.fill(WHITE)
        instruction = font.render("Playing... Press S to stop, Q to quit", True, BLACK)
        screen.blit(instruction, (20, WINDOW_HEIGHT // 2 - 36))
        pygame.display.flip()
        clock.tick(30)
    return True

def countdown_timer(minutes, seconds, music_path, screen, font, clock, phase_label):
    """
    Displays a countdown timer for the specified duration and phase.
    """

    total_seconds = minutes * 60 + seconds
    start_time = time.time()

    while True:
        elapsed = time.time() - start_time
        remaining = max(0, int(total_seconds - elapsed))
        minutes, seconds = divmod(remaining, 60)
        timer_display = f"{minutes:02d}:{seconds:02d}"

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                return False

        screen.fill(WHITE)
        label_surface = font.render(phase_label, True, BLACK)
        timer_surface = font.render(timer_display, True, BLACK)
        screen.blit(label_surface, (WINDOW_WIDTH // 2 - label_surface.get_width() // 2, WINDOW_HEIGHT // 4))
        screen.blit(timer_surface, (WINDOW_WIDTH // 2 - timer_surface.get_width() // 2, WINDOW_HEIGHT // 2))
        pygame.display.flip()
        clock.tick(1)

        if remaining == 0:
            break

    return play_audio_with_control(music_path, screen, font, clock)

def run_pomodoro_session(args):
    """
    Executes the full Pomodoro session based on user-defined parameters.
    """

    print('\n\n--- Welcome to the Professional Pomodoro Timer ---\n')

    set_window_position()
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Pomodoro Timer")
    font = pygame.font.SysFont(None, 48)
    clock = pygame.time.Clock()

    for session_count in range(args.repeat):
        if not countdown_timer(args.minutes, args.seconds, args.work_music, screen, font, clock, "Work Period"):
            break
        if session_count < args.repeat - 1:
            if not countdown_timer(args.break_minutes, args.break_seconds, args.break_music, screen, font, clock, "Break Period"):
                break

    pygame.quit()

def main():
    parser = argparse.ArgumentParser(
        description='A Professional Pomodoro Timer with Visual Display and Sound Feedback.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument('-M', '--minutes', type=int, default=25,
                        help='Work session duration in minutes.')
    parser.add_argument('-S', '--seconds', type=int, default=0,
                        help='Work session additional seconds.')
    parser.add_argument('-R', '--repeat', type=int, default=2,
                        help='Number of Pomodoro cycles.')
    parser.add_argument('-BM', '--break-minutes', type=int, default=5,
                        help='Break session duration in minutes.')
    parser.add_argument('-BS', '--break-seconds', type=int, default=0,
                        help='Break session additional seconds.')
    parser.add_argument('-WM', '--work-music', type=str,
                        default='Rest.mp3',
                        help='Audio file for work period completion.')
    parser.add_argument('--break-music', type=str,
                        default='BackToWork.mp3',
                        help='Audio file for break period completion.')

    args = parser.parse_args()

    try:
        run_pomodoro_session(args)
    except KeyboardInterrupt:
        print('\n\nSession interrupted by user. Exiting...')

if __name__ == '__main__':
    main()
