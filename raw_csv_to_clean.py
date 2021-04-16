# Mihai DAMIAN
# UVT, Timisoara, 2021

import pandas

# change khz according to desired file
df = pandas.read_csv(open('./input_sanitized_ghz.csv', encoding="utf8"), delimiter=',', decimal=",")

dict_all = df.to_dict()

new_dict = {}

for key, value in dict_all.items():
    new_val = []
    for valkey, val in value.items():
        val = str(val)
        new_val.append(val)
    new_dict[str(key)] = new_val

# change kHz according to the file used
col1 = "Banda de frecvenţe\n(GHz)"
col2 = "Atribuiri în România"

final_dict = {}
last_el = ''

for el, el2 in zip(new_dict[col1], new_dict[col2]):
    if el != "nan":
        final_dict[el] = [el2]
        last_el = el
    else:
        if el2 != "nan":
            final_dict[last_el].append(el2)

dict_short = {}

freq = []
uses_aux = []

for key, val in final_dict.items():
    if len(val) == 0:
        freq.append(key)
    else:

        for el in val:
            freq.append(key)
            uses_aux.append(el)

uses = uses_aux

data = dict(
    freqs=freq,
    usess=uses,
    value=[1 for el in range(len(freq))])

print(data)

df = pandas.DataFrame(data)

# change khz according to the file used
df.to_csv('ghz_clean_aux.csv', encoding='utf-8')
