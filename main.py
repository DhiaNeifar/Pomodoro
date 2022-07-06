import time


class The_Time:

    def __init__(self):
        self.minutes = 0
        self.seconds = 0
        self.milliseconds = 0

    def update(self):
        self.milliseconds += 1
        if self.milliseconds % 1000 == 0:
            self.milliseconds = 0
            self.seconds += 1
            if self.seconds % 60 == 0:
                self.seconds = 0
                self.minutes += 1
                self.minutes %= 60

    def display(self):

        if self.minutes < 10:
            minutes = f'0{self.minutes}'
        else:
            minutes = f'{self.minutes}'

        if self.seconds < 10:
            seconds = f'0{self.seconds}'
        else:
            seconds = f'{self.seconds}'

        if self.milliseconds < 10:
            milliseconds = f'00{self.milliseconds}'
        elif 10 <= self.milliseconds < 100:
            milliseconds = f'0{self.milliseconds}'
        else:
            milliseconds = f'{self.milliseconds}'

        disp = f'{minutes}:{seconds}.{milliseconds}'

        return disp


def main():
    print('------------------- TIME -------------------')
    time_1 = The_Time()
    print(f'time: {time_1.display()}', end='\r')
    for i in range(10 ** 6):
        time_1.update()
        print(f'time: {time_1.display()}')
        time.sleep(0.00001)


if __name__ == '__main__':
    main()