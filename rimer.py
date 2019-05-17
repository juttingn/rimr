from voxpopuli import Voice
import json
import pprint
import argparse


with open('data/phonemized_lexicon.json', 'r') as f:
    phonemized_lexicon = json.load(f)



parser = argparse.ArgumentParser()
parser.add_argument("query", help= "Quel mot voulez-vous faire rimer?", type=str)
parser.add_argument("--gram", help= "Quelle est la classe grammaticale?", type=str)
parser.add_argument("--genre", help= "Quelle est le genre de la rime?", type=str)
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--pauvre', help='Rime pauvre', action='store_true',  type=str)
group.add_argument('-r', '--riche', help='Rime riche',  action='store_true', type=str)

args = parser.parse_args()


if args.query:
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
        if args.riche:
            if rime_length(pho_query, pho_list) >= 3:
                rimes.append(mot)
        elif args.pauvre:
            if rime_length(pho_query,pho_list) >=1:
                rimes.append(mot)



        #if rime_length(pho_query, pho_list) >= l_rime:
            #rimes.append(mot) x




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

#zizz