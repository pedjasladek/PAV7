"""Topological sort graph"""
from vertexstruct import Vertex, depth_first_search

SORTEDLIST = []
UNDERWEAR = Vertex('Underwear')
PANTS = Vertex('Pants')
BELT = Vertex('Belt')
TIE = Vertex('Tie')
SHIRT = Vertex('Shirt')
SHOES = Vertex('Shoes')
SOCKS = Vertex('Socks')
WATCH = Vertex('Watch')
JACKET = Vertex('Jacket')
GRAPH = {
    UNDERWEAR: [PANTS, SHOES],
    PANTS: [BELT, SHOES],
    BELT: [JACKET],
    JACKET: [],
    TIE: [JACKET],
    SOCKS: [SHOES],
    WATCH: [],
    SHOES: [],
    SHIRT: [BELT]
}

depth_first_search(GRAPH, SORTEDLIST)
for i in SORTEDLIST:
    print(i.name)
