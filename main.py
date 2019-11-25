from data_visualization.connector import plot_bipartite_module_to_contributor_graph,\
    plot_bipartite_module_to_contributor_graph_given_module
from data_collection.processes.node_edge_producer import get_data_for_vis
import sys


### Draws the entire graph
# plot_bipartite_module_to_contributor_graph(*get_data_for_vis())


if len(sys.argv) != 2:
    print('please pass one argument as module name')
    print('$ python3 main.py docs/topics')
    sys.exit(11)



module_name = sys.argv[1]
plot_bipartite_module_to_contributor_graph_given_module(*get_data_for_vis(), module_name)
