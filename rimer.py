from voxpopuli import Voice
import json
import tqdm
import pprint

with open('data/phonemized_lexicon.json', 'r') as f:
    phonemized_lexicon = json.load(f)

l_rime = 3
query = input()

v = Voice(lang="fr")
phonemes = v.to_phonemes(query)

pho_query = []
for pho in phonemes:
    if pho.name != "_":
        pho_query.append(pho.name)


def rime_length(pho_query, pho_list):
    rime_number = 0
    min_l = min(len(pho_query), len(pho_list))
    for i in range(min_l):
        if pho_query[-(i + 1)] == pho_list[-(i + 1)]:
            rime_number += 1
        else:
            break
    return rime_number

rimes = []

for mot, pho_list in phonemized_lexicon.items():
    if rime_length(pho_query, pho_list) >= l_rime:

        rimes.append(mot)

pprint.pprint(rimes)