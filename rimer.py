from voxpopuli import Voice, FrenchPhonemes
import json
import pprint
import argparse



with open('data/phonemized_lexicon.json', 'r') as f:
    lexicon = json.load(f)



parser = argparse.ArgumentParser()
parser.add_argument("query", help= "Quel mot voulez-vous faire rimer?", type=str)
parser.add_argument("--gram", help= "Quelle est la classe grammaticale des rimes recherchées?", type=str,
                    choices=["ADV", "ADJ", "NOM"])
parser.add_argument("--genre", help= "Quelle est le genre des rimes recherchées?", type=str,
                    choices=["m", "f"])
parser.add_argument("--nombre", help="Les rimes recherchées doivent-elles être au pluriel ou au singulier?", type=str,
                    choices=["p", "s"])
group = parser.add_mutually_exclusive_group()
group.add_argument('-p', '--pauvre', help='Rime pauvre', action='store_true')
group.add_argument('-r', '--riche', help='Rime riche',  action='store_true')
group.add_argument('-n', '--numérique', help="Rime numérique", action="store_true")

args = parser.parse_args()



v = Voice(lang="fr")
phonemes = v.to_phonemes(args.query)

pho_query = []
for pho in phonemes:
    if pho.name != "_":
        pho_query.append(pho.name)



def rime_length(pho_query, pho_list, natural=False):
    rime_number = 0
    min_l = min(len(pho_query), len(pho_list))
    for i in range(min_l):
        if pho_query[-(i + 1)] == pho_list[-(i + 1)]:
            rime_number += 1
        else:
            break
    return rime_number


def syllabizer(pho_list):
    """Le syllabizer prends en argument une liste de phonèmes, puis les ajoute à une "liste d'attente"  (syllablebuffer)
     en attendant qu'on détermine sa voyelle correspondante pour stocker celle-ci dans syllable_list. C'est cette liste
      qui est retournée par le syllabizer."""
    syllabe_list = []
    syllablebuffer = []
    for pho in pho_list:
        if pho in FrenchPhonemes.CONSONANTS:
            syllablebuffer.append(pho)
        elif pho in FrenchPhonemes.VOWELS:
            syllablebuffer.append(pho)
            syllabe = "".join(syllablebuffer)
            syllabe_list.append(syllabe)
            syllablebuffer = []
    #si le syllablebuffer n'est pas vide on ajoute les phonèmes à la dernière syllabe
    if syllablebuffer:
        syllabe_list[-1] += "".join(syllablebuffer)
    return syllabe_list


def natural_rime_length(syllabized_query, syllabized_list):
    rime_number = 0
    min_l = min(len(syllabized_query), len(syllabized_list))
    for i in range(min_l):
        if syllabized_query[-(i + 1)] == syllabized_list[-(i + 1)]:
            rime_number += 1
        else:
            break
    return rime_number

rimes = []

for mot, word_data in lexicon.items():
    pho_list = word_data['pho']
    if args.riche:
        if rime_length(pho_query, pho_list) >= 3:
            rimes.append(mot)
    elif args.pauvre:
        if rime_length(pho_query, pho_list) >=1:
            rimes.append(mot)
    else:
        if rime_length(pho_query, pho_list) >= args.numérique:
            rimes.append(mot)



