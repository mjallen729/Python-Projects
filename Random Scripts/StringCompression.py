def compressedString(message):
    last_char = None
    num_occur = 0
    compressed = ''
    
    for c in message:
        print(num_occur)
        if c != last_char:
            if num_occur > 1:
                compressed += str(num_occur)
            
            last_char = c
            compressed += c
            num_occur = 1

            continue
        
        if c == last_char:
            num_occur += 1

    if num_occur > 1:
        compressed += str(num_occur)
            
    return compressed