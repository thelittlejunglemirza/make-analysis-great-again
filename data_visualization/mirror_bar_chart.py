import plotly.graph_objects as go


def plot_with_slider(final_data):
    years = []

    fig = go.Figure()
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
                             visible = False,
                             marker_color='crimson',
                             orientation='h',
                             name='additions'))
        fig.add_trace(go.Bar(y=contributors_list, x=deletions_list,
                             base=negated_list,
                             visible=False,
                             marker_color='grey',
                             orientation='h',
                             name='deletions'))

    # Create and add slider
    steps = []
    fig.data[0].visible = True
    fig.data[1].visible = True
    for i in range(len(years)):
        step = dict(
            method="restyle",
            args=["visible", [False] * len(fig.data)],
        )
        j = i*2
        for k in range (j,j+2):
            step["args"][1][k] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Date: "},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )
    fig.show()