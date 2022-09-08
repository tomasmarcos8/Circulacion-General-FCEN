with open(r"/home/tomas/Circulacion-General-FCEN/modulo_oceano/modeloQG/out_tmp/QG_diag.dat") as datFile: 
    Ec = [data.split()[3] for data in datFile]
 
'''
print(Ec)
for E in Ec:
    print(f'{E:<10s}')'''