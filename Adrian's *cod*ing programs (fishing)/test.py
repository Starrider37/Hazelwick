'''
import threading
import time

def count():
    for i in range(5):
        print("Count:", i)
        time.sleep(1)

thread = threading.Thread(target=count)
thread.start()

while True:
    text = input("Type something: ")
    print("You typed:", text)
'''
import threading
import time

def count():
    for i in range(5):
        print("Count:", i)
        time.sleep(1)

thread = threading.Thread(target=count)
thread.start()

thread.join()  # Wait for the counter thread to finish

text = input("Type something: ")
print("You typed:", text)
'''
import time

for i in range(1, 6):
    print(f"Processing {i * 20}%", flush=True)
    time.sleep(1)

print("Finished!")
''''''
import time
for i in range(5, 0, -1):
    print(i, end=" ", flush=True)
    time.sleep(1)
'''