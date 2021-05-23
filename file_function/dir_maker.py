import os
import shutil


def dir_viewer():
    """function views current directory"""
    print('CURRENT WORK DIRECTORY')
    print(os.getcwd())
    for i in os.listdir():
        print(i)


def dir_change(path):
    if not os.path.exists(path):
        print('DIRECTORY NOT FOUND')
    else:
        print('DIRECTORY`S CHANGED')
        os.chdir(path)
        dir_viewer()


def make_dir(dir_name):
    if os.path.exists(dir_name):
        print('DIRECTORY EXIST')
    else:
        os.mkdir(dir_name)
        print('make directory')


def remove_dir(dir_name):
    try:
        os.rmdir(dir_name)
        print('remove directory')
    except FileNotFoundError:
        print('DIRECTORY NOT FOUND')


def rename_dir(dir_name, new_name):
    try:
        os.rename(dir_name, new_name)
        print('FILE`S RENAMED')
    except FileNotFoundError:
        print('DIRECTORY NOT FOUND!')


def copy_dir(dir_name, new_name):
    try:
        shutil.copytree(dir_name, new_name)
        print('FILE`S COPIED')
    except shutil.SameFileError:
        print('DIST IS THE SAME DIRECTORY')
    except FileNotFoundError:
        print('DIRECTORY NOT FOUND')
    except PermissionError:
        print('PERMISSION DENIED')
    except FileExistsError:
        print('DIRECTORY EXISTS')


def move_dir(dir_name, dist_name):
    try:
        shutil.move(dir_name, dist_name)
        print('DIRECTORY`S MOVED')
    except shutil.SameFileError:
        print('DIST IS THE SAME DIRECTORY')
    except FileNotFoundError:
        print('DIRECTORY NOT FOUND')
    except PermissionError:
        print('PERMISSION DENIED')
    except FileExistsError:
        print('DIRECTORY EXISTS')