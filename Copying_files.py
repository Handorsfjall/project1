import os, shutil

path = (input('Enter the directory: '))
new_path = (input('Enter the file copy directory: '))
os.chdir(path)
i = 0

print('Copied files:')
for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))
        full_file_name = os.path.join(root, file)
        shutil.copy(full_file_name, new_path)
        i += 1
        
        maximum_file_size = 0
        if os.path.getsize(full_file_name) > maximum_file_size:
            maximum_file_size = round(os.path.getsize(full_file_name)  * 9.537*10**(-7),1)
            file_name = full_file_name

print(f'\nFiles copied:  {i}')            
print(f'Largest file:  {file_name}' )
print(f'Size:  {maximum_file_size}' + ' MB')
