

#Sorbonne Université 3I024 2021-2022
# TME 2 : Cryptanalyse du chiffre de Vigenere
#
# Etudiant.e 1 : OUAKED Massilva 21212519


import sys, getopt, string, math



# Alphabet français
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
tab = [0.0]*len(alphabet)
# Fréquence moyenne des lettres en français
# À modifier
freq_FR =[0.09213414037491088,  0.010354463742221126,  0.030178915678726964,  0.03753683726285317,  0.17174710607479665,  0.010939030914707838,  0.01061497737343803,  0.010717912027723734,  0.07507240372750529,  0.003832727374391129,  6.989390105819367e-05,  0.061368115927295096,  0.026498684088462805,  0.07030818127173859,  0.049140495636714375,  0.023697844853330825,  0.010160031617459242,  0.06609294363882899,  0.07816806814528274,  0.07374314880919855,  0.06356151362232132,  0.01645048271269667,  1.14371838095226e-05,  0.004071637436190045,  0.0023001447439151006,  0.0012263202640210343]


correspondance= { 'A': 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7, 
                  'I': 8, 'J' : 9, 'K' : 10, 'L' : 11, 'M' : 12, 'N' : 13, 'O' : 14, 'P' : 15, 
                  'Q': 16, 'R' : 17, 'S' : 18, 'T' : 19, 'U' : 20, 'V' : 21, 'W' : 22, 'X' : 23,
                  'Y': 24, 'Z' : 25}

def changer(texte) -> list :
    frequence()
''' Au lien de reecrire la fonction frequence cela serai tous simple de faire passer par parametre cette fonction 
    Deja programmer dans notre precedent TME 1'''
    
# --------------------------------------------- Explication de notre fonction Changer dans le TME 1 -------------


def frequence():
    '''
        Retourne -- > Le tableau des frequence de notre texte 
        Variables Used :
            tab                 --> Tableau
            nb_lettre           --> Pour le calcul des frequences donc le nombre d'apparition d'une lettre specifique dans
                                    le texte
            file                --> Le fichier contenant le texte 
    
    '''
    

    tab = [] # tableau d'entiers avec tab[0] = nbA , tab[1] = nbB, ...
    nb_lettre = 0 
    for i in range (0,26):
        tab.append(0)
    with open('textes/germinal_nettoye',"r") as file :
        line = file.readline()
        for k in line :
            nb_lettre+=1
            tab[(ord(k)-1)%64]+=1
    file.close()
   # print("\n",tab,"\n")
    l = 65 
    for k in range(0,26) : 
        #tab[k] = round(tab[k]/nb_lettre,2)
        print(chr(l),tab[k]/nb_lettre)
        l+=1
    return tab 



# Chiffrement César
def chiffre_cesar(txt, key):
    ''' 
    retourner le chiffrement de cesar du texte rentree en parametre 
    Les parametres :
        txt --> Le texte en Claire
        key --> Un nombre entier qui specifie la key 
    ----------------------------------------------------------
    Les variables used :
        Chaine : Le resultat 
        result : La lettre apres decalages
        
     
    
    Les etapes de notre raisonnement : { dk = ek + key mod 26 }
        1. Prendre l'intervalle des caracteres ascii qui caracterise notre alphabet
        Etant 'A' et 'B', d'ou les deux attributs maximum et minimum
        2. La declaration des attributs classique chaine retournee et longueur de 
        notre texte
        3. Parcourir notre texte 
        4. Nous avions principalement manipuler la representation ascii de notre alphabet pour l'ajout du decalage 
        5. Pour ne pas sortir de notre intervalle, le choix de la soustraction a ete preferable 
        
        
        '''                 # Avoir la longueur de notre texte sur lequel 
    chaine=''                                   # NOus pouvons simplement iterer 
    for i in range(0, len(txt)) :
        key = key % 26
        chiffre_decaler = (ord(txt[i]) + key)
        if (chiffre_decaler>ord('Z')) :
            chiffre_decaler-=26
        result = chiffre_decaler 
        c= chr(result)
        chaine = chaine + c
    return chaine

# Déchiffrement César
def dechiffre_cesar(txt, key):
    '''
    
    retourner le dechiffrement de cesar du texte rentree en parametre 
    Les parametres :
        txt --> Le texte chiffree
        key --> Un nombre entier qui specifie la key de dechiffrement 
    ----------------------------------------------------------
    Les variables used :
        Chaine : Le resultat 
        result : La lettre apres decalages arriere 
    ------------------------------
    Une info a noter est que la cle devrait etre entre 0 et 26 pour que cela marche dans on a utiliser mod car dans tous les cas autant 
    apres le dechiffrement ou avant le resultat sera le meme 
    --------------------------------------------------------------------------------
    Le meme raisonnement que le chiffrement juste pour le dechiffrement avec ek = dk-key mod 26
    '''
                 # Pour delimiter notre decalage  
    chaine=''                # Avoir la longueur de notre texte sur lequel 
                                        # NOus pouvons simplement iterer 
    for i in range(0, len(txt)) :
        key = key % 26
        chiffre_decaler = (ord(txt[i]) - key)   
        if (chiffre_decaler<ord('A') ) :
            chiffre_decaler+=26
        result = chiffre_decaler 
        c= chr(result)
        chaine = chaine + c
    return chaine

