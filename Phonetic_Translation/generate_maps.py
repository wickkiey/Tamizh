from keyvalpairs import *
import numpy as np
import pickle

combinations = {}
chars_dict = {}
chars_dict = uyir_chars.copy()
chars_dict.update(mei_chars)


def save_to_file(filename,obj):
    with open(filename, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

char_iter = 0
for mk, mv in mei_chars.items():
    for uk, uv in uyir_chars.items():
        chars_dict[tam_chars[char_iter]] = mv + uv
        combinations[(mk,uk)] = tam_chars[char_iter]
        char_iter += 1


# Add ayutha eluthu to chars_dict
chars_dict["ஃ"] = "igh"

save_to_file("data/tam2eng.pkl",uyir_chars)
save_to_file("data/char_source_combinations.pkl",combinations)
