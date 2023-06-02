import methodPython

from methodPython.methodPython import methodPython
class pythonDictionnaryZipWithoutRandom():
    
    
    
    viande=["onglet", "filet de boeuf", "foie de veau", "souris d'agneau", "gigot", "roti de porc", "sauté de porc", "osso bucco", "cuisse de canard", "filet de dinde"]

    poids= [2.3, 4.6, 0.4, 0.5, 3.1, 1.2, 0.8, 1.8, 1.4, 0.6]
    
    dictionnaire_viande_poids_sans_randomize_list = methodPython.create_dic_zip(viande, poids)

    print(dictionnaire_viande_poids_sans_randomize_list)

    dictionnaire_viande_poids_avec_randomize_list = methodPython.create_dic_zip(methodPython.randomize_list(viande), methodPython.randomize_list(poids))

    print(dictionnaire_viande_poids_avec_randomize_list) 