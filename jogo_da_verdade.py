#!/usr/bin/env python3
# -*- coding: UTF-8 -*-


print("#########################################################")
print("#########################################################")
print("###########       ##################       ##############")
print("#########################   #############################")
print("#########################################################")
print("#####   #################################   #############")
print("#########   ##########################   ################")
print("###########                             #################")
print("###########################  #    #######################")
print("###########################    #   ######################")
print("#############################    # ######################")
print("#########################################################")
print("#####/ BEM VINDO AO JOGO DA VERDADE E AUTOREFLEXÃO \#####")

def verdade():
    name = input("Crie uma senha: ")
    name2 = input("Repita a mesma senha: ")
    if name == name2:
        p = input("OK, agora vamos pra próxima faze?\ndigite s/n: ")
        if p == "s":
            print("\nBoa o jogo vai começar agora!\nFique atento as regras...\nvoce só pode falar a verdade\nEsta é a unica regra.\n")
            p1 = input("1 Quem sou eu mesmo?\n")
            p2 = input("2 O que mais me preocupa no futuro?\n")
            p3 = input("3 Se este fosse o último dia da minha vida, \ngostaria de fazer o que estou fazendo hoje?\n")
            p4 = input("4 Do que eu realmente tenho medo?\n")
            p5 = input("5 Estou me prendendo a algo que preciso liberar?\n")
            p6 = input("6 O que mais importa na minha vida?\n")
            p7 = input("7 O que estou fazendo sobre as coisas mais importantes na minha vida?\n")
            p8 = input("8 Com que me importo?\n")
            p9 = input("9 Eu fiz alguém sorrir hoje?\n")
            p10 = input("10 O que é pior: falhar ou nunca ter tentado?\n")

            with open("log.txt", "a") as arquivo:
                arquivo.write("Aqui estão tuas repostas:\n")
                arquivo.write("\n1 Quem sou eu mesmo?\n" + p1)
                arquivo.write("\n2 O que mais me preocupa no futuro?\n" + p2)
                arquivo.write(
                    "\n3 Se este fosse o último dia da minha vida, gostaria de fazer o que estou fazendo hoje?\n" + p3)
                arquivo.write("\n4 Do que eu realmente tenho medo?\n" + p4)
                arquivo.write("\n5 Estou me prendendo a algo que preciso liberar?\n" + p5)
                arquivo.write("\n6 O que mais importa na minha vida?\n" + p6)
                arquivo.write("\n7 O que estou fazendo sobre as coisas mais importantes na minha vida?\n" + p7)
                arquivo.write("\n8 Com que me importo?\n" + p8)
                arquivo.write("\n9 Eu fiz alguém sorrir hoje?\n" + p9)
                arquivo.write("\n10 O que é pior: falhar ou nunca ter tentado?\n" + p10)
                arquivo.write("\n")
                arquivo.write("\n")

            print("Criei um arquivo com suas respostas quardadas, \npra você ler e fazer uma alto reflexão sobre você mesmo.")
            print("fim")
        else:
            print("TypeError")
    else:
        print("Senhas não coincidem")


verdade()