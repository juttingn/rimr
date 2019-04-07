import pandas as pd
from voxpopuli import Voice
import json
import tqdm
import pprint

lx = pd.read_csv('data/lexique.csv', sep='\t')
filtered_lx = lx[lx['4_cgram'] == "NOM"]


dict_pho= {}

v = Voice(lang="fr")

for index, word_row in tqdm.tqdm(filtered_lx.iterrows(), total=len(filtered_lx)):
    mot = word_row["1_ortho"]
    try:
        phonemes = v.to_phonemes(mot)
    except Exception as e:
        print(e)
        print(mot)
        continue
    pho_list = []
    for pho in phonemes:
       if pho.name != "_":
           pho_list.append(pho.name)
    dict_pho[mot] = pho_list

with open('data/phonemized_lexicon.json' , 'w') as fp:
    json.dump(dict_pho, fp, indent=4)

pprint.pprint(dict_pho)