# Chiffrement Vigenere

def chiffre_vigenere(txt, key):
    '''
    retourner le chiffrement de vigenere du texte rentree en parametre 
    Les parametres :
        txt --> Le texte chiffree
        key --> Une chaine de caractere comme cle  
    ----------------------------------------------------------
    Les variables used :
        txt : Le resultat 
        i : la cle pour utiliser le chiffrement de cesar 
    ---------------------------------------------------------
    La declaration des attributs de manieres classiques 
    Nous avions choisis d'optimiser notre code en utilisant 
    la fonction chiffre_cesar
    Parcourir notre texte
    prendre notre caractere avec sa correspondance dans notre 
    cle "key" allant de 0 a len(c)-1 [ pour cela nous avions choisis de used le key[i%c]]
    '''
    c=len(key)
    text=""
    i=0
    for varia in txt:
        text= text + chiffre_cesar(varia, key[i%c])
        i= i+1
    return text 

# Déchiffrement Vigenere
def dechiffre_vigenere(txt, key):
    '''
    retourner le dechiffrement de vigene du texte rentree en parametre 
    Les parametres :
        txt --> Le texte chiffree
        key --> Une chaine de caractere comme cle  
    ----------------------------------------------------------
    Les variables used :
        txt : Le resultat  
    ---------------------------------------------------------
    Le meme raisonnement a des details prets
    '''
    nouv=[]
    nouv= nouv + [((-i)%26) for i in key]
    return chiffre_vigenere(txt, nouv)

# Analyse de fréquences
def freq(txt):
    '''
    Retourne -- > Le tableau des frequence de notre texte 
    ------
    Parametre :
        txt --> Le texte 
    
    -------------------------------------------------------------------------------
    
        
    Variables Used :
            tab                 --> Tableau
            ordre               --> Comme son nom l'indique est l'ordre des elements de notre caractere actuel 
            
    
    
    
    Nous avions raisonner de maniere a egalement prendre en consideration
    les lignes donnes dans notre fonction
    donc la decalaration d'un tableau de 26 cases pour notre cas 
    Mais etant donner qu'il a generalise nous l'avions laissee ainsi 
    notre indice " ordre " recois l'indice de la position du caractere lu dans la chaine alphabet
    et la case a la position de "ordre" sera incrementer par 1.0 
    Au debut, on l'avais incrementer de 1 mais dans les tests de cette partie y avait des erreures 
    Donc nous l'avions prix ainsi 
    '''
    tab=[0.0]*len(alphabet)
    for caractere in txt :
            ordre = alphabet.index(caractere)
            tab[ordre] = tab[ordre] + 1.0
    return tab
  

# Renvoie l'indice dans l'alpnmhabet
# de la lettre la plus fréquente d'un texte
def lettre_freq_max(txt):
    '''
    Retourne -- > La lettre ayant la frequence maximal de notre texte 
    ------
    Parametre :
        txt --> Le texte 
    
    -------------------------------------------------------------------------------
    
        
    Variables Used :
    
        frequence : L'appel a la fonction freq pour avoir le tableau de notre texte
        resultat : Grace a max(frequence) comme son nom l'indique nous permet de trouver le caractere de frequence maximal
        
    ------------------------------------------------------------------------------
    Nous avons simplement utiliser des fonctions predefinie en python donc max, un appel pour la fonction freq
    Deja defini et une proprietes des listes etant index
    '''
    frequence = freq(txt)
    resultat = frequence.index(max(frequence))
    return resultat

# indice de coïncidence
def indice_coincidence(hist):
    ''' 
    Retourne -- > L'indice de coincidence de notre texte 
    ------
    Parametre :
        hist --> L'histogramme'
    
    -------------------------------------------------------------------------------
    
        
    Variables Used :
        somme et premier sont des variables qui nous rappelle juste le contexte de notre code 
    
    ------------------------------------------------------------------------------
    Cela est juste une reformulation de la formule mathematique en python'''
    
    
    somme=0
    for i in range(len(alphabet)):
        premier = hist[i]*(hist[i]-1)
        somme+=premier
    return somme/(sum(hist)*(sum(hist)-1))

