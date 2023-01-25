def fone(s):
    trim = str()
    nums = 0

    for c in s:
        if c.isdigit():
            trim += c
            nums += 1
        
        if nums % 3 == 0 and len(trim) > 0 and trim[-1] != '-':
            trim += '-'

    if trim[-1] == '-':
        trim = trim[:-1]

    return trim

print(
    fone('    --213-244  22 42-214---4531absjdad,.')
    )