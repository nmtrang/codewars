"""
Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
If you want to know more: http://en.wikipedia.org/wiki/DNA
In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

Example: (input:output)
DNA_strand("ATTCG") # 'TAAGC'
DNA_strand("GTAT") # 'CATA'
"""

def DNA_strand(dna):
    complements = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }

    return ''.join(complements[i] for i in dna)

print(DNA_strand('TAACG'))  # 'ATTGC
print(DNA_strand('TATGCCCGATGTCA'))

# Another solution
# def DNA_strand(dna):
#     return dna.translate(str.maketrans('ATCG', 'TAGC'))
# print(DNA_strand('TAACG'))  # 'ATTGC
# print(DNA_strand('TATGCCCGATGTCA'))
