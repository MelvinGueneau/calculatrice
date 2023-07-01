import tkinter as tk

# Fonction pour ajouter deux nombres
def addition(a, b):
    return a + b

# Fonction pour soustraire deux nombres
def soustraction(a, b):
    return a - b

# Fonction pour multiplier deux nombres
def multiplication(a, b):
    return a * b

# Fonction pour diviser deux nombres
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur : division par zéro"

def calculer():
    nombre1 = float(entry_nombre1.get())
    nombre2 = float(entry_nombre2.get())
    choix = choix_operation.get()

    if choix == 1:
        resultat = addition(nombre1, nombre2)
    elif choix == 2:
        resultat = soustraction(nombre1, nombre2)
    elif choix == 3:
        resultat = multiplication(nombre1, nombre2)
    elif choix == 4:
        resultat = division(nombre1, nombre2)
    else:
        resultat = "Choix invalide"

    label_resultat.config(text="Résultat : " + str(resultat))

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Calculatrice")

# Création des éléments de l'interface
label_nombre1 = tk.Label(fenetre, text="Nombre 1:")
label_nombre1.pack()

entry_nombre1 = tk.Entry(fenetre)
entry_nombre1.pack()

label_nombre2 = tk.Label(fenetre, text="Nombre 2:")
label_nombre2.pack()

entry_nombre2 = tk.Entry(fenetre)
entry_nombre2.pack()

choix_operation = tk.IntVar()
choix_operation.set(1)

label_operation = tk.Label(fenetre, text="Opération:")
label_operation.pack()

radio_addition = tk.Radiobutton(fenetre, text="Addition", variable=choix_operation, value=1)
radio_addition.pack()

radio_soustraction = tk.Radiobutton(fenetre, text="Soustraction", variable=choix_operation, value=2)
radio_soustraction.pack()

radio_multiplication = tk.Radiobutton(fenetre, text="Multiplication", variable=choix_operation, value=3)
radio_multiplication.pack()

radio_division = tk.Radiobutton(fenetre, text="Division", variable=choix_operation, value=4)
radio_division.pack()

button_calculer = tk.Button(fenetre, text="Calculer", command=calculer)
button_calculer.pack()

label_resultat = tk.Label(fenetre, text="Résultat :")
label_resultat.pack()

# Lancement de la boucle principale
fenetre.mainloop()


#                                               
#                                                ██████████████                          
#                                        ████████▓▓▓▓██░░░░██▓▓████                      
#                                ████████░░░░░░░░██▓▓██░░░░██▓▓▓▓▓▓██                    
#                            ████░░██▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                        ████░░░░░░░░██▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓▓▓██                  
#                      ██▓▓▓▓██░░░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓██░░░░░░██▓▓▓▓██░░██▓▓▓▓██░░██▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓██░░░░██▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██                    
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓██░░██▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██                      
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                        
#                    ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                            
#                      ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████                                
#                          ████████▓▓▓▓▓▓▓▓▓▓▓▓██████                                    
#                                  ████████████           