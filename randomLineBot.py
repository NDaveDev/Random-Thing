import time
import random

def get_random_line(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

# Loop indefinitely
while True:
    # Generate a random delay between 1 and 5 minutes
    delay = random.randint(60, 300)
    
    # Wait for the delay
    time.sleep(delay)
    
    random_line = get_random_line('example.txt')
    print(random_line)
