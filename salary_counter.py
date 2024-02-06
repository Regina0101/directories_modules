from pathlib import Path
import re

path = Path('salary/path.txt')

def total_salary(path):
    with open(path, 'r') as fh:
        content = fh.read()
        lines = content.splitlines()

    content_array = re.split(',|\n|\\s', content)

    digit_list = []
    total_sum = 0

    for salary in content_array:
        if salary.isdigit():
            salary_value = int(salary)
            total_sum += salary_value
            digit_list.append(total_sum)
        else:
            pass

    average = total_sum // len(lines)
    return total_sum, average

if __name__ == "__main__":
    total_sum, average = total_salary(path)
print(f"Total salary is: {total_sum}, Average is: {average}")
