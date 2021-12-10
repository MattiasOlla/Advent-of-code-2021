from pathlib import Path

data_path = Path(__file__).parent / "data.txt"
binary_nums = data_path.read_text().splitlines()

# binary_nums = [
#     "00100",
#     "11110",
#     "10110",
#     "10111",
#     "10101",
#     "01111",
#     "00111",
#     "11100",
#     "10000",
#     "11001",
#     "00010",
#     "01010",
# ]


def part1():
    most_common_digits = "".join(
        "1" if digits.count("1") > len(digits) / 2 else "0" for digits in zip(*binary_nums)
    )

    gamma_rate = int(most_common_digits, base=2)
    epsilon_rate = gamma_rate ^ (2 ** len(most_common_digits) - 1)
    print(f"Most common digits: {most_common_digits}")
    print(f"Gamma rate: {gamma_rate}")
    print(f"Epsilon rate: {epsilon_rate} (in binary: {epsilon_rate:b})")
    print(f"Product {gamma_rate * epsilon_rate}")


def most_common_in_position(binary_nums: list[str], position: int) -> bool:
    nums = [x[position] for x in binary_nums]
    print(f"Num 1s: {nums.count('1')}")
    return nums.count("1") >= (len(nums) / 2)


def part2():
    binary_nums1 = binary_nums.copy()
    for pos, _ in enumerate(binary_nums[0]):
        most_common = "1" if most_common_in_position(binary_nums1, pos) else "0"
        print(f"{pos=}, {most_common=}")
        binary_nums1 = [x for x in binary_nums1 if x[pos] == most_common]
        print(f"After filtering: {binary_nums1=}")
        if len(binary_nums1) == 1:
            print(f"Most common value after filtering: {binary_nums1[0]}")
            break

    binary_nums2 = binary_nums.copy()
    for pos, _ in enumerate(binary_nums[0]):
        least_common = "1" if not most_common_in_position(binary_nums2, pos) else "0"
        print(f"{pos=}, {least_common=}")
        binary_nums2 = [x for x in binary_nums2 if x[pos] == least_common]
        if len(binary_nums2) == 1:
            print(f"Least common value after filtering: {binary_nums2[0]}")
            break

    o2_gen_rating = int(binary_nums1[0], base=2)
    co2_scrub_rating = int(binary_nums2[0], base=2)
    print(
        f"O2: {o2_gen_rating}, CO2: {co2_scrub_rating}, product: {o2_gen_rating*co2_scrub_rating}"
    )


if __name__ == "__main__":
    part1()
    print()
    part2()
