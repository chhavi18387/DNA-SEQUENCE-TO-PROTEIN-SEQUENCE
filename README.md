# Transcribing DNA to RNA and Translating the RNA into corresponding protein  sequence(only using first reading frame)

At first, sequences are read out from the given FASTA file, ignoring the headers. These  sequences are then used for the following: 
We have defined two functions : 
-  dna_to_rna: In the given DNA sequence , we replace T by U and obtain the  corresponding RNA sequence. 
-  dna_to_protein : We first convert the given DNA sequence to RNA sequence using  the above function . In this RNA sequence , we search for the the start codon  “AUG” in the first reading frame only (starting from the first nucleotide in the given  fasta and considering three nucleotides at a time ) . We define a dictionary  amino_acids mapping codon with its corresponding amino acid. We check if codon  is present in the dictionary or not , if it is then we start adding the amino_acids to  a protein string. We keep on translating until we find stop codon “UAA” or “UGA”  or “UAG”. 
### Input Format  :FASTA file containing DNA sequences. 
