# import
import os

# func : makeDir()
def makekDir(PROJ_DIR, dir_name) :
    dir_abs_name = os.path.join(PROJ_DIR, dir_name)

    if not os.path.exists(dir_abs_name):
        os.mkdir(dir_abs_name)
    else : 
        print(f"{os.path.basename(dir_abs_name)} exists!") 
        
# func : moveFile()
def moveFile(PROJ_DIR, files) :
    from_abs_file = os.path.join(PROJ_DIR, files[0])
    to_abs_file = os.path.join(PROJ_DIR, files[1])

    if not os.path.exists(to_abs_file) :
        os.replace(from_abs_file, to_abs_file)
    else : 
        print(f"{os.path.basename(to_abs_file)} exists!") 

