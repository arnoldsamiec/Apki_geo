from os import getcwd 

current_path = getcwd()
#print(current_path)

print(1233)

import czas
print(czas.aktualny_czas)

import time
time.sleep(20)

print(czas.aktualny_czas)

from importlib import reload
reload(czas)
print(czas.aktualny_czas)
