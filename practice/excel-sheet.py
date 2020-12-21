alphabets = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


def ExcelColumn(n):
    if n == 0:
        return ''

    head, rest = divmod(n, 26)
    if head == 0:
        return alphabets[rest - 1]
    if rest == 0:
        return ExcelColumn(head - 1) + alphabets[rest - 1]
    else:
        return ExcelColumn(head) + alphabets[rest - 1]


if __name__ == "__main__":
    print(ExcelColumn(1))      # A
    print('--------------------')
    print(ExcelColumn(5))      # E
    print('--------------------')
    print(ExcelColumn(51))     # AY
    print('--------------------')
    print(ExcelColumn(312))    # KZ
    print('--------------------')
    print(ExcelColumn(26))     # Z
