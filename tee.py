from threading import Timer

def timeout():
    print("Game over")

t = Timer(1, timeout)
t.start()

t.join()