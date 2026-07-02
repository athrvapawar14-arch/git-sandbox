def count_vowels(text):
    text = list(text)
    vowel = [ 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    count = 0
    for i in text:
        if i in vowel:
            count = count +1


    return count    



a = count_vowels("arewtgcineiwe")