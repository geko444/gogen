import networkx as nx
from networkx.algorithms import bipartite
from networkx_viewer import Viewer
import string

B = nx.Graph()
B.add_nodes_from(string.ascii_uppercase[:25].split(), bipartite=0)
B.add_nodes_from(range(25), bipartite=1)

app = Viewer(B)
app.mainloop()