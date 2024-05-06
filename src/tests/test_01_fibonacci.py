'''Test for module task_02_generator'''
import sys
from pathlib import Path
sys.path.append(str(Path(str(Path('.').absolute()),"src")))

import task_01_fibonacci.fibonacci as fibonacci

fib = fibonacci.caching_fibonacci()
while True:
    i = int(input("Entet n >>>  "))
    print(fib(i))