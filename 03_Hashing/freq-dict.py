s = 'abbcadeabb'
freq = {}
for i in range(len(s)):
    if s[i] not in freq:
        freq[s[i]] = 1
    else:
        freq[s[i]] += 1
print(freq)