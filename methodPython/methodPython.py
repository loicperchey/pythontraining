import random

class methodPython():
    
    #Spliting some list

    def splitGestion(list2):

        split_list=[]

        split_row = list2.split(" ")

        for row in split_row:

            split_rows = row.split(',')

            split_list.append(split_rows)

        return(split_list)

   

    #Add in list

    def gestionListAppend(list1, list2, number):

        for row in list1:

            list2.append(row[number])

        return(list2)

   

    #Create a dictionnary by zip method

    def create_dic_zip(list1, list2):

        dictionnary_zip=dict(zip(list1, list2))

        return dictionnary_zip

   

    #Randomize list

    def randomize_list(list):

        random.shuffle(list)

        return list

   

    #Function search for an element in a dictionnary

    def searchElement(object, listOrDictionary):

            if object in listOrDictionary:

                print(object + " has been found and it's value is " + listOrDictionary[object])

            else:

                print("None Object has been found")
