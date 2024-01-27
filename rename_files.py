# script to remove '#' from filenames

import os

path = "CFL_data"

for folder in os.listdir(path):
    if "#" in folder:
        print(folder)
        new_folder_name = os.path.join(path, folder.replace("#", ""))
        os.rename(os.path.join(path, folder), new_folder_name)
        cfl_files = os.listdir(new_folder_name)
        for f in cfl_files:
            if "#" in f:
                print(f)
                os.rename(
                    os.path.join(new_folder_name, f),
                    os.path.join(new_folder_name, f.replace("#", "")),
                )
