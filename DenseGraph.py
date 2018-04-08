#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 22:10:28 2017

@author: oem
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import math
import numpy as np
import collections
import scipy.stats as stats



G=nx.florentine_families_graph()
pos=nx.get_node_attributes(G,'pos')

p=nx.density(G)
pos=nx.spring_layout(G,k=0.1,iterations=50)
nx.draw_networkx(G,pos,with_labels=True)
plt.axis('off')
plt.show()
edges=nx.to_edgelist(G)
nodes=nx.nodes(G)
print(len(nodes))
print(len(edges))
print(p)


p=nx.density(G)
d=nx.degree(G)

dseq=sorted(d.values(),reverse=True)
degreecount=collections.Counter(dseq)
fit=stats.norm.pdf(dseq,np.mean(dseq),np.std(dseq))
plt.plot(dseq,fit,'-o')
plt.hist(dseq,normed=True)
plt.show()

deg,cnt =zip(*degreecount.items())
fig,ax=plt.subplots()
plt.bar(deg,cnt,width=0.8,color='b')

summ=0
for node in nodes:
    summ=summ+d[node]
    avg=math.floor(summ/len(nodes))
print(avg)

plt.title("Degree Histogram")
plt.ylabel("Count")
plt.xlabel("Degree")
ax.set_xticks([d+0.4 for d in deg])
ax.set_xticklabels(deg)
plt.axes([0.4, 0.4, 0.5, 0.5])

q=nx.degree_histogram(G)
dlist=[]
for key,value in d.items():
    temp=[key,value]
    dlist.append(temp)
    
    

    


c=np.argmax(q)


print(d)






maxi=max(d,key=d.get)
print(maxi,d[maxi])

minim=min(d,key=d.get)
print(minim,d[minim])
        


def finminre(graph):
    visitnodes=[]
    mini=None
    val=0
    while (1>0):
        d=nx.degree(graph)
        mini=min(d,key=d.get)
        print(mini,d[mini])
        print(nodes)
        if avg <c:
            val=avg
        else:
            val=c
        print(val)    
        if (d[mini]==avg):
            print("reached")
            break
        else:
            nodes.remove(mini)
            visitnodes.append(mini)
        print(len(nodes))
            
        return(nodes,mini) 
        
    
   
  
    
    






def remegdes(edges,nodes):
    unwanted=[]
    for edge in edges:
        s,d,_=edge
        if s==mini or d==mini :
            unwanted.append(edge)
    for item in unwanted:
        edges.remove(item)
        
    print(len(edges))        
   
        
            
    return(edges)

def creatnewgraph(edges):
    H= nx.Graph()
    H.add_edges_from(edges)
    pos=nx.spring_layout(G)
    nx.draw_networkx(H,pos,with_labels=True)
    plt.axis('off')
    plt.show()
    print(nx.density(G))
    edges=nx.to_edgelist(H)
    print(nx.degree(H))
    
    return edges,H
    
    
    

for i in range(0,33):
    edges,graph=creatnewgraph(edges)
    graph
    nodes,mini=finminre(graph)
    remegdes(edges,mini)
    print(nx.density(graph))