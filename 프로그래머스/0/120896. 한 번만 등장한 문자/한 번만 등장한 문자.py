def solution(s):
    freq = {}
    
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    
    unique_chars = []
    for ch in freq:
        if freq[ch] == 1:
            unique_chars.append(ch)
    
    unique_chars.sort()
    return ''.join(unique_chars)
