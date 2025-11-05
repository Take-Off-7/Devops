from metrics import Counter
import time


def expensive_operation():
    counter = Counter(__name__, 'expensive_operation')
    for i in range(10):
        time.sleep(0.5)
        counter += 1
        print(f"Operation {i+1}/10 completed")


if __name__ == "__main__":
    print("Starting instrumented app...")
    expensive_operation()
    print("Done!")
