import time

seconds = int(input("Enter time in seconds: "))
def countdown_timer (seconds):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f'{mins}:{secs}'
        print(timer) 
        time.sleep(1)
        seconds -= 1   
    print("time up!!!!")


countdown_timer(seconds)