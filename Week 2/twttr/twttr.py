inp = input("Input: ").strip()
vowel = ["a","e","i","o","u","A","E","I","O","U"]

for i in inp:
    if i in vowel:
        inp = inp.replace(i,"")

print("Output:", inp)
