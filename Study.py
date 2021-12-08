count = 0

while count < 10:
    count += 1
    if count < 3:
        continue
    print(count)
    if count == 9:
        break