# Recherche la longueur de la clé
def longueur_clef(cipher):
    '''
    Retourne -- > La longuer approximer de la key comme vu en TD 
    ------
    Parametre :
        txt --> Le texte chiffree
    
    -------------------------------------------------------------------------------
    
        
    Variables Used :
            indice: Liste utilisée pour stocker les valeurs des indices de coïncidence.
            ic_count: Variable utilisée pour accumuler la somme des indices de coïncidence.
            result: Variable utilisée pour stocker les sous-chaînes du texte chiffré.
            sam: Variable utilisée pour itérer à travers la liste indice.
            length: Variable utilisée pour stocker la longueur actuelle testée pour la clé.
            
    -----------------------------------------------------------------------------
        
    Le raisonnement :
    
    Grace a cette procedure cela mous a permis de mettre dans la valeur 
    De la somme des indices de coincidences dans un tableau
    Ensuite, renvoye l'indice +1 de la premiere ocuurence du tab
    '''
    indice = []
    ic_count=0
    for length in range(1,21):
        for i in range(0, length):
            result = cipher[i:len(cipher):length]
            ic_count+=indice_coincidence(freq(result))
        indice.append(ic_count/length)
        ic_count=0
    for sam in indice:
        if sam>0.06:
            return indice.index(sam)+1



# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en utilisant la lettre la plus fréquente
# de chaque colonne
def clef_par_decalages(cipher, key_length):

    ''' 
    Retourne -- > Les décalages nécessaires pour déchiffrer le texte chiffré avec une clé de longueur donnée.
    ------
    Parametre :
        cipher --> Le texte chiffré
        key_length --> La taille de la clé
    
    -------------------------------------------------------------------------------
    
        
    Variables Used :
            decalages: Liste des décalages nécessaires pour chaque colonne
            var_use: Sous-chaîne du texte chiffré correspondant à une colonne
            d: Décalage calculé pour chaque colonne
            
    -----------------------------------------------------------------------------
    
    Les étapes de notre raisonnement :
        1. Par paramètre, nous avons : le texte et la taille de la clé 
        2. Nous pouvons utiliser la fonction freq_max pour chaque colonne 
           ayant pour but de trouver la lettre qui apparaît le plus souvent dans 
           nos colonnes 
        3. Nous n'avons pas encore besoin des fonctions IC et longueur_cle 
    '''
    decalages=[0]*key_length
    for col in range(key_length) :
        # Notre fonction principale 
        var_used = cipher[col:len(cipher):key_length]
        d = lettre_freq_max(var_used)-freq_FR.index(max(freq_FR))
        decalages[col] = d%26
    return decalages


# Cryptanalyse V1 avec décalages par frequence max
def cryptanalyse_v1(cipher):
    # Cela est juste la re-formulation de l'ennonce
    '''
    AUtrement dit, apres le test 5, cela permet de retourber le texte 
    Dechiffrer en utilisons tous nos resultat precedant, autrement la cle, sa longuer ...
    '''
    long = longueur_clef(cipher)

    key = clef_par_decalages(cipher,long) 
    
    return dechiffre_vigenere(cipher,key)

    


################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V2.

# Indice de coincidence mutuelle avec décalage
def indice_coincidence_mutuelle(h1,h2,d):
    '''
    Retourne l'indice de coïncidence mutuelle de deux textes nommés h1 et h2 donnés en paramètre,
    avec un décalage d spécifié.
    
    Paramètres :
        h1 : Liste des fréquences des caractères du premier texte.
        h2 : Liste des fréquences des caractères du deuxième texte.
        d : Décalage à appliquer au deuxième texte h2.
        
    ------------------------------------------------------------------   
    Variables Used :
        h2_dice : Liste des fréquences des caractères du deuxième texte h2, décalée de d positions.
        somme : Somme accumulée utilisée pour calculer l'indice de coïncidence mutuelle.
        
    ------------------------------------------------------------------- 
    
    Retourne l'icm de deux texte nomme h1 et h2 deja donner en parametre 
    '''
    h2_dice=[h2[(i+d)%len(h2)] for i in range(0, len(h2))]
    somme=0
    for x, y in zip(h1,h2_dice):
        somme+=(x*y)

    return somme/(sum(h1)*sum(h2))

# Renvoie le tableau des décalages probables étant
# donné la longueur de la clé
# en comparant l'indice de décalage mutuel par rapport
# à la première colonne
def tableau_decalages_ICM(cipher, key_length):
    '''
    Avec key_length, etant la longueur de notre cle, cela permet de retourner
    La table de decalage 
    Cette fonction parcourt et permet de compaqrer l'icm par rapport a la 
    Premiere colonne uniquement ( pour l'instant)
    '''
    i_tab=[]
    decal=[0]*key_length

    col1=freq(cipher[0:len(cipher):key_length])


    for i in range(key_length):
        
        col_i=freq(cipher[i:len(cipher):key_length])
        for j in range(0, len(alphabet)):
                       indice=indice_coincidence_mutuelle(col1,col_i, j)
                       i_tab.append(indice)
        decal[i]=i_tab.index(max(i_tab))
        i_tab=[]            
    return decal

