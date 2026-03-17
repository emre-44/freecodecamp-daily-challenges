def repeat_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    result = ""
    
    for ch in s:
        if ch in vowels:
            count += 1
            if count == 1:
                result += ch
            else:
                result += ch + ch.lower() * (count - 1)
        else:
            result += ch
    
    return result