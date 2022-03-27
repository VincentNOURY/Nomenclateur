from os import rename
from os.path import exists
from os import mkdir
from os import listdir
from datetime import date


#NOMENCLATURE : Révision/Cours/Correction
#(Type d'exo ou examen vu TD/DE/CE/CC) - Matière LX
#(Examen à passer: DE/CE/CC/TP/RAT) DD-MM-AAAA [par Prénom Nom (L/MX)]

def main(in_folder = "in", out_folder = "out"):

    files = listdir(in_folder)
    for file in files:
        if file[0] == "." : files.remove(file)

    if files == []:
        print("No files in directory (might be the first launch)")
        exit()
    if len(files) > 1:
        for i in range(len(files)):
            print(f"{i}) {files[i]}")
        file_number = int(input("Entrez le numéro correspondant au fichier a modifier : "))
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
    date_input = input("Entrez la date (format : DD-MM-AAAA \n \
laisser vide pour aujourd'hui) : ")

    if date_input == "":
        date_input = date.today().strftime("%d-%m-%Y")

    rename(f"{in_folder}/{files[file_number]}", f"{out_folder}/{type_cours}\
 ({type_exo}) - {matiere} {niveau} ({type_exam}) {date_input} [{eprof}].{ext}")

    print("Fichier renommé")


if __name__ == '__main__':
    in_folder = "in"
    out_folder = "out"
    if not exists(in_folder) : mkdir(in_folder)
    if not exists(out_folder) : mkdir(out_folder)

    main(in_folder, out_folder)
