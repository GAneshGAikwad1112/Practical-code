import os

oldname = 'rename_file&remove_old/sample.txt'
newname = 'rename_file&remove_old/renamed_by_python.txt'

with open( oldname) as f:
    content = f.read()

with open(newname,'w')as f:
    f.write(content)

os.remove(oldname)