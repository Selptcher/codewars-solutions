def generate_hashtag(s: str):
    if len(s.strip()) == 0: return False
    s = [w.capitalize() for w in s.strip().split()]
    hash = "#" + "".join(s)
    if len(hash) > 140: return False
    return hash
        


print(generate_hashtag('Codewars'))
print(generate_hashtag('Codewars      '))
print(generate_hashtag('      Codewars'))
print(generate_hashtag('Codewars Is Nice'))
print(generate_hashtag('CoDeWaRs is niCe'))
print(generate_hashtag('c i n'))
print(generate_hashtag('codewars  is  nice'))
print(generate_hashtag(''))
print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))
print(generate_hashtag('#ABbCccDdddEeeeeFfffffGggggggHhhhhhhhIiiiiiiiiJjjjjjjjjjKkkkkkkkkkkLlllllllllllMmmmmmmmmmmmmNnnnnnnnnnnnnnOooooooooooooooPpppppppppppppppQqq'))



def better_generate_hashtag(s):
    output = "#"
    
    for word in s.split():
        output += word.capitalize()
    
    return False if (len(s) == 0 or len(output) > 140) else output
        