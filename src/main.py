# Obligatorio: Generar una tabla usando Python con TODOS los ficheros (recursivamente) del workspace que contenga el nombre del fichero, el peso REAL y la última fecha de modificación.


import os
import pandas as pd
import datetime

main_route = '/workspaces/exercise-terminal-challenge'

#------------------
def list_recursive_files(route):
    files = []
    for this_folder, subfolder, files_in_folder in os.walk(route):
        for file in files_in_folder:
            full_route = os.path.join(this_folder, file)
            files.append(full_route)
    return files

#------------------

def get_size(files):
    sizes = []  # Make a list to save the sizes
    for file in files:
        size = os.path.getsize(file)

        if size < 1024:
            size_str = f"{size} bytes"
        elif size < 1024 * 1024:
            size_str = f"{size / 1024:.3f} KB"
        elif size < 1024 * 1024 * 1024:
            size_str = f"{size / (1024 * 1024):.3f} MB"
        else:
            size_str = f"{size / (1024 * 1024 * 1024):.3f} GB"


        sizes.append(size_str)  # Add the size to the list
    return sizes  # Return the file sizes


#------------------

def get_date_modification(files):
    dates = []
    for file in files:
        # Get the date modified 
        date_modification = os.path.getmtime(file)

        #Change the format of the date
        modification_time = datetime.datetime.fromtimestamp(date_modification)
        formatted_date = modification_time.strftime('%d-%m-%Y %H:%M:%S')

        dates.append(formatted_date)
    return dates

#------------------



#Make the list of all files
all_files = list_recursive_files(main_route)

#Save the size file 
size_files = get_size(all_files)

# Save the date modification of the file
all_dates= get_date_modification(all_files)


pandas_files = {'Files': all_files,
                'Size': size_files,
                'Date Modified': all_dates}

data_pandas = pd.DataFrame(pandas_files)

print(data_pandas)





# Opcional: Hacer lo mismo que en la línea anterior pero en Bash Scripting y exportando un CSV