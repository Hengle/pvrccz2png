#!python 
import os,sys
from xml.etree import ElementTree
from PIL import Image

def endWith(s,*endstring): 
    array = map(s.endswith,endstring) 
    if True in array: 
        return True 
    else: 
        return False 
    
# Get the all files & directories in the specified directory (path). 
def get_recursive_file_list(path): 
    current_files = os.listdir(path) 
    all_files = [] 
    for file_name in current_files: 
        full_file_name = os.path.join(path, file_name)
        if endWith(full_file_name,'.pvr.ccz'): 
            full_file_name = full_file_name.replace('.pvr.ccz','')
            all_files.append(full_file_name) 
 
        if os.path.isdir(full_file_name): 
            next_level_files = get_recursive_file_list(full_file_name) 
            all_files.extend(next_level_files)
    return all_files
    
def tree_to_dict(tree):
    d = {}
    for index, item in enumerate(tree):
        if item.tag == 'key':
            if tree[index+1].tag == 'string':
                d[item.text] = tree[index + 1].text
            elif tree[index + 1].tag == 'true':
                d[item.text] = True
            elif tree[index + 1].tag == 'false':
                d[item.text] = False
            elif tree[index+1].tag == 'dict':
                d[item.text] = tree_to_dict(tree[index+1])
    return d

if __name__ == '__main__':
    currtenPath = os.getcwd() 
    allcczArray = get_recursive_file_list(currtenPath)
    for cczfile in allcczArray:
		cczfilename = cczfile + '.pvr.ccz'
		pngfile = cczfile + '.png'
		command = "TexturePacker \'" + cczfilename + "\' --sheet \'" + pngfile + "\' --data dummy.plist --algorithm Basic --allow-free-size --no-trim "
		os.system(command)
	
