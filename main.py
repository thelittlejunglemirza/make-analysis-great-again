from data_visualization.connector import plot_bipartite_module_to_contributor_graph,\
    plot_bipartite_module_to_contributor_graph_given_module
from data_collection.processes.node_edge_producer import get_data_for_vis
from data_collection.processes.contributor_to_lines_changed import get_quarter_label_to_vis3_data
from data_visualization.mirror_bar_chart import plot_with_slider
from data_visualization.boxplot import plot_boxplot
import sys

def main():
    # print command line arguments
    if 0 < len(sys.argv[1:]) < 3:
        if len(sys.argv[1:]) > 1:
            if sys.argv[1] == "bipartite":
                module_name = sys.argv[2]
                plot_bipartite_module_to_contributor_graph_given_module(*get_data_for_vis(), module_name)
            elif sys.argv[1] == "mirrorchart":
                module_name = sys.argv[2]
                final_data = get_quarter_label_to_vis3_data(module_name)
                plot_with_slider(final_data)
            else:
                print("incorrect arguments: "
                      "to run..."
                      "Bipartite Graph:   main.py bipartite"
                      "                   main.py bipartite [module_name]"
                      "Boxplot Graph:     main.py boxplot"
                      "MirrorChart Graph: main.py mirrochart [module_name")
        else:
            if sys.argv[1] == "bipartite":
                if len(sys.argv) == 2:
                    plot_bipartite_module_to_contributor_graph(*get_data_for_vis())
            elif sys.argv[1] == "boxplot":
                plot_boxplot()
            else:
                print("incorrect arguments: "
                      "to run..."
                      "Bipartite Graph:   main.py bipartite"
                      "                   main.py bipartite [module_name]"
                      "Boxplot Graph:     main.py boxplot"
                      "MirrorChart Graph: main.py mirrochart [module_name")
    else:
        print("incorrect arguments: \n"
              "to run...\n"
              "Bipartite Graph:   main.py bipartite\n"
              "                   main.py bipartite [module_name]\n"
              "Boxplot Graph:     main.py boxplot\n"
              "MirrorChart Graph: main.py mirrochart [module_name\n")


if __name__ == "__main__":
    main()