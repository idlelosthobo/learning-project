from collatz import process_number_list, STEP_MAXIMUM

import numpy as np
import pandas as pd


processed_list = list()
max_length = 0

for i in range(20000):
    number_list = process_number_list(i)

    if len(number_list) > max_length:
        max_length = len(number_list)

    processed_list.append(number_list)

for processed in processed_list:
    processed.extend([0] * (max_length - len(processed)))


df = pd.DataFrame(processed_list)