#!/bin/bash
IFS=$'\n';

in_folder="in/";
out_folder="out/";

if [ ! -d $in_folder ]
then
  mkdir $in_folder;
fi

if [ ! -d $out_folder ]
then
  mkdir $out_folder;
fi
# Creating the necessary folders

array_of_files=($(ls $in_folder | grep -vw ".DS_Store"))
number_of_files=${#array_of_files[@]}
# Creating array for files found in the in folder

if [[ (($number_of_files < 1)) ]]
then
  echo "Aucun fichiers trouvés (peut etre le cas au premier lancement).";
  exit;
fi
# Checking if the number of files is correct
echo "number of files $number_of_files";
if [[ (($number_of_files > 1)) ]]
then
  for i in $(seq 0 $(($number_of_files - 1)));
  do
    echo "$i) ${array_of_files[$i]}";
  done

  echo "Entrez le numéro du fichier a renommer";
  read file_number;
  while [[ ( -z "$(echo $file_number | grep "^[ [:digit:] ]*$")") || $file_number > $(($number_of_files - 1)) || $file_number < 0 ]]
  do
    echo "Veuillez entrer un nombre";
    read file_number;
  done
  # File selection

else
  file_number=0;
fi

echo "Fichier sélectionné : ${array_of_files[$file_number]}";

echo "Entrez votre nom : ";
read eprof;

echo "Entrez le type de cours (Révision/Cours/Correction) : ";
read type_cours;

echo "Entrez le type d'exo (TD/DE/CE/CC) : ";
read type_exo;

echo "Entrez la matiere : ";
read matiere;

echo "Entrez le niveau du cours (LX/MX) : ";
read niveau;

echo "Entrez le type d'exam à passer (DE/CE/CC/TP/RAT) : ";
read type_exam;

echo -e "Entrez la date (format : DD-MM-AAAA \nlaisser vide pour aujourd'hui) : ";
read date_input;
# Asks for the necessary informations

while [[ ! -z $(echo $date_input | grep -vw "[0-3][0-9]-[01][0-9]-[0-2][0-9][0-9][0-9]") ]]
do
  echo "Merci de respecter le format DD-MM-AAAA ou de laisser vide";
  read date_input;
done

if [ -z "$date_input" ]
then
  date_input=$(date +"%d-%m-%Y")
fi
# Setting the date input if empty

if [[ "$OSTYPE" == "darwin"* ]] # MacOS
then
  md5=$(md5 $in_folder${array_of_files[$file_number]} | rev | cut -d ' ' -f 1 | rev);
else # Linux
  md5=$(md5sum $in_folder${array_of_files[$file_number]} | cut -d ' ' -f 1);
fi


ext=$(echo ${array_of_files[$file_number]} | rev | cut -d '.' -f 1 | rev);
file_name="$out_folder/$type_cours ($type_exo) - $matiere $niveau ($type_exam) $date_input [$eprof] - $md5.$ext";


mv "$in_folder/${array_of_files[$file_number]}" "$file_name";

echo "Fichier renommé et déplacé dans $out_folder";
