import time

class Pomodoro_Timer(object):
    """Pomodoro Timer"""

    def __init__(self, task, **kwargs):
        """Initialise the Pomodoro_Timer"""
        self.task = task
        self.timer = 25
        self.shortBreak = 5
        self.longBreak = 15
        self.checkmarks = 0
        self.longBreakCheckmark = 4
        return super().__init__(**kwargs)

    def countDown(self, timer):
        """Countdown timer. Arguments is the number of seconds for the timer"""
        # Set the countdown timer to be argument
        countDownTimer = timer * 60
        while True:
            # Countinuously countdowns in seconds
            if countDownTimer == 0:
                # Break from loop when timer is at 0 seconds
                break
            # Timer decreases by 1
            countDownTimer -= 1
            # Set the delay between timers to be every second
            time.sleep()

    def run(self):
        """Pomodoro technique that continuously runs"""
        while True:
            # Count downs from the main timer
            self.countDown(self.timer)

            # Increment the number of checkmarks
            self.checkmarks =+ 1
            
            if self.checkmarks % self.longBreakCheckmark == 0:
                # Take a long break if checkmark is modulo of a long break
                self.countDown(self.longBreak)
            else:
                # Take a short break if not a long break
                self.countDown(self.timerBreak)