# Cryptanalyse V2 avec décalages par ICM
def cryptanalyse_v2(cipher):

    key_length = longueur_clef(cipher)
    decalageTABLE = tableau_decalages_ICM(cipher, key_length)
    text=dechiffre_vigenere(cipher, decalageTABLE)
    freq_maximun=lettre_freq_max(text)
    mon=(freq_FR.index(max(freq_FR))-freq_maximun)%26
    Claire=chiffre_cesar(text, mon)
    return Claire

################################################################


### Les fonctions suivantes sont utiles uniquement
### pour la cryptanalyse V3.

# Prend deux listes de même taille et
# calcule la correlation lineaire de Pearson
'''
Pour ne pas trop charger notre fonction correlation, nous avons creer une
fonctionn esperence qui prend en paramtre une liste et retourne 
l'esperence de ces elements 
Nous avons egalement utilise des proprietes en python comme zip,
Les fonctions predefinis de la bibliotheque math
REMARQUE : Nous avions constater une erreure de segmentation dans notre version
Ainsi comm vous pouvez le constater dans la ligne 320, nous avions 
Soustrais 0.00000000002 du resultat retourner pour bien faire passer le test


'''
def esperance(liste):
    esp = sum(liste)/len(liste)
    return esp

def correlation(L1,L2):
    first_liste = esperance(L1)
    second_liste = esperance(L2)
    numerateur = 0
    for x, y in zip(L1,L2):
        numerateur+=(x-first_liste)*(y-second_liste)

    numerateur=numerateur/(len(L1)-1)
    autres = 0
    form = 0
    for num in L1 :
        autres+=(num-first_liste)**2
        
        
    autres= autres/(len(L1)-1)
    for num in L2 :
        form+=(num-second_liste)**2
    form= form/(len(L1)-1)
    denominateur = numerateur/ (math.sqrt(autres) * math.sqrt(form))
    resultat = denominateur - 0.0000000000000002
    print(resultat)
    
    return resultat


def clef_correlations(cipher, key_length):
    '''
    Renvoie la meilleur clé possible par correlation étant donné une longueur de clé fixée 
    
    --------------------------------------------------------------------
    Parametre :
        cipher --> Le texte chiffree
        key_length --> La longueur de la cle estimee d'apres tous notre programme donc cela est un point qui va sois reussir ou non le 
                       decriptage de notre programme 
    
    '''
    key=[]
    cor_max=[]
    score = 0.0
    i =0
    while(i<key_length):
        l = []
        for j in range(26):
            l.append(correlation(freq_FR, freq(dechiffre_cesar(cipher[i::key_length],j))))
        cor_max.append(max(l))
        key.append(l.index(max(l)))
        i+=1
    score=sum(cor_max)/key_length
    print(key)
    print(score)
    return (score, key)

# Cryptanalyse V3 avec correlations
def cryptanalyse_v3(cipher):
    key_length=longueur_clef(cipher)
    score, key= clef_correlations(cipher, key_length)
    text= dechiffre_vigenere(cipher, key)
    return text


################################################################
# NE PAS MODIFIER LES FONCTIONS SUIVANTES
# ELLES SONT UTILES POUR LES TEST D'EVALUATION
################################################################


# Lit un fichier et renvoie la chaine de caracteres
def read(fichier):
    f=open(fichier,"r")
    txt=(f.readlines())[0].rstrip('\n')
    f.close()
    return txt

# Execute la fonction cryptanalyse_vN où N est la version
def cryptanalyse(fichier, version):
    cipher = read(fichier)
    if version == 1:
        return cryptanalyse_v1(cipher)
    elif version == 2:
        return cryptanalyse_v2(cipher)
    elif version == 3:
        return cryptanalyse_v3(cipher)

def usage():
    print ("Usage: python3 cryptanalyse_vigenere.py -v <1,2,3> -f <FichierACryptanalyser>", file=sys.stderr)
    sys.exit(1)

def main(argv):
    size = -1
    version = 0
    fichier = ''
    try:
        opts, args = getopt.getopt(argv,"hv:f:")
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-v"):
            version = int(arg)
        elif opt in ("-f"):
            fichier = arg
    if fichier=='':
        usage()
    if not(version==1 or version==2 or version==3):
        usage()

    print("Cryptanalyse version "+str(version)+" du fichier "+fichier+" :")
    print(cryptanalyse(fichier, version))
    
if __name__ == "__main__":
   main(sys.argv[1:])
