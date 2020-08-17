import os
os.chdir(r'C:\Users\jayasans4085\OneDrive - ARCADIS\Desktop\EPAi\session4')
from session5 import *
import pytest

def test_repetitionsZero():
    with pytest.raises(ValueError):
        time_it(print, 1, 2, 3, sep='-', end= ' ***\n',repetitions=-5)

parameters = [squared_power_list,2, -1, 5,5]

def test_timeit_print():
    with pytest.raises(ValueError):
        time_it(parameters[0],
                parameters[1], 
                repetitions = parameters[2],
                start = parameters[3],
                end = parameters[4])

    