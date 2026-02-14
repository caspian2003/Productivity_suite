import time

class Timer:
    def countdown(self):
        try:
            seconds = int(input("Enter seconds: "))
            while seconds:
                print(f"Time left: {seconds}s")
                time.sleep(1)
                seconds -= 1
            print("⏰ Time's up!")
        except ValueError:
            print("Invalid input")


class Stopwatch:
    def run(self):
        input("Press Enter to start")
        start = time.time()
        input("Press Enter to stop")
        print("Elapsed:", round(time.time() - start, 2), "seconds")