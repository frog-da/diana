s = open('k8-0.txt').readline().strip()

counter = 1
current_letter = ''
max_counter = 0
for i in range(len(s)):
    if current_letter == s[i]:
        counter += 1
        if counter == 3:
            print(current_letter)

    else:
        current_letter = s[i]
        max_counter = max(counter, max_counter)
        counter = 1



print(max_counter)
