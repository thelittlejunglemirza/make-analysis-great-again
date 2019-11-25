from data_visualization.connector import plot
from data_collection.processes.node_edge_producer import get_data_for_vis

module_nodes, contributor_nodes, all_edges = get_data_for_vis()

plot(module_nodes, contributor_nodes, all_edges)

