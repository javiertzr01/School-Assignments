from itertools import permutations
import copy

def get_most_common_single_letter(filein):
    with open(filein, mode="r") as fin:
        letter_dict = {}
        text = fin.read()
        for character in text:
            if character in letter_dict:
                letter_dict[character] += 1
            else:
                letter_dict[character] = 1
    letter_dict.pop(" ")
    return sorted(letter_dict.items(), key= lambda x: x[1], reverse=True)

def get_words(filein):
    with open(filein, mode="r") as fin:
            line = fin.readline()
            words = {}
            while line:
                    word = ""
                    for character in line:
                            if character != " ":
                                word += character
                            elif word in words:
                                words[word] += 1
                                word = ""
                            else:
                                if len(word) <= 4:
                                    words[word] = 1
                                word = ""
                    line = fin.readline()
            words.pop('')
    return sorted(words.items(), key = lambda x : (len(x[0]), x[1]))

def filter_by_length(dictionary, length):
    result = []
    for x in dictionary:
        if len(x[0]) == length:
            result.append(x[0])
    return result

def get_most_common_gram(filein, length):
    with open(filein, mode="r") as fin:
            line = fin.readline()
            words = {}
            while line:
                    word = ""
                    for character in line:
                            if character != " ":
                                word += character
                                if word in words:
                                    words[word] += 1
                                    word = character
                                elif len(word) == length:
                                    words[word] = 1
                                    word = character
                            if character == " ":
                                word = ""
                    word = ""
                    line = fin.readline()
    return sorted(words.items(), key = lambda x : x[1], reverse=True)

def map_replace(map, filein, fileout):
    with open(filein, "r") as fin:
        with open(fileout, "w") as fout:
            text = fin.read()
            for key, value in map.items():
                text = text.replace(key, value)
            fout.write(text)


if __name__ == "__main__":
    file = "story_cipher.txt"
    word_freq = get_words(file)
    letter_freq = get_most_common_single_letter(file)
    bigram_freq = get_most_common_gram(file,2)
    trigram_freq = get_most_common_gram(file,3)
    print(letter_freq[0])
    print(bigram_freq[0])
    print(trigram_freq[0])
    
    #('U', 305)
    #('JX', 82)
    #('JXU', 47)
    # e is the most common letter in the English language, th is the most common bigram, and the is the most common trigram.
    # U = e, th = JX, the = JXU
    
    #after first iteration, can see "thQt", which implies that Q = a
    #Short words provide useful clues. One-letter words are either a or i.
    #we can see that Y also appears alone, and since Q = a, Y = i
    #we can see this combination "it iI", can assume that I = s
    #we can see TiT, can assume it that T = d
    #"i did DEt KDdeHstaDd Mhat it is" looks like "I did not understand what it is" --> D = n, E = o, K = u, H = r, M = w
    # Reen a satisVOinW one throuWhout --> R = b, V = f, O = y, W = g
    # CyseBf in this franShise --> C = m, B = l, S = c
    # haLe neLer --> L = v
    # imFortantly --> F = p, maZor --> Z = j, Anow --> A = k, eNFect --> N = x, F = p
    mapping = {'U':"e", 
            'J':"t", 
            "X":"h",
            "Q":"a",
            "Y":"i",
            "I":"s",
            "T":"d",
            "D":"n",
            "E":"o",
            "K":"u",
            "H":"r",
            "M":"w",
            "R":"b",
            "V":"f",
            "O":"y",
            "W":"g",
            "C":"m",
            "B":"l",
            "S":"c",
            "L":"v",
            "F":"p",
            "Z":"j",
            "A":"k",
            "N":"x"}
    
    map_replace(mapping, file, "decrypted.txt")