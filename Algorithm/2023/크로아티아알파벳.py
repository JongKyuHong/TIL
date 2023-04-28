import sys
input = sys.stdin.readline

word = ['c=','c-','dz=','d-','lj','nj','s=','z=']
input_word = input().rstrip()
for w in word:
    input_word = input_word.replace(w, '*')
print(len(input_word))