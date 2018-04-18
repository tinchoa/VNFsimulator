import pickle
import numpy as np
import random
import networkx as nx

requisicoes = []
topologia = nx.read_gml("Rnp.gml")
nodes = topologia.nodes()

reqFile = open("logRequisicoes.log","w")

print nodes

for i in range(1000):
    src = random.choice(nodes)
    dst = src
    while dst == src:
        dst = random.choice(nodes)
    vms = np.random.normal(4,1)
    vms = int(vms)
    while vms == 0:
        vms = np.random.normal(4,1)
        vms = int(vms)
    
    arrayVolume = []
    for j in range (vms):
        volume = np.random.lognormal(3,1.7)
        while volume > 100:
            volume = np.random.lognormal(3,1.7)
        arrayVolume.append(volume)
    
    requisicoes.append({"src":src, "dst":dst, "volume":arrayVolume})

pickle.dump(requisicoes, reqFile)

print requisicoes
        