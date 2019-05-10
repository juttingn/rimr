import pandas as pd
from voxpopuli import Voice
import json
import tqdm
import pprint

lx = pd.read_csv('data/lexique.csv', sep='\t')
filtered_lx = lx[lx['4_cgram'].isin(["NOM" , "ADJ" , "ADV"])]


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
    if len(pho_list) > 1:
            word_data = dict()
            word_data["gram"]= word_row["4_cgram"]
            word_data["genre"] = word_row["5_genre"]
            word_data["nb"] = word_row["6_nombre"]
            dict_pho[mot] = word_data




with open('data/phonemized_lexicon.json', 'w') as fp:
    json.dump(dict_pho, fp, indent=4)

pprint.pprint(dict_pho)

