import file_function.file_maker as files
import file_function.dir_maker as dirs
import os
os.system('cls'if os.name == 'nt' else 'clear')

while True:
    dirs.dir_viewer()

    print('1_MOVE     ', '2_COPY     ', '3_RENAME     ',
          '4_CREATE     ', '5_DELETE     ', '6_GOTO     ',
          '7_VIEW     ', '8_EDIT     ', '9_EXIT')
    command = input('\nPLEASE ENTER YOUR COMMAND (digit or word) : \n')

    ##########################  MOVE ###################################

    if command.lower() == '1' or command.lower() == 'move':
        command = input('1_FILE OR 2_DIRECTORY:\n')
        if command.lower() == '1' or command.lower() == 'file':
            files.move_file(input('INPUT SOURCE:\n'), input('INPUT DESTINATION:\n'))
        elif command.lower() == '2' or command.lower() == 'directory':
            dirs.move_dir(input('INPUT SOURCE:\n'), input('INPUT DESTINATION:\n'))
        else:
            print('INCORRECT INPUT')

    ##########################  COPY ###################################

    elif command.lower() == '2' or command.lower() == 'copy':
        command = input('1_FILE OR 2_DIRECTORY:\n')
        if command.lower() == '1' or command.lower() == 'file':
            files.copy_file(input('INPUT SOURCE:\n'), input('INPUT DESTINATION:\n'))
        elif command.lower() == '2' or command.lower() == 'directory':
            dirs.copy_dir(input('INPUT SOURCE:\n'), input('INPUT DESTINATION:\n'))
        else:
            print('INCORRECT INPUT')

    ##########################  RENAME ###################################

    elif command.lower() == '3' or command.lower() == 'rename':
        command = input('1_FILE OR 2_DIRECTORY:\n')
        if command.lower() == '1' or command.lower() == 'file':
            files.rename_file(input('INPUT OLD NAME:\n'), input('INPUT NEW NAME:\n'))
        elif command.lower() == '2' or command.lower() == 'directory':
            dirs.rename_dir(input('INPUT OLD NAME:\n'), input('INPUT NEW NAME:\n'))
        else:
            print('INCORRECT INPUT')

    ##########################  CREATE ###################################

    elif command.lower() == '4' or command.lower() == 'create':
        command = input('1_FILE OR 2_DIRECTORY:\n')
        if command.lower() == '1' or command.lower() == 'file':
            files.make_file(input('INPUT NAME: \n'))
        elif command.lower() == '2' or command.lower() == 'directory':
            dirs.make_dir(input('INPUT NAME: \n'))
        else:
            print('INCORRECT INPUT')

    ##########################  DELETE ###################################

    elif command.lower() == '5' or command.lower() == 'delete':
        command = input('1_FILE OR 2_DIRECTORY:\n')
        if command.lower() == '1' or command.lower() == 'file':
            files.remove_file(input('INPUT NAME: \n'))
        elif command.lower() == '2' or command.lower() == 'directory':
            dirs.remove_dir(input('INPUT NAME: \n'))
        else:
            print('INCORRECT INPUT')

    ##########################  GOTO ###################################

    elif command.lower() == '6' or command.lower() == 'goto':
        dirs.dir_change(input('INPUT PATH: \n'))

    ##########################  VIEW ###################################

    elif command.lower() == '7' or command.lower() == 'view':
        files.file_viewer(input('INPUT FILE NAME: \n'))

    ##########################  EDIT ###################################
    elif command.lower() == '8' or command.lower() == 'edit':
        files.file_writer(input('INPUT FILE NAME: \n'))

    ##########################  EXIT ###################################

    elif command.lower() == '9' or command.lower() == 'exit':
        os.system('cls' if os.name == 'nt' else 'clear')
        print('GOODBYE!')
        exit()
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('INCORRECT COMMAND')

    print('#' * 100)
    print('#' * 100)
