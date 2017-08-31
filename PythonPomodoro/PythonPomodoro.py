import pomodoro_timer

task = input("Enter Task: ")
pomodoro = pomodoro_timer.Pomodoro_Timer(task)

if input("Press enter to start timer: "):
    pomodoro.run()
