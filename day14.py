

def parse_input(input_text):
    all_entries = []
    counter = 0
    for entry in input_text:
        if entry.startswith("mask = "):
            counter += 1
            all_entries.append({
                "mask": entry[7:],
                "assignments": []
            })
        else:
            all_entries[counter - 1]["assignments"].append(
                {
                    "location": entry[4:entry.find("] = ")],
                    "base-10 value": int(entry.split("] = ")[-1]),
                    "binary value": f"{int(entry.split('] = ')[-1]):b}",
                }
            )
    return all_entries


def mask_values(mask, binary_raw):
    new_binary = mask
    for i in range(-1, -len(binary_raw) - 1, -1):
        if mask[i] == "X" or mask[i] not in [0, 1, "0", "1"]:
            bin_list = list(new_binary)
            if len(mask) + i >= 0:
                bin_list[i] = binary_raw[i]
            else:
                bin_list.insert(0, binary_raw[i])
            new_binary = "".join(bin_list)

    new_binary = new_binary.replace("X", "0")
    return new_binary, int(new_binary, 2)


def mask_address(mask, address):
    binary_addr = f"{int(address):b}"
    new_binary = mask
    for i in range(-1, -len(binary_addr) - 1, -1):
        bin_list = list(new_binary)
        if len(mask) + i < 0:
            bin_list.insert(0, binary_addr[i])
        elif mask[i] == "1":
            continue
        elif mask[i] == "0":
            bin_list[i] = binary_addr[i]
        else:
            continue
        new_binary = "".join(bin_list)

    new_binary = get_variants([new_binary])
    new_binary_dec = [int(n, 2) for n in new_binary]
    return new_binary_dec


def get_variants(list_variants):
    new_variants = []
    for v in list_variants:
        if "X" in v:
            loc = v.find("X")
            temp_variants = []
            for alt in ["0", "1"]:
                temp = list(v)
                temp[loc] = alt
                str_temp = "".join(temp)
                temp_variants.extend(get_variants([str_temp]))
            new_variants.extend(temp_variants)
        else:
            new_variants.append(v)
    return new_variants


def mask_and_apply_input(input_text, mask_apply="value"):
    all_entries = parse_input(input_text)
    value_storage = {}
    for entry in all_entries:
        mask = entry.get("mask")
        for assignment in entry.get("assignments"):
            if mask_apply == "value":
                value_storage[assignment.get("location")] = mask_values(
                    mask, assignment.get("binary value"))[1]
            elif mask_apply == "address":
                locs = mask_address(
                    mask=mask, address=assignment.get("location"))
                for l in locs:
                    value_storage[l] = assignment.get("base-10 value")
    return sum(list(value_storage.values()))


filename = "input_day14.txt"

with open(filename, "r") as input:
    input_file = input.read().splitlines()

calculated_sum_1 = mask_and_apply_input(input_file, mask_apply="value")
calculated_sum_2 = mask_and_apply_input(input_file, mask_apply="address")

print(f"Calculated sum, 1 is:\t{calculated_sum_1}")
print(f"Calculated sum, 2 is:\t{calculated_sum_2}")
