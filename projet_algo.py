
        
def chercher_region_def(n,case_def):
    def_x = case_def[0]
    def_y = case_def[1]
    
    if (def_x < n//2) and (def_y < n//2):
        return 1
    elif (def_x < n//2) and (def_y >= (n//2)):
        return 2
    elif (def_x >= (n//2)) and (def_y < n//2):
        return 3
    elif (def_x >= (n//2)) and (def_y >= (n//2)):
        return 4

  

def L_shape(region, n):
    
    central_positions = [
        (n//2 - 1, n//2 - 1),
        (n//2 - 1, n//2),
        (n//2, n//2 - 1),
        (n//2, n//2)
    ]
    
    result = []
    for i in range(len(central_positions)):
        if i != region - 1:
            result.append(central_positions[i])
    
    return result



def diviser_echiquier(matrice):
    n = len(matrice)  
    mid = n // 2      
    
    sous_matrice_1 = []
    sous_matrice_2 = []
    sous_matrice_3 = []
    sous_matrice_4 = []
    
    for i in range(mid):
        sous_matrice_1.append(matrice[i][:mid])  # Haut-gauche
        sous_matrice_2.append(matrice[i][mid:])  # Haut-droite
    
    for i in range(mid, n):
        sous_matrice_3.append(matrice[i][:mid])  # Bas-gauche
        sous_matrice_4.append(matrice[i][mid:])  # Bas-droite
    
    return sous_matrice_1,sous_matrice_2,sous_matrice_3,sous_matrice_4


def recombiner_sous_echiquier(sous_matrice_1, sous_matrice_2, sous_matrice_3, sous_matrice_4):
    # Taille des sous-matrices
    mid = len(sous_matrice_1)  # Nombre de lignes dans une sous-matrice
    
    # Recombine les sous-matrices ligne par ligne
    matrice_complete = []
    
    # Combine les deux sous-matrices du haut
    for i in range(mid):
        ligne_complete = sous_matrice_1[i] + sous_matrice_2[i]  # Fusionne les lignes de haut-gauche et haut-droite
        matrice_complete.append(ligne_complete)
    
    # Combine les deux sous-matrices du bas
    for i in range(mid):
        ligne_complete = sous_matrice_3[i] + sous_matrice_4[i]  # Fusionne les lignes de bas-gauche et bas-droite
        matrice_complete.append(ligne_complete)
    
    return matrice_complete


def carreler(echiquier, n,case_def,num=1):
    if n==2 :
        for i,j in [(0,0),(0,1),(1,0),(1,1)]:
            if (i,j)!= case_def:
                echiquier[i][j]=num
        resultat = echiquier
    else:
        sous_echiquier1,sous_echiquier2,sous_echiquier3,sous_echiquier4 = diviser_echiquier(echiquier)
        
        region=chercher_region_def(n, case_def)
        
        if region==1:
            l_shape = L_shape(region, n)
            se1_case_def = case_def
            se2_case_def = (l_shape[0][0], l_shape[0][1]-(n//2))
            se3_case_def=(l_shape[1][0]-(n//2), l_shape[1][1])
            se4_case_def=(l_shape[2][0]-(n//2), l_shape[2][1]-(n//2))
            
        if region==2:
            l_shape = L_shape(region, n)
            se1_case_def = (l_shape[0][0],l_shape[0][1])
            se2_case_def = (case_def[0],case_def[1]-(n//2))
            se3_case_def=(l_shape[1][0]-(n//2), l_shape[1][1])
            se4_case_def=(l_shape[2][0]-(n//2), l_shape[2][1]-(n//2))

            
        if region==3:
            l_shape = L_shape(region, n)
            se1_case_def = (l_shape[0][0],l_shape[0][1])
            se2_case_def = (l_shape[1][0],l_shape[1][1]-(n//2))
            se3_case_def=(case_def[0]-(n//2), case_def[1])
            se4_case_def=(l_shape[2][0]-(n//2), l_shape[2][1]-(n//2))
          
        if region==4:
            l_shape = L_shape(region, n)
            se1_case_def = (l_shape[0][0],l_shape[0][1])
            se2_case_def = (l_shape[1][0],l_shape[1][1]-(n//2))
            se3_case_def=(l_shape[2][0]-(n//2), l_shape[2][1])
            se4_case_def=(case_def[0]-(n//2), case_def[1]-(n//2))

            
            
        r1, num =carreler(sous_echiquier1, n//2, se1_case_def , num)
        r2, num =carreler(sous_echiquier2, n//2, se2_case_def , num+1)
        r3, num =carreler(sous_echiquier3, n//2, se3_case_def , num+1)
        r4, num =carreler(sous_echiquier4, n//2, se4_case_def , num+1)
        
        
        
        resultat=recombiner_sous_echiquier(r1, r2, r3, r4)
        
        num = num + 1
        for i,j in l_shape:
            resultat[i][j]=num
    return resultat, num

