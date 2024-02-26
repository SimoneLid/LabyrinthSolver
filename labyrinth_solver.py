import pathfind
import images
import os
import random

caselle={"vuoto":(255,255,255),"muro":(0,0,0),"inizio":(255,0,0),"fine":(0,255,0),"passo":(0,0,255)}



def search_start_end(labyrinth):
    '''
    Trova l'inizio e la fine del labirinto
    '''
    start=(-1,-1)
    end=(-1,-1)
    for i in range(1,len(labyrinth)-1):
        for j in range(1,len(labyrinth[i])-1):
            if labyrinth[i][j]==caselle["fine"]:
                end=(i,j)
            elif labyrinth[i][j]==caselle["inizio"]:
                start=(i,j)
    return start,end



def color_route(tiles,labyrinth):
    '''
    Colora le caselle indicanti il percorso finale
    '''
    for tile in tiles:
        if labyrinth[tile[0]][tile[1]]==caselle["vuoto"]:
            labyrinth[tile[0]][tile[1]]=caselle["passo"]
    return labyrinth



def labyrinth_solver(labyrinth_in):
    '''
    Richiama le varie funzione per caricare l'immagine, trovare l'inizio e la fine ed eseguire l'algoritmo A_star
    per trovare il percorso ottimale, colorandolo
    '''
    labyrinth=images.load_RGBA_notA("input/"+labyrinth_in)
    start,end=search_start_end(labyrinth)
    if start==(-1,-1) or end==(-1,-1):
        print("Labirinto:",labyrinth_in.removesuffix(".png"),"non ha inizio e/o fine")
    else:
        path,resolved=pathfind.A_star(labyrinth,start,end,caselle["muro"])
        if resolved==False:
            print("Labirinto:",labyrinth_in.removesuffix(".png"),"non ha soluzione")
        else:
            print("Labirinto:",labyrinth_in.removesuffix(".png"),"risolto in",len(path)+1,"passi")
        labyrinth=color_route(path,labyrinth)
    images.save(labyrinth,"output/"+labyrinth_in.removesuffix(".png")+"_out"+".png")
    return



def input_reader():
    '''
    Legge dalla cartella di input le immagini e se quella determinata immagine non è stata
    già risolta(cioè il suo nome non c'è un'immagine nella cartella output associata) viene risolta tramite labyrinth_solver
    '''
    inputs=os.listdir("input")
    outputs=os.listdir("output")
    for labyrinth in inputs:
        if labyrinth.removesuffix(".png")+"_out"+".png" not in outputs:
            print("input:",labyrinth.removesuffix(".png")+"_out"+".png")
            labyrinth_solver(labyrinth)
    return



def random_labyrinth(lenght,filename):
    '''
    Crea un labirinto random con grandezza e nome in input
    '''
    labyrinth=[["" for i in range(lenght)] for j in range(lenght)]
    for i in range(lenght):
        for j in range(lenght):
            random_cas=random.randint(0,2)
            if random_cas==0:
                labyrinth[i][j]=caselle["muro"]
            else:
                labyrinth[i][j]=caselle["vuoto"]
    start=(random.randint(0,lenght-1),random.randint(0,lenght-1))
    end=(random.randint(0,lenght-1),random.randint(0,lenght-1))
    labyrinth[start[0]][start[1]]=caselle["inizio"]
    labyrinth[end[0]][end[1]]=caselle["fine"]
    images.save(labyrinth,"input/"+filename)



if __name__=="__main__":
    input_reader()






