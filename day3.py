from pathlib import Path

data_path = Path(__file__).parent / "data" / "day3.txt"
binary_nums = data_path.read_text().splitlines()

most_common_digits = "".join(
    "1" if digits.count("1") > len(digits) / 2 else "0" for digits in zip(*binary_nums)
)

gamma_rate = int(most_common_digits, base=2)
epsilon_rate = gamma_rate ^ (2 ** len(most_common_digits) - 1)
print(f"Most common digits: {most_common_digits}")
print(f"Gamma rate: {gamma_rate}")
print(f"Epsilon rate: {epsilon_rate} (in binary: {epsilon_rate:b})")
print(f"Product {gamma_rate * epsilon_rate}")
