#!/bin/bash
# Opcional: Hacer lo mismo que en el ejercicio anterior pero en Bash Scripting y exportando un CSV

# Route of the main directory
main_route="/media/tr4shhh/Tr4Shhh_FOLDER/Proyects/4geeks/08 - ML Ops/exercise-terminal-challenge/"

# CSV headers
echo "Nombre del Archivo,Peso Real (Bytes),Fecha de Modificación" > archivos.csv

# Function to get file size
get_file_size() {
    file_size=$(stat -c %s "$1")
    echo $file_size
}

# Function to get the file size in human readable format

format_size() {

    size_in_bytes=$1

    # Define the limits for KB, MB y GB
    KB=1024
    MB=$((KB * 1024))
    GB=$((MB * 1024))

    if [ $size_in_bytes -lt $KB ]; then
        echo "$size_in_bytes bytes"
    elif [ $size_in_bytes -lt $MB ]; then
        size_in_kb=$(echo "scale=3; $size_in_bytes / $KB" | bc)
        echo "${size_in_kb} KB"
    elif [ $size_in_bytes -lt $GB ]; then
        size_in_mb=$(echo "scale=3; $size_in_bytes / $MB" | bc)
        echo "${size_in_mb} MB"
    else
        size_in_gb=$(echo "scale=3; $size_in_bytes / $GB" | bc)
        echo "${size_in_gb} GB"
    fi
}

# Function to get modification date
get_modification_date() {
    modification_date=$(date -r "$1" "+%d-%m-%Y %H:%M:%S")
    echo $modification_date
}

# Get the files recursively
find "$main_route" -type f | while read -r file; do
    file_size=$(get_file_size "$file")
    human_file_size=$(format_size "$file_size")
    modification_date=$(get_modification_date "$file")
    echo "$file,$file_size,$human_file_size,$modification_date" >> archivos.csv
done

echo "CSV generado: archivos.csv"
