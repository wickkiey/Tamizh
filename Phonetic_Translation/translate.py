import os
import pickle
from tamil import utf8
import re
with open("data/tam2eng.pkl",'rb') as f:
    tam2eng_map = pickle.load(f)

def tamil2eng(text):
    chars = utf8.get_letters(text)
    result = [tam2eng_map.get(char,char) for char in chars]
    return ''.join(result)

def tamil2eng1(text):
    return  re.sub('({})'.format('|'.join(map(re.escape, tam2eng_map.keys()))), lambda m: tam2eng_map[m.group()], text)

print(tamil2eng("நலமாக உள்ளீர்களா"))
print(tamil2eng1("நலமாக உள்ளீர்களா"))