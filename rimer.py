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
group.add_argument('-n', '--numerique', help="Rime numérique", type=int)




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


def natural_rime_length(pho_query, pho_list):
    rime_number = 0
    min_l = min(len(pho_query), len(pho_list))
    for i in range(min_l):
        if pho_query[-(i + 1)] == pho_list[-(i + 1)] , :
            rime_number += 1
        else:
            break
    return rime_number

if __name__ == "__main__":
    args = parser.parse_args()

    rimes =[]
    for mot, word_data in lexicon.items():
        pho_list = word_data['pho']

        # Depending on the argument selected by the user regarding grammatical class, genre, number,
        # certain words are 'skipped'.

        if args.gram is not None:
            if args.gram != word_data['gram']:
                continue
        if args.genre is not None:
            if args.genre != word_data['genre']:
                continue
        if args.nombre is not None and args.nombre != word_data['nb']:
            continue

        # If the user wants a 'rich' rime, or wants to manually input the rime length,
        # only words with a specific amount of consecutive identical phonemes from the ennd are selected.
        # If the user wants a 'poor' rime or doesn't specify the power of the rime, only words
        # with 1 or more identical consecutive phoneme(s) from the end are selected.
        if args.riche:
            if natural_rime_length(pho_query, pho_list) >= 3:
                rimes.append(mot)
        elif args.numerique is not None:
            if rime_length(pho_query, pho_list) >= args.numerique:
                rimes.append(mot)
        else:
            if natural_rime_length(pho_query, pho_list) >= 1:
                rimes.append(mot)


    pprint.pprint(rimes)
