from typing import List


# Time Limit Exceeded
def validUtf8_1(data: List[int]) -> bool:
    if not data:
        return True

    def binarize(num):
        num_bin = bin(num)[2:]
        return '0' * (8 - len(num_bin)) + num_bin

    str_bin = list(map(binarize, data))
    if str_bin[0][0] == '0':
        return validUtf8_1(data[1:])

    elif str_bin[0][:3] == '110':
        if len(data) < 2:
            return False
        if str_bin[1][:2] != '10':
            return False
        return validUtf8_1(data[2:])

    elif str_bin[0][:4] == '1110':
        if len(data) < 3:
            return False
        for i in range(1, 3):
            if str_bin[i][:2] != '10':
                return False
        return validUtf8_1(data[3:])

    elif str_bin[0][:5] == '11110':
        if len(data) < 4:
            return False
        for i in range(1, 4):
            if str_bin[i][:2] != '10':
                return False
        return validUtf8_1(data[4:])

    else:
        return False


def validUtf8_2(data: List[int]) -> bool:

    def binarize(num):
        if num in bin_dict:
            return bin_dict[num]
        num_bin = bin(num)[2:]
        bin_dict[num] = '0' * (8 - len(num_bin)) + num_bin
        return '0' * (8 - len(num_bin)) + num_bin

    bin_dict = {}
    idx = 0
    while idx < len(data):
        cur_num = data[idx]
        if cur_num not in bin_dict:
            bin_dict[cur_num] = binarize(cur_num)

        if bin_dict[cur_num][:2] == '10':
            return False
        elif bin_dict[cur_num][0] == '0':
            flag = 1
        elif bin_dict[cur_num][:3] == '110':
            flag = 2
        elif bin_dict[cur_num][:4] == '1110':
            flag = 3
        elif bin_dict[cur_num][:5] == '11110':
            flag = 4
        else:
            return False

        for next_idx in range(1, flag):
            if idx + next_idx >= len(data):
                return False
            next_num = data[idx + next_idx]
            if next_num not in bin_dict:
                bin_dict[next_num] = binarize(next_num)
            if bin_dict[next_num][:2] != '10':
                return False
        idx += flag
    return True


def validUtf8(data: List[int]) -> bool:

    def check(size):
        for i in range(start + 1, start + size + 1):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
        return True

    start = 0
    while start < len(data):
        first = data[start]
        if (first >> 3) == 0b11110 and check(3):
            start += 4
        elif (first >> 4) == 0b1110 and check(2):
            start += 3
        elif (first >> 5) == 0b110 and check(1):
            start += 2
        elif (first >> 7) == 0:
            start += 1
        else:
            return False
    return True


if __name__ == "__main__":
    data_ = [197, 130, 1]
    print(validUtf8(data_))

    data_ = [235, 140, 4]
    print(validUtf8(data_))

    data_ = [237]
    print(validUtf8(data_))
