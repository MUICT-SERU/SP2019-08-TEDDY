# Source: https://stackoverflow.com/questions/9282967/how-to-open-a-file-using-the-open-with-statement

def filter(txt, oldfile, newfile):
    '''\
    Read a list of names from a file line by line into an output file.
    If a line begins with a particular name, insert a string of text
    after the name before appending the line to the output file.
    '''

    with open(newfile, 'w') as outfile, open(oldfile, 'r', encoding='utf-8') as infile:
        for line in infile:
            if line.startswith(txt):
                line = line[0:len(txt)] + ' - Truly a great person!\n'
            outfile.write(line)

# input the name you want to check against
text = input('Please enter the name of a great person: ')    
letsgo = filter(text,'Spanish', 'Spanish2')