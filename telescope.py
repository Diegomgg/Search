import os

#################################################
#First version, searcher in a single file
#################################################
'''
with open(r"./test.txt", 'r') as fp:
    for l_no, line in enumerate(fp):
        # search string
        if 'akennedy_sa' in line:
            print('string found in a file')
            print('Line Number:', l_no)
            print('Line:', line)
            # don't look for next lines
            break
'''

#################################################
#Second version, searcher in files
#################################################

dir_path = r'./'
# iterate each file in a directory
for file in os.listdir(dir_path):
    cur_path = os.path.join(dir_path, file)
    # check if it is a file
    if os.path.isfile(cur_path):
        with open(cur_path, 'r') as file:
            for l_no, line in enumerate(file):
                # search string
                if 'akennedy_sa' in line:
                    print('string found in file: ' + cur_path)
                    print('Line Number:', l_no)
                    print('Line:', line)
                    # don't look for next lines
                    break