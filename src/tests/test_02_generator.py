'''Test for module task_02_generator'''
import sys
from pathlib import Path
sys.path.append(str(Path(str(Path('.').absolute()),"src")))

import task_02_generator.generator_numbers as gn

gn.sum_profit("",gn.generator_numbers)

test_text_1 = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
test_text_2 = "Загальний дохід -1.5працівника складається з -45 декількох частин: 1000.00 як основний дохід, доповнений додатковими надходженнями 10.00 і 350 доларів."

print(gn.extract_numbers_from_text(test_text_1))
print(f"sum_profit(test_text_1) = {gn.sum_profit(test_text_1,gn.generator_numbers)}")
print()
print(gn.extract_numbers_from_text(test_text_2))
print(f"sum_profit(test_text_2) = {gn.sum_profit(test_text_2,gn.generator_numbers)}")

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = gn.sum_profit(text, gn.generator_numbers)
print(f"\nЗагальний дохід: {total_income}\n")