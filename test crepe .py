#création du fichier texte
fichier = open("carte_crepe.txt","w")
fichier.close()
#Voici notre dictionnaire de crêpes, avec le nom de la crepe, son prix, le type de crepe et sa contenance
carte = {"Crepe Confiture Fraise":[float(5.90),"Sucrée",("Sucre glace, confiture")],
"Crepe Nutella":[float(6.50),"Sucrée",("Nutella, Chantilly")],
"Crepe Jambon Fromage":[float(7.00),"Salée",("Jambon, fromage")],
"Crepe Sarasin au trois fromages":[float(8.00),"Végétarienne",("Fromage de chèvre, mozarella, cheddar")],
"Crepe Kebab poulet":[float(8.50),"Salée",("Kebab, poulet, tomate, émental")]
}

#On a là nos ingredients de crêpe perso en liste et en dictionnaire
listeingredient = ['chevre(1)','gruyere(2)','mimolette(3)','cheddar(4)','comté(5)','jambon(6)','jambon de pays(7)','bacon(8)','saumon(9)','steak haché(10)','salade(11)','tomate(12)','oignon de roscoff(13)','beurre demi-sel(14)','creme fraiche(15)','sauce tomate(16)']
ingredients_perso = { 1 :"chevre", 2 : "gruyere", 3:"mimolette",4:"cheddar",5:"comté",6:"jambon",7:"jambon de pays",8:"bacon",9:"saumon",10:"steak haché",11:"salade",12:"tomate",13:"oignon de roscoff",14:"beurre demi-sel",15:"creme fraiche",16:"sauce tomate"}

#Mise en page du titre
print("")
print("")
print("             |------------------------|")
print("             |-Bienvenue à la kwèpwie-|")
print("             |------------------------|")
print("")
print("")



#on definit nos fonctions pour renvoyer l'info qui nous interesse (soit le nom, le prix ou les ingrédients)
def prix (crepe):
    info = carte[crepe]
    return info[0]

def type_crepe(crepe):
    info = carte[crepe]
    return info[1]

def ingr (crepe):
    info = carte[crepe]
    return info[2]

def tri_bulle(tab):
    n = len(tab)
    # Traverser tous les éléments du tableau
    for i in range(n):
        for j in range(0, n-i-1):
            # échanger si l'élément trouvé est plus grand que le suivant
            if tab[j] > tab[j+1] :
                tab[j], tab[j+1] = tab[j+1], tab[j]

def tri_selection(tab):
   for i in range(len(tab)):
      # Trouver le min
       min = i
       for j in range(i+1, len(tab)):
           if tab[min] > tab[j]:
               min = j
                
       tmp = tab[i]
       tab[i] = tab[min]
       tab[min] = tmp
   return tab




#Fonction pour la crepe perso
def crepe_perso ():
    #On présente au client tous nos ingrédients disponibles
    print("Voici la liste des ingrédients disponibles :" )
    for ingredients in listeingredient :
        print ("-",ingredients,"\n")
    print("--------------------------------------------")
    print("Combien d'ingredients voulez vous mettre dans votre crêpe ?")
    #On calcule le prix de la crepe perso en fonction du nombre d'ingredients voulu par le client
    perso_in=int(input("->> "))
    perso_out=perso_in*3.50
    print("Votre crêpe coutera ",perso_out,"$")

    #On crée une liste qui recensera tous les ingrédients choisi par le client
    print("Quels ingrédients voulez vous mettre ? (1 à la fois)")
    liste_perso=[]
    for i in range(perso_in):
        x=int(input("->> "))
        #on rejoute a la liste l'ingrédient ayant le meme indice que le nombre choisi
        liste_perso.append(ingredients_perso[x])
        print("")
        
    #On demande au client de nommer sa crepe
    print("Donnez un nom à votre crêpe")
    name = (str(input("->>")))
    print("----------------------------")
    #on affiche les ingredients contenus dans la crepe perso du clients
    print("Voici votre crêpe" ,name," : ",liste_perso,'\nElle sera ajouté à notre carte')
    print("")
    print("A emporter ou sur place ?  Emporter(1) / Sur Place(2)      (+3.99$ de livraison)")
    aplus = int(input("->> "))
    print("----------------------------------------------")
    print("Tout est bon !")
    print("Merci de votre achat et à bientôt à la kwèpwie!")
    # on ouvre le fichier texte afin d'enregistrer la nouvelle crepe
    carte_crepe = open("carte_crepe.txt", "a")
    carte_crepe.write("- Crêpe ")
    carte_crepe.write(name)
    carte_crepe.write(" - ")
    carte_crepe.write(str(perso_out))
    carte_crepe.write("$")
    carte_crepe.write("\nCette crêpe contient :")
    carte_crepe.write(str(liste_perso))
    carte_crepe.write("\n\n")
    carte_crepe.close()

#Actions possibles par l'utilisateurs
print("1. Afficher la liste de crêpe par ordre alphabétique",
                   "\n2. Afficher la liste de crêpes par prix croissant ",
                   "\n3. Crêpe la plus chère",
                   "\n4. crêpe la moins chère",
                   "\n5. Quitter")
