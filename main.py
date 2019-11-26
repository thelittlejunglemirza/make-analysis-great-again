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
import numpy as np
from data_collection.processes.contributor_to_lines_changed import get_contributors_to_lines_changed_given_module

years = []

fig = go.Figure()
final_data = {
    '2017': {
        '1': {
            'additions': 2376,
            'deletions': 355
        },
        '2': {
            'additions': 3444,
            'deletions': 244,
        },
        '2': {
            'additions': 3444,
            'deletions': 244,
        },
        '3': {
            'additions': 3444,
            'deletions': 244,
        },
        '4': {
            'additions': 3444,
            'deletions': 244,
        },
        '5': {
            'additions': 3444,
            'deletions': 244,
        },
        '6': {
            'additions': 3444,
            'deletions': 244,
        },
        '7': {
            'additions': 3444,
            'deletions': 244,
        },
        '8': {
            'additions': 3444,
            'deletions': 244,
        },
        '9': {
            'additions': 3444,
            'deletions': 244,
        },
        '10': {
            'additions': 3444,
            'deletions': 244,
        },
        '11': {
            'additions': 3444,
            'deletions': 244,
        },
        '12': {
            'additions': 3444,
            'deletions': 244,
        },
        '13': {
            'additions': 3444,
            'deletions': 244,
        },
        '14': {
            'additions': 3444,
            'deletions': 244,
        },
        '15': {
            'additions': 3444,
            'deletions': 244,
        },
        '16': {
            'additions': 3444,
            'deletions': 244,
        },
        '17': {
            'additions': 3444,
            'deletions': 244,
        },
        '18': {
            'additions': 3444,
            'deletions': 244,
        },
        '19': {
            'additions': 3444,
            'deletions': 244,
        },
        '20': {
            'additions': 3444,
            'deletions': 244,
        }
    },
    '2018': {
        '1': {
            'additions': 100,
            'deletions': 35
        },
        '2': {
            'additions': 344,
            'deletions': 24,
        },
        '2': {
            'additions': 344,
            'deletions': 24,
        },
        '3': {
            'additions': 344,
            'deletions': 24,
        },
        '4': {
            'additions': 344,
            'deletions': 24,
        },
        '5': {
            'additions': 344,
            'deletions': 24,
        },
        '6': {
            'additions': 344,
            'deletions': 24,
        },
        '7': {
            'additions': 344,
            'deletions': 24,
        },
        '8': {
            'additions': 344,
            'deletions': 24,
        },
        '9': {
            'additions': 344,
            'deletions': 24,
        },
        '10': {
            'additions': 344,
            'deletions': 24,
        },
        '11': {
            'additions': 344,
            'deletions': 24,
        },
        '12': {
            'additions': 344,
            'deletions': 24,
        },
        '13': {
            'additions': 344,
            'deletions': 24,
        },
        '14': {
            'additions': 344,
            'deletions': 24,
        },
        '15': {
            'additions': 344,
            'deletions': 24,
        },
        '16': {
            'additions': 344,
            'deletions': 24,
        },
        '17': {
            'additions': 344,
            'deletions': 24,
        },
        '18': {
            'additions': 344,
            'deletions': 24,
        },
        '19': {
            'additions': 344,
            'deletions': 24,
        },
        '20': {
            'additions': 344,
            'deletions': 24,
        }
    }
}


module_name = 'django/utils'

#final_data = get_contributors_to_lines_changed_given_module(module_name)


def plot():
    contributors_list = []
    additions_list = []
    deletions_list = []
    negated_list = []
    contributors = final_data.keys()
    for cont in contributors:
        contributors_list.append(cont)
        additions_list.append(final_data[cont]['additions'])
        deletions_list.append(final_data[cont]['deletions'])
        negated_list.append(-final_data[cont]['deletions'])
    fig.add_trace(go.Bar(y=contributors_list, x=additions_list,
                         base=0,
                         marker_color='crimson',
                         orientation='h',
                         name='additions'))
    fig.add_trace(go.Bar(y=contributors_list, x=deletions_list,
                         base=negated_list,
                         marker_color='grey',
                         orientation='h',
                         name='deletions'))
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


def plot_with_slider():
    for key in final_data:
        years.append(key)
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

    # Create and add slider
    steps = []
    print(fig)
    for i in range(len(years)):
        step = dict(
            method="restyle",
            args=["visible", [False] * len(years) * 2],
        )

        j = i*2
        for k in range(j, j+2):
            step["args"][1][k] = True
        steps.append(step)
    print(steps)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Date: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )
    fig.show()
plot_with_slider()
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