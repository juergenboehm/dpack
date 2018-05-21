
import re
import os

prog_file = 'dpackc'


p = re.compile(u'([A-Za-z0-9_/]+)\s*:=\s*proc')
q = re.compile(u'`type/.*')



def get_line_lis(filename):

    f = open(filename, mode = 'r')

    line_lis = []

    for line in f:
        line_lis.append(line)

    f.close()

    return line_lis



def get_procs(line_lis):
    global p
    export_list = []
    for lin in line_lis:
        res = p.match(lin)
        if res:
            export_list.append(res.group(1))
    return export_list

p1 = re.compile(u'(^`[A-Za-z0-9_/]+`)\s*:=')

def get_types(line_lis):
    global p1
    export_list = []
    for lin in line_lis:
        res = p1.match(lin)
        if res:
            export_list.append(res.group(1))
    return export_list

    

def process_prog_file(prog_file):

    line_lis = get_line_lis(prog_file)

    nml_lis = get_procs(line_lis)
    typ_lis = get_types(line_lis)

    return [prog_file, nml_lis, typ_lis]


batch_filename = 'module-list.txt'

f = open(batch_filename, mode='r')

prog_name_lis = []

for lin in f:
    lin1 = lin.rstrip()
    if len(lin1) > 0:
        prog_name_lis.append(lin1)

f.close()


reslis = []

for pn in prog_name_lis:
    reslis.append(process_prog_file(pn))

for rr in reslis:
    if len(rr[2]) > 0:
        print(rr)


    
    





            
