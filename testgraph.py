"""Projektovanje Alogiratma Vezba 07"""
from vertexstruct import Vertex, depth_first_search, breadth_first_search, print_path

# Prvo cvorovi
VERTEX1 = Vertex(1)
VERTEX2 = Vertex(2)
VERTEX3 = Vertex(3)
VERTEX4 = Vertex(4)
VERTEX5 = Vertex(5)
# Sam grapf kao recnik gde su kljucevi cvorovi a vredosti svi ostali cvorovi koji su spojeni na njega
G1 = dict()
G1[VERTEX1] = [VERTEX2, VERTEX5]
G1[VERTEX2] = [VERTEX1, VERTEX5, VERTEX4, VERTEX3]
G1[VERTEX3] = [VERTEX2, VERTEX4]
G1[VERTEX4] = [VERTEX2, VERTEX5, VERTEX3]
G1[VERTEX5] = [VERTEX1, VERTEX2, VERTEX4]
breadth_first_search(G1, VERTEX1)
print_path(VERTEX1, VERTEX3)
# Zadatak1 donji graph mozemo iskoristit stare vertexe samo dodati 6 i drukcije ih povezati
VERTEX6 = Vertex(6)
G2 = dict()
G2[VERTEX1] = [VERTEX2, VERTEX4]
G2[VERTEX2] = [VERTEX5]
G2[VERTEX3] = [VERTEX5, VERTEX6]
G2[VERTEX4] = [VERTEX2]
G2[VERTEX5] = [VERTEX4]
G2[VERTEX6] = [VERTEX6]

breadth_first_search(G2, VERTEX1)
print_path(VERTEX1, VERTEX5)
print_path(VERTEX1, VERTEX3)

VERTEXR = Vertex('r')
VERTEXV = Vertex('v')
VERTEXS = Vertex('s')
VERTEXW = Vertex('w')
VERTEXT = Vertex('t')
VERTEXX = Vertex('x')
VERTEXU = Vertex('u')
VERTEXY = Vertex('y')
G3 = dict()
G3[VERTEXV] = [VERTEXR]
G3[VERTEXR] = [VERTEXS, VERTEXV]
G3[VERTEXS] = [VERTEXW, VERTEXR]
G3[VERTEXW] = [VERTEXS, VERTEXT, VERTEXX]
G3[VERTEXT] = [VERTEXW, VERTEXX, VERTEXU]
G3[VERTEXX] = [VERTEXW, VERTEXT, VERTEXY, VERTEXU]
G3[VERTEXU] = [VERTEXT, VERTEXY]
G3[VERTEXY] = [VERTEXX, VERTEXU]
breadth_first_search(G3, VERTEXV)
# v-r-s-w-t-u
print_path(VERTEXV, VERTEXU)

# Zadatak3 koristimo iste nodove sto smo definisali samo pravimo
# drugaciji dictionary veza
G4 = {
    VERTEXU: [VERTEXV, VERTEXX],
    VERTEXX: [VERTEXV],
    VERTEXV: [VERTEXY],
    VERTEXY: [VERTEXX],
    VERTEXW: [VERTEXY, VERTEXR],
    VERTEXR: [VERTEXR]
}
depth_first_search(G4)
# u-v-y-x
print_path(VERTEXU, VERTEXX)
