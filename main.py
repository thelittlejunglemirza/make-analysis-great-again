# from data_visualization.connector import plot_bipartite_module_to_contributor_graph,\
#     plot_bipartite_module_to_contributor_graph_given_module
# from data_collection.processes.node_edge_producer import get_data_for_vis
# import sys
#
# if len(sys.argv) == 2:
#     module_name = sys.argv[1]
#     plot_bipartite_module_to_contributor_graph_given_module(*get_data_for_vis(), module_name)
# else:
#     ### Draws the entire graph
#     plot_bipartite_module_to_contributor_graph(*get_data_for_vis())

import plotly.graph_objects as go

years = ['2016','2017','2018']

fig = go.Figure()
final_data = {
    '2017': {
        'hramezani': {
            'additions': 2376,
            'deletions': 355
        },
        'someoneelse': {
            'additions': 3444,
            'deletions': 244,
        }
    }
}


for key in final_data:
    contributors_list = []
    additions_list = []
    deletions_list =[]
    negated_list = []
    contributors = final_data[key]
    for cont in contributors:
        contributors_list.append(cont)
        additions_list.append(contributors[cont]['additions'])
        deletions_list.append(contributors[cont]['deletions'])
        negated_list.append(-contributors[cont]['deletions'])
    fig.add_trace(go.Bar(y= contributors_list, x=additions_list,
                         base = 0,
                         marker_color='crimson',
                         orientation='h',
                         name='additions'))
    fig.add_trace(go.Bar(y=contributors_list, x=deletions_list,
                         base=negated_list,
                         marker_color='grey',
                         orientation='h',
                         name='deletions'))

    fig.show()

# final_data = {
#     '2017': {
#         'hramezani': {
#             'additions': 2376487,
#             'deletions': 355
#         },
#         'fhjbkfjlf': {
#             'additions': 3444,
#             'deletions': 244,
#         }
#     },
#     '2018': {
#
#     },
#     '2019': {
#
#     }
# }