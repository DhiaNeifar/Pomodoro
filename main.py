import time
import argparse
from playsound import playsound


def _(minutes, seconds, music_path):
    time_1 = time.time()
    time_2 = time_1 + minutes * 60 + seconds
    print("\t\t\t       ---    Time Remaining   ---")
    while True:
        rem = time_2 - time.time()
        if abs(rem) < 0.05:
            print(f"\n\t\t\t\t Music {music_path} is playing!")
            playsound(music_path)
            break
        else:
            disp = f"\t\t\t\t\t  "
            rem_mins = int(rem // 60)
            rem_secs = int(rem % 60)
            if rem_mins < 10:
                disp += f'0{rem_mins}:'
            else:
                disp += f"{rem_mins}:"
            if rem_secs < 10:
                disp += f'0{rem_secs}'
            else:
                disp += f"{rem_secs}"

            print(disp, end='\r')


def pomodoro(args):

    print('\n\n\t\t------------------- Welcome to Pomodoro -------------------')
    while args.repeat:
        _(args.minutes, args.seconds, 'morning.mp3')
        _(0, 3, 'micro.mp3')
        args.repeat -= 1


def main():

    argparser = argparse.ArgumentParser(
            description='Pomodoro')
    argparser.add_argument(
        '--minutes', '-M',
        metavar='M',
        default=25,
        type=int,
        help='Minutes before turning up (default: 25).')

    argparser.add_argument(
        '--seconds', '-S',
        metavar='S',
        default=0,
        type=int,
        help='Seconds before turning up (default: 0).')

    argparser.add_argument(
        '--repeat', '-R',
        metavar='R',
        default=2,
        type=int,
        help='Number of times to repeat the process.')

    args = argparser.parse_args()
    try:
        pomodoro(args)

    except KeyboardInterrupt:
        print('\nCancelled by user. Bye!')


if __name__ == '__main__':
    main()