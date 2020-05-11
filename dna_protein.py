import sys
inputfile = sys.argv[2]
outputfile = sys.argv[4]
seq_in_fasta=[]
seq_fline=[]
index=-1
def dna_to_rna(dna_sequence):
    return dna_sequence.replace('T','U')
def dna_to_protein(dna_sequence):
    rna_sequence = dna_to_rna(dna_sequence)
    amino_acid={"AAA":"K", "AAC":"N", "AAG":"K", "AAU":"N", 
                "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T", 
                "AGA":"R", "AGC":"S", "AGG":"R", "AGU":"S", 
                "AUA":"I", "AUC":"I", "AUG":"M", "AUU":"I", 

                "CAA":"Q", "CAC":"H", "CAG":"Q", "CAU":"H", 
                "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P", 
                "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R", 
                "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L", 

                "GAA":"E", "GAC":"D", "GAG":"E", "GAU":"D", 
                "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A", 
                "GGA":"G", "GGC":"G", "GGG":"G", "GGU":"G", 
                "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V", 

                "UAA":"_", "UAC":"Y", "UAG":"_", "UAU":"T", 
                "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S", 
                "UGA":"_", "UGC":"C", "UGG":"W", "UGU":"C", 
                "UUA":"L", "UUC":"F", "UUG":"L", "UUU":"F"}
    protein_sequence=''
    for i in range (0,len(rna_sequence),3):
        if(rna_sequence[i:i+3]=="AUG"):
            rna_sequence=rna_sequence[i:]
            break

    for i in range(0,len(rna_sequence),3):
        
        if rna_sequence[i:i+3] in amino_acid:
            if amino_acid[rna_sequence[i:i+3]] == "_":
                break
            protein_sequence+=amino_acid[rna_sequence[i:i+3]]
    return protein_sequence


with open(inputfile) as file:
    for seq in file:
        seq=seq.strip()
        if seq[0]=='>':
            index += 1
            seq_fline.append(seq[1:])
            seq_in_fasta.append('')
        else:
            seq_in_fasta[index] += seq

for i in range(len(seq_in_fasta)):
    print('>' + seq_fline[i])
    
    rna=dna_to_rna(seq_in_fasta[i])
    protein=dna_to_protein(seq_in_fasta[i])
    print("RNA: "+rna+"\n")
    print("PROTEIN: "+protein+"\n")
    
    

with open(outputfile,"w") as out_file:
    for i in range(len(seq_in_fasta)):
        out_file.write('>'+seq_fline[i]+"\n")
        rna=dna_to_rna(seq_in_fasta[i])
        protein=dna_to_protein(seq_in_fasta[i])
        out_file.write("RNA: "+rna+"\n")
        out_file.write("PROTEIN: "+protein+"\n")

