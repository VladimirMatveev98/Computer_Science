from enum import IntEnum
from typing import Tuple, List


def string_to_gene(str):
    gene: Gene = []
    for i in range (0,len(str),3):
        #Проверка на случай неполного гена
        if (i + 2) >= len(str):
            return gene
        #Инициализируем кодон из трёх нуклеотидов:
        codon: Codon = (Nucleotide[str[i]],Nucleotide[str[i + 1]],
                        Nucleotide[str[i + 2]])
        gene.append(codon)

    return gene


def linear_contains(gene, key_codon):
    for codon in gene:
        if codon == key_codon:
            return True

        return False


def binary_contains(gene, key_codon):
    low: int = 0
    high: int = len(gene) - 1
    #До тех пор, пока есть место для поиска:
    while low <= high:
        mid: int = (low + high) // 2
        if gene [mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

Nucleotide: IntEnum = IntEnum('Nucleotide', ('A','C','G','T'))
#Псевдоним типа для кодонов:
Codon = Tuple[Nucleotide,Nucleotide,Nucleotide]
#Псевдоним для генов:
Gene = List[Codon]

gene_str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTT"
my_gene: Gene = string_to_gene(gene_str)

acg: Codon = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat: Codon = (Nucleotide.G, Nucleotide.A, Nucleotide.T)

print(linear_contains(my_gene,acg)) #True
print(linear_contains(my_gene,gat)) #False

my_sorted_gene: Gene = sorted(my_gene)
print(binary_contains(my_sorted_gene, acg)) #True
print(binary_contains(my_sorted_gene, gat)) #False
