import networkx as nx
import matplotlib.pyplot as plt
import pylab, random, copy
import logging
import datetime,time    
import pickles

g=nx.read_gml('Rnp.gml') #file with topology
size = len(g) #graph size, amount of nodes


reque=pickle.load(open("logRequisicoes.log","rb"))



def allocation(reque):
	for i in reque:
		volumes=i.values()[0]
		src=i.values()[1]
		dst=i.values()[2]



def betweeness(g):
	betweeness_centrality

def getDistance (g,node1ind, node2ind):
	
	path = nx.shortest_path(g, int(node1ind), int(node2ind))
	
	total = 0
	
	for i in range (len(path)-1):
		node1 = g.node[self.g.nodes()[path[i]]]
		node2 = g.node[self.g.nodes()[path[i+1]]]
	
		try:
			total += getDistanceFromLatLonInKm(node1["Latitude"],
node1["Longitude"], node2["Latitude"], node2["Longitude"])
		except KeyError:
			if "Latitude" not in node2: total += 0 #retorna 0 pq qualquer mapeamento eh possivel
			#print node1, node2
			elif "Latitude" not in node1: return np.inf
	return total