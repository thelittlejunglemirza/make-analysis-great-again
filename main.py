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

#import plotly.graph_objects as go
import numpy as np
from data_collection.processes.contributor_to_lines_changed import get_contributors_to_lines_changed_given_module

#years = []

#fig = go.Figure()
final_data = {
    '2016': {
        'ads': {
            'additions': 24,
            'deletions': 355
        },
        'wESXAS': {
            'additions': 3444,
            'deletions': 244,
        },
        'wESXAS': {
            'additions': 42,
            'deletions': 244,
        },
        'dwas': {
            'additions': 344,
            'deletions': 244,
        },
        'adss': {
            'additions': 344,
            'deletions': 244,
        },
        'asdgrzb': {
            'additions': 344,
            'deletions': 244,
        },
        'ever': {
            'additions': 344,
            'deletions': 244,
        },
        'what': {
            'additions': 344,
            'deletions': 244,
        },
        'you': {
            'additions': 344,
            'deletions': 244,
        },
        'say': {
            'additions': 3444,
            'deletions': 2444,
        },
        'we': {
            'additions': 3444,
            'deletions': 244,
        },
        'will': {
            'additions': 3444,
            'deletions': 244,
        },
        'do': {
            'additions': 3444,
            'deletions': 244,
        },
        'so': {
            'additions': 3444,
            'deletions': 244,
        },
        'please': {
            'additions': 3444,
            'deletions': 244,
        },
        'say': {
            'additions': 3444,
            'deletions': 244,
        },
        'some': {
            'additions': 3444,
            'deletions': 244,
        },
        'thing': {
            'additions': 3444,
            'deletions': 244,
        },
        'cool': {
            'additions': 3444,
            'deletions': 244,
        },
        'right': {
            'additions': 3444,
            'deletions': 244,
        },
        'now': {
            'additions': 3444,
            'deletions': 244,
        }
    },
    '2017': {
        'wd': {
            'additions': 2376,
            'deletions': 355
        },
        'sad': {
            'additions': 3444,
            'deletions': 244,
        },
        'das': {
            'additions': 3444,
            'deletions': 244,
        },
        'bryan': {
            'additions': 3444,
            'deletions': 244,
        },
        'arash': {
            'additions': 3444,
            'deletions': 244,
        },
        'vsdv': {
            'additions': 3444,
            'deletions': 244,
        },
        'vd': {
            'additions': 3444,
            'deletions': 244,
        },
        'ht': {
            'additions': 3444,
            'deletions': 244,
        },
        'ngb': {
            'additions': 3444,
            'deletions': 244,
        },
        'ndgb': {
            'additions': 3444,
            'deletions': 244,
        },
        'nds': {
            'additions': 3444,
            'deletions': 244,
        },
        'dn': {
            'additions': 3444,
            'deletions': 244,
        },
        '1ergb': {
            'additions': 3444,
            'deletions': 244,
        },
        'drh': {
            'additions': 3444,
            'deletions': 244,
        },
        'arg': {
            'additions': 3444,
            'deletions': 244,
        },
        'sdrhbf': {
            'additions': 3444,
            'deletions': 244,
        },
        'sdhrtbf': {
            'additions': 3444,
            'deletions': 244,
        },
        'sdfb': {
            'additions': 3444,
            'deletions': 244,
        },
        'adf': {
            'additions': 3444,
            'deletions': 244,
        },
        'sedbf': {
            'additions': 3444,
            'deletions': 244,
        },
        'aergs': {
            'additions': 3444,
            'deletions': 244,
        }
    },
    '2018': {
        'ads': {
            'additions': 2376,
            'deletions': 355
        },
        'wESXAS': {
            'additions': 3444,
            'deletions': 244,
        },
        'wESXAS': {
            'additions': 3444,
            'deletions': 244,
        },
        'dwas': {
            'additions': 344,
            'deletions': 244,
        },
        'adss': {
            'additions': 3444,
            'deletions': 2444,
        },
        'asdgrzb': {
            'additions': 3444,
            'deletions': 244,
        },
        'ever': {
            'additions': 44,
            'deletions': 2442,
        },
        'what': {
            'additions': 3444,
            'deletions': 244,
        },
        'you': {
            'additions': 3444,
            'deletions': 244,
        },
        'say': {
            'additions': 3444,
            'deletions': 24,
        },
        'we': {
            'additions': 344,
            'deletions': 244,
        },
        'will': {
            'additions': 3444,
            'deletions': 244,
        },
        'do': {
            'additions': 3444,
            'deletions': 244,
        },
        'so': {
            'additions': 3444,
            'deletions': 244,
        },
        'please': {
            'additions': 3444,
            'deletions': 244,
        },
        'say': {
            'additions': 3444,
            'deletions': 244,
        },
        'some': {
            'additions': 3444,
            'deletions': 244,
        },
        'thing': {
            'additions': 3444,
            'deletions': 244,
        },
        'cool': {
            'additions': 3444,
            'deletions': 244,
        },
        'right': {
            'additions': 3444,
            'deletions': 244,
        },
        'now': {
            'additions': 3444,
            'deletions': 244,
        }
    }
}

