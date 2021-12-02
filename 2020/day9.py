

def find_first_invalid(input_text, preamble_length):
    if len(input_text) <= preamble_length:
        return -999
    for entry_idx in range(preamble_length, len(input_text)):
        entry = input_text[entry_idx]
        leading = input_text[entry_idx - preamble_length:entry_idx]
        sum_exists = check_if_sum_exists(leading, entry)
        if not sum_exists:
            return entry
    return "All numbers valid"

def check_if_sum_exists(nums, sum_to):
    for i in range(len(nums)-1):
        num1 = nums[i]
        for j in range(i+1, len(nums)):
            num2 = nums[j]
            if int(num1) + int(num2) == int(sum_to):
                return True
    return False


def find_contiguous_sum(nums, sum_to):
    for i in range(len(nums) - 1):
        num1 = int(nums[i])
        if num1 >= int(sum_to) or num1 == 0:
            continue

        sum_list = [num1]
        for j in range(i + 1, len(nums)):
            num2 = int(nums[j])
            sum_list.append(num2)
            if sum(sum_list) == int(sum_to):
                return sum_list
            elif sum(sum_list) > int(sum_to):
                break
            else:
                continue
    return None

def find_encryption_weakness(contiguous_list):
    return min(contiguous_list) + max(contiguous_list)

filename = "input_day9.txt"
preamble_length = 25

with open(filename, "r") as input:
    input_file = input.read().splitlines()

first_invalid = find_first_invalid(input_file, preamble_length)
contiguous_sum_list = find_contiguous_sum(input_file, first_invalid)

print(f"First invalid num:\t{first_invalid}")
print(f"Contiguous list:\t{contiguous_sum_list}")
print(f"Encryption weakness:\t{find_encryption_weakness(contiguous_sum_list)}")
