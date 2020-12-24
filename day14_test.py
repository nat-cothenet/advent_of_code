import day14


def test_masks_correctly1():
    value = "000000000000000000000000000001100101"
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"

    _, masked_val = day14.mask_values(mask, value)
    assert masked_val == 101, f"Masked value is wrong, is {masked_val}"


def test_masks_correctly2():
    value = "000000000000000000000000000000001011"
    mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"

    masked_val_bin, masked_val = day14.mask_values(mask, value)
    assert (masked_val_bin, masked_val) == (
        "000000000000000000000000000001001001", 73), f"Masked value is wrong, is {masked_val}"


def test_calculation1():
    input_text = [
        "mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X",
        "mem[8] = 11",
        "mem[7] = 101",
        "mem[8] = 0"
    ]

    calc_val = day14.mask_and_apply_input(input_text)

    assert calc_val == 165, f"Incorrect calculation, resulted in {calc_val}"


def test_mask_2():
    address = 42
    mask = "000000000000000000000000000000X1001X"
    masked_addr = day14.mask_address(mask, address)

    assert masked_addr == [26, 27, 58, 59], \
        f"Incorrect masking, result was {masked_addr}"


def test_calculation2():
    input_text = [
        "mask = 000000000000000000000000000000X1001X",
        "mem[42] = 100",
        "mask = 00000000000000000000000000000000X0XX",
        "mem[26] = 1"
    ]

    calc_val = day14.mask_and_apply_input(input_text, mask_apply="address")

    assert calc_val == 208, f"Incorrect calculation, resulted in {calc_val}"
