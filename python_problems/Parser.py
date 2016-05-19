with open('statement.txt','r') as f:
    total = 0
    for line in f:
        words = line.split()
        for word in words:
            if word[0] == '$':
                price = word[1:].strip()
                total += float(price)
    print(total)