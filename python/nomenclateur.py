from os import rename
from os.path import exists
from os import mkdir
from os import listdir
from datetime import date
import hashlib
import re


#NOMENCLATURE : Révision/Cours/Correction
#(Type d'exo ou examen vu TD/DE/CE/CC) - Matière LX
#(Examen à passer: DE/CE/CC/TP/RAT) DD-MM-AAAA [par Prénom Nom (L/MX)]

def main(in_folder = "in", out_folder = "out"):

    files = listdir(in_folder)
    for file in files:
        if file[0] == "." : files.remove(file)

    if files == []:
        print("Aucun fichiers trouvés (peut etre le cas au premier lancement).")
        exit()
    if len(files) > 1:
        for i in range(len(files)):
            print(f"{i}) {files[i]}")
        file_number = sanitize_int("Entrez le numéro correspondant au fichier a modifier : ", len(files))
    else:
        file_number = 0

    print(f"Fichier a renommer : {files[file_number]}")

    ext = files[file_number].split(".")[-1]
    eprof = input("Entrez votre nom : ")
    type_cours = input("Entrez le type de cours (Révision/Cours/Correction) : ")
    type_exo = input("Entrez le type d'exo (TD/DE/CE/CC) : ")
    matiere = input("Entrez la matiere : ")
    niveau = input("Entrez le niveau du cours (LX/MX) : ")
    type_exam = input("Entrez le type d'exam à passer (DE/CE/CC/TP/RAT) : ")
    date_input = input("Entrez la date (format : DD-MM-AAAA \n\
laisser vide pour aujourd'hui) : ")

    temp_bool = True

    while temp_bool:
        if date_input == "" or re.match("[0-3][0-9]-[01][0-9]-[0-2][0-9][0-9][0-9]", date_input):
            temp_bool = False
        else:
            date_input = input("Veuillez entrer une date conforme au format DD-MM-AAAA ou laisser vide :")


    if date_input == "":
        date_input = date.today().strftime("%d-%m-%Y")

    md5 = ""

    with open(in_folder + "/" + files[file_number], "rb") as file:
        md5 = hashlib.md5(file.read()).hexdigest()

    rename(f"{in_folder}/{files[file_number]}", f"{out_folder}/{type_cours}\
 ({type_exo}) - {matiere} {niveau} ({type_exam}) {date_input} [{eprof}] - {md5}.{ext}")

    print("Fichier renommé")


def sanitize_int(message, max):
    set = False
    var = -1
    while (not set) or (var < 0 or var >= max):
        try:
            var = int(input(message))
            set = True
        except KeyboardInterrupt:
            print('\nOpération annulée.')
            exit()
        except:
            print(f"Veuillez entrer un nombre entre 0 et {max - 1}")
    return var

if __name__ == '__main__':
    in_folder = "in"
    out_folder = "out"
    if not exists(in_folder) : mkdir(in_folder)
    if not exists(out_folder) : mkdir(out_folder)

    main(in_folder, out_folder)
