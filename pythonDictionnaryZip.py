import random
from typing import List
from methodPython.methodPython import methodPython

 

class pythonDictionnaryZip():

    #List of elements

    list_cure_paroisse = "Pierre,Bordeaux Michel,Rennes Paul,Toulouse Jacques,Reims François,Paris Jean,Nice Youenn,Camaret-sur-Mer Tristan,Palavas-Les-Flots Julien,Grenoble"

    cure = []

    paroisse= []

    cure_list=[]

    paroisse_list=[]

    
   

   

 
 

    split_list_cure_paroisse = methodPython.splitGestion(list_cure_paroisse)

   

    print(split_list_cure_paroisse)

   

    cure_list = methodPython.gestionListAppend(split_list_cure_paroisse, cure, 0)

 

    for i, cureList in enumerate(cure_list):

        if i>0:

            print(i, cureList)

 

    paroisse_list = methodPython.gestionListAppend(split_list_cure_paroisse, paroisse, 1)

   

 

    for i, paroisseList in enumerate(paroisse_list):

        if i>0:

            print(i, paroisseList)

     

 

    dictionnaire_cure_paroisse = methodPython.create_dic_zip(methodPython.randomize_list(cure_list), methodPython.randomize_list(paroisse_list))

    print(dictionnaire_cure_paroisse)

 

    recherche = str(input("Que recherchez vous ici ? :"))

 

    searchForAnElement = methodPython.searchElement(recherche, dictionnaire_cure_paroisse)
    
   