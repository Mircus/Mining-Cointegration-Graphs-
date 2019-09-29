


import networkx as nx
import operator
import matplotlib.pyplot as plt 

from  scipy.stats import entropy



G= nx.read_graphml('C:/Users/mirco/Desktop/DMLab/code/cointegration/sp5002013.graphml')

#G = G1.subgraph(['GOOGL', 'VMC','ABT', 'A', 'BMY'])
#
print(nx.info(G))


print("density of G :")
print( nx.density(G))



triadic_closure = nx.transitivity(G)
print("Triadic closure:", triadic_closure)

betCent = nx.eigenvector_centrality(G)

print("entropy of G:")

print(entropy(list(betCent.values())))





# cliques 

cliques =nx.find_cliques(nx.to_undirected(G))

#print("cliques:")

#print(list(cliques))



# minimum spanning tree of SP500

#T=nx.minimum_spanning_tree(nx.to_undirected(G))
#print(nx.info(T))
#
#centrality = nx.eigenvector_centrality(T)
#print(centrality)
#
#
#print("density of T:")
#print( nx.density(T))
#
#pos = nx.spring_layout(T)
#nx.draw(T, pos, node_color = 'r', node_size = 10, alpha = 1)
#
#labels = {}    
#for node in T.nodes():
#    
#        #set the node name as the key and the label as its value 
#  labels[node] = node
##Now only add labels to the nodes you require (the hubs in my case)
#nx.draw_networkx_labels(T,pos,labels,font_size=16,font_color='g')
#
#plt.title('spanning tree  of SP coint graph')
#plt.show() 


####################################################################



#
## PAGE RANK              Now we apply the page rank algorith to determine the "influencers" of the SP500 cointegration  graph.
## The idea is that these nodes with the highest rank are the times series which influence most of the others
#

#
#pr = nx.pagerank(G, alpha=0.9)
#
#
## In[ ]:
#
#
#sorted_rank = sorted(pr.items(), key=operator.itemgetter(1))

#print(sorted_rank)
#
#





G.remove_edges_from(nx.selfloop_edges(G))

core = nx.k_core (G, 26)



print(nx.info(core))


print("density of core :")
print( nx.density(core))

betCentCore = nx.eigenvector_centrality(core)
print("entropy of core:")

print(entropy(list(betCentCore.values())))

pos = nx.spring_layout(core)
nx.draw(core, pos, node_color = 'r', node_size = 10, alpha = 1)

labels = {}    
for node in core.nodes():
    
        #set the node name as the key and the label as its value 
  labels[node] = node
#Now only add labels to the nodes you require (the hubs in my case)
nx.draw_networkx_labels(core,pos,labels,font_size=16,font_color='b')

plt.title('Core of SP coint graph')
plt.show() 

#core_number = nx.core_number(G)
#
#print(core_number)
#
#print(core.nodes())






#crust = nx.k_crust(G)
#
#print(crust.nodes())
#
#print(crust.edges())
#
#pos = nx.circular_layout(crust)
#nx.draw_networkx_nodes(crust, pos, node_color = 'r', node_size = 10, alpha = 1)
#
#labels = {}    
#for node in crust.nodes():
#    
#        #set the node name as the key and the label as its value 
#  labels[node] = node
##Now only add labels to the nodes you require (the hubs in my case)
#nx.draw_networkx_labels(crust,pos,labels,font_size=16,font_color='b')
#
#plt.title('Crust of SP coint graph')
#plt.show() 





#p = nx.shortest_path(G)
#
#p['GOOGL']['AAPL']
#

#
#p['AAPL']['GOOGL']
#

mis = nx.maximal_independent_set(nx.to_undirected(G))

print(mis)

#
#print ("SCC: " , nx.number_strongly_connected_components(G))
#print ("WCC: " ,  nx.number_weakly_connected_components(G))
#
#
## Now let us calculate and plot the distribution of degrees across the entire graph
## 

#plt.hist(list(dict(G.in_degree() ).values()))
#plt.show()
#

#
#plt.hist(list(dict(G.out_degree() ).values()))
#plt.show()
#


##G1 = G.subgraph(['GOOGL', 'VMC','ABT', 'A', 'BMY'])
#

#eigenvectors centrality and entropy











#pos = nx.spring_layout(G)

#node_color = [20000.0 * G.in_degree(v) for v in G]
#node_size =  [v * 10000 for v in betCent.values()]
#plt.figure(figsize=(20,20))
#nx.draw_networkx(G, pos=pos, with_labels=False,
#                 node_color=node_color,
#                 node_size=node_size )
#
#labels = {}    
#for node in G.nodes():
#    
#        #set the node name as the key and the label as its value 
#  labels[node] = node
##Now only add labels to the nodes you require (the hubs in my case)
#nx.draw_networkx_labels(G,pos,labels,font_size=16,font_color='r')
#
#
#
#plt.axis('off')
#
