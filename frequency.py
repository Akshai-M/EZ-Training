vowels = ["a", "e", "i", "o", "u"]
string = [
    ["Alex", "oooooo u iiiii"],
    ["Ben", "e iii aaaa"],
]

output = {}

for name, text in string:
    print(name)
    print(text)
    vowel_counts = {vowel: 0 for vowel in vowels}
    
   
    for char in text:
        if char in vowels:
            vowel_counts[char] += 1
    
   
    max_vowel = max(vowel_counts, key=vowel_counts.get)
    
    
    output[name] = max_vowel

print(output)

    