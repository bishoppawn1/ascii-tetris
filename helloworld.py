import os,time

i = 0

while True:
    print('number of seconds' + str(i))
    time.sleep(1)
    i += 1
    os.system('cls' if os.name == 'nt' else 'clear')