from data_visualization.mirror_bar_chart import plot_with_slider
plot_with_slider(final_data)
# module_name = 'django/utils'
#
# #final_data = get_contributors_to_lines_changed_given_module(module_name)
#
#
# def plot():
#     contributors_list = []
#     additions_list = []
#     deletions_list = []
#     negated_list = []
#     contributors = final_data.keys()
#     for cont in contributors:
#         contributors_list.append(cont)
#         additions_list.append(final_data[cont]['additions'])
#         deletions_list.append(final_data[cont]['deletions'])
#         negated_list.append(-final_data[cont]['deletions'])
#     fig.add_trace(go.Bar(y=contributors_list, x=additions_list,
#                          base=0,
#                          marker_color='crimson',
#                          orientation='h',
#                          name='additions'))
#     fig.add_trace(go.Bar(y=contributors_list, x=deletions_list,
#                          base=negated_list,
#                          marker_color='grey',
#                          orientation='h',
#                          name='deletions'))
# # ad
# print(fig.data)
# # Create and add slider
# steps = []
# for i in range(len(years)):
#     step = dict(
#         method="restyle",
#         args=["visible", [False] * len(fig.data)],
#     )
#     step["args"][1][i] = True  # Toggle i'th trace to "visible"
#     steps.append(step)
#
# sliders = [dict(
#     active=10,
#     currentvalue={"prefix": "Date: "},
#     pad={"t": 50},
#     steps=steps
# )]
#
# fig.update_layout(
#     sliders=sliders
# )
# fig.show()


# def plot_with_slider():
#     for key in final_data:
#         years.append(key)
#         contributors_list = []
#         additions_list = []
#         deletions_list =[]
#         negated_list = []
#         contributors = final_data[key]
#         for cont in contributors:
#             contributors_list.append(cont)
#             additions_list.append(contributors[cont]['additions'])
#             deletions_list.append(contributors[cont]['deletions'])
#             negated_list.append(-contributors[cont]['deletions'])
#         fig.add_trace(go.Bar(y= contributors_list, x=additions_list,
#                              base = 0,
#                              visible = False,
#                              marker_color='crimson',
#                              orientation='h',
#                              name='additions'))
#         fig.add_trace(go.Bar(y=contributors_list, x=deletions_list,
#                              base=negated_list,
#                              visible=False,
#                              marker_color='grey',
#                              orientation='h',
#                              name='deletions'))
#
#     # Create and add slider
#     steps = []
#     fig.data[0].visible = True
#     fig.data[1].visible = True
#     for i in range(len(years)):
#         step = dict(
#             method="restyle",
#             args=["visible", [False] * len(fig.data)],
#         )
#         j = i*2
#         for k in range (j,j+2):
#             step["args"][1][k] = True  # Toggle i'th trace to "visible"
#         steps.append(step)
#
#     sliders = [dict(
#         active=0,
#         currentvalue={"prefix": "Date: "},
#         steps=steps
#     )]
#
#     fig.update_layout(
#         sliders=sliders
#     )
#     fig.show()
# plot_with_slider()
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