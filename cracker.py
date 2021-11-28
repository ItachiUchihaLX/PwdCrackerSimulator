import time, itertools
from stdiomask import getpass, chrlist

def cracker(password, chrlist, showprcs):
  guess = ''

  for i in range(1, 6): 
      for g in itertools.product(chrlist, repeat=i):
        if showprcs:
          print('Guess: ' + ''.join(g), end='\r')
        if (guess := ''.join(g)) == password:
            return ''.join(guess)
        time.sleep(.000001)

password = getpass()
showprcs = True if input('Show cracking-process? (Y/N) ').upper() == 'Y' else False

start = time.time()
guess = cracker(password, chrlist, showprcs)
end = time.time()

print('------------------')
print('Guess: ' + guess)
print('Time: ' + str(round(end - start, 5)) + 's')