print("_____________________________")
print("Que choisissez vous ?")
choice = int(input("->> "))
#Tri par ordre alphabethique
if choice == 1 :
    liste= sorted(carte)
    #on ouvre le fichier afin d'enregistrer ce qu'il contient dans une variable
    carte_crepe_check = open("carte_crepe.txt","r")
    check_crepe = carte_crepe_check.read()
    carte_crepe_check.close()
    # boucle pour afficher chaque crèpe 
    for i in range(len(liste)):
        #variable pour comparer aux crèpes déja présente dans le fichier texte
        check_in = str(liste[i])
        print(i+1,". ",liste[i]," - ",prix(liste[i]),"$"," - ",type_crepe(liste[i]))
        print("Cette crêpe contient :", ingr(liste[i]))
        print("")
        #condition pour vérifier si la crèpe est déja présente dans le fichier texte
        if check_in not in str(check_crepe):
            carte_crepe = open("carte_crepe.txt", "a")
            carte_crepe.write("- ")
            carte_crepe.write(str(liste[i]))
            carte_crepe.write(" - ")
            carte_crepe.write(str(prix(liste[i])))
            carte_crepe.write("$")
            carte_crepe.write(" - ")
            carte_crepe.write(str(type_crepe(liste[i])))
            carte_crepe.write("\nCette crêpe contient :")
            carte_crepe.write(str(ingr(liste[i])))
            carte_crepe.write("\n")
            carte_crepe.close()
    print("6 .  Crêpe personnalisé  -  3.50 $/ingrédients")
    #choix de crèpe si 6 alors fonction crepe perso
    choice2 = int(input("->> "))
    if choice2==6 :
        crepe_perso()
    else :
    
        print("")
        print("A emporter ou sur place ?  Emporter(1) / Sur Place(2)      (+3.99$ de livraison)")
        aplus = int(input("->> "))
        print("----------------------------------------------")
        print("Tout est bon !")
        print("Merci de votre achat et à bientôt à la kwèpwie!")
#Tri par prix croissant avec le tri séléction
if choice == 2:
    liste_prix=[]
    liste= sorted(carte)
    #on ouvre le fichier afin d'enregistrer ce qu'il contient dans une variable
    carte_crepe_check = open("carte_crepe.txt","r")
    check_crepe = carte_crepe_check.read()
    carte_crepe_check.close()
    #tri de tous les prix avec le tri selection
    for cle, valeur in carte.items():
        liste_prix.append(valeur[0])
    tri_prix_bulle=tri_bulle(liste_prix)
    tri_prix=tri_selection(liste_prix)
    # 2 boucle pour comparer les prix du dictionnaire avec cex de la liste triée
    for i in range (len(tri_prix)):
        check_in = str(liste[i])
        if check_in not in str(check_crepe):
            carte_crepe = open("carte_crepe.txt", "a")
            carte_crepe.write("- ")
            carte_crepe.write(str(liste[i]))
            carte_crepe.write(" - ")
            carte_crepe.write(str(prix(liste[i])))
            carte_crepe.write("$")
            carte_crepe.write(" - ")
            carte_crepe.write(str(type_crepe(liste[i])))
            carte_crepe.write("\nCette crêpe contient :")
            carte_crepe.write(str(ingr(liste[i])))
            carte_crepe.write("\n")
            carte_crepe.close()
        #affichage des crêpes trié par prix
        for j in range (len(carte)):
            if tri_prix[i]== prix(liste[j]):
                print(i+1,". ",liste[j]," - ",prix(liste[j]),"$"," - ",type_crepe(liste[j]))
                print("Cette crêpe contient :", ingr(liste[i]))
                print("")
    print("6 .  Crêpe personnalisé  -  3.50 $/ingrédients  -  max 3 ingrédients")
    choice2 = int(input("->> "))
    if choice2==6 :
        crepe_perso()
    #Finalisation du prog
    else :
        print("")
        print("A emporter ou sur place ?  Emporter(1) / Sur Place(2)      (+3.99$ de livraison)")
        aplus = int(input("->> "))
        print("----------------------------------------------")
        print("Tout est bon !")
        print("Merci de votre achat et à bientôt à la kwèpwie!")
#On affiche la crepe la plus cher
if choice == 3 :
    liste_prix=[]
    liste= sorted(carte)
    for cle, valeur in carte.items():
        liste_prix.append(valeur[0])
    tri_prix=tri_selection(liste_prix)
    for i in range (len(carte)):
        # on prend la crèpe qui a le même prix que le dernière élément dans la table triée
        if tri_prix[len(tri_prix)-1] == prix(liste[i]):
            print(i+1,". ",liste[i]," - ",prix(liste[i]),"$"," - ",type_crepe(liste[i]))
            print("Cette crêpe contient :", ingr(liste[i]))
            print("")
#On affiche la crepe la moins cher
if choice == 4:
    liste_prix=[]
    liste= sorted(carte)
    for cle, valeur in carte.items():
        liste_prix.append(valeur[0])
    tri_prix=tri_selection(liste_prix)
    for i in range (len(carte)):
        # on affiche la crèpe qui a le même prix que le première élément dans la table triée

        if tri_prix[0] == prix(liste[i]):
            print(i+1,". ",liste[i]," - ",prix(liste[i]),"$"," - ",type_crepe(liste[i]))
            print("Cette crêpe contient :", ingr(liste[i]))
            print("")
if choice == 5:
    print("A bientôt à la kwèpwie!")


