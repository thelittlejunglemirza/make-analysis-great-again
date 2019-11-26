import plotly.graph_objects as go
from data_collection.processes.module_name_to_commit_dates import get_module_name_to_commit_dates

module_name_to_dates_map = get_module_name_to_commit_dates()
fig = go.Figure()

for module_name in module_name_to_dates_map.keys():
    dates = module_name_to_dates_map[module_name]
    fig.add_trace(go.Box(y=dates, name=module_name))

fig.show()
