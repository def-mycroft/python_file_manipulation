import os, shutil

def gen_dir_list():
    return list(os.walk(os.getcwd()))

# For each dir and for each file, create list of filepaths for the .awz files 

def gen_filepath_list(files):

    filepaths = []

    for dir_group in files:
        for file in dir_group[2]:
            if file[-3:] == 'azw':
                filepath = dir_group[0]
                filepath += '\\'
                filepath += file
                filepaths.append(filepath)

    return filepaths

def copy_files(filepaths):
    output_path = 'C:\\Users\\dasen\\Downloads'
    for filepath in filepaths:
        shutil.copy(filepath, output_path)

def execute_script():
    copy_files(
            gen_filepath_list(gen_dir_list())
            )
