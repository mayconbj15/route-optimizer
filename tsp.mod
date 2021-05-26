set S ordered;
param n := card {S}; # n = Cardinalidade de S (tamanho)

# Gera números inteiros que representam, em binário, os subconjuntos.
# Ex: 15 é 1111 em binário, que significa colocar todas as cidades no subconjunto
set BITS_OF_THE_SUBSETS := 0 .. (2**n - 1);

# Para cada sequência de bits (ex.: 1111),
# gera o subjunto equivalente com as cidades (ex.: {a,b,c,d}).
# A operação "ord(i)-1" obtém o índice da cidade i (começando em 0).
# A operação "k div 2**indice" equivale a um shift de bits "k >> indice".
# Esse shift é feito para saber se o bit da cidade i é 1 ou 0.
# Após o shift, "mod 2 = 1" checa se o primeiro bit do número é 1
# Equivale a saber se a cidade deve ou não ser incluída no subconjunto que está sendo gerado
set SUBSETS {k in BITS_OF_THE_SUBSETS} := {i in S: (k div 2**(ord(i)-1)) mod 2 = 1};

param cost {i in S, j in S} >= 0;
var X {i in S, j in S} binary;

minimize TotCost: sum {i in S, j in S} cost[i,j] * X[i,j];

subj to OneEdgeLeaving {i in S}:
   sum {j in S} X[i,j] = 1;

subj to OneEdgeEntering {j in S}:
   sum {i in S} X[i,j] = 1;

# "BITS_OF_THE_SUBSETS diff {0, 2**n - 1}" gera um novo conjunto sem
# as sequências de bits 0000 e 1111
subj to SubtourElim {k in BITS_OF_THE_SUBSETS diff {0, 2**n - 1}}:
   sum {i in SUBSETS[k], j in SUBSETS[k]} X[i,j] <= card{SUBSETS[k]} - 1;


data;

set S := a b c d ;

param cost:  a      b       c       d :=
        a    0      120767  19496   228133
        b    119085 0       105592  112085
        c    20209  104912  0       212329
        d    224256 109717  210763  0 ;

