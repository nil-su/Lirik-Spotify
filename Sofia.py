import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.07): 
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nI think we could do it if we tried", 0.07),
        ("If only to say", 0.09),
        ("you're mine", 0.15),
        ("Sofia, know that you and I", 0.10),
        ("Shouldn't feel", 0.09),
        ("like a crime", 0.15),
    ]
    
    delays = [0.5, 3.5, 5.7, 8.6, 11.8, 13.8]

    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
