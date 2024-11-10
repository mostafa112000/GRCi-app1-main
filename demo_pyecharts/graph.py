from pyecharts import options as opts

from pyecharts.charts import Graph
from streamlit_echarts import st_pyecharts


def render_basic_graph_chart():
    nodes = [
        {"name": "Node1", "symbolSize": 10},
        {"name": "Node2", "symbolSize": 20},
        {"name": "Node3", "symbolSize": 30},
        {"name": "Node4", "symbolSize": 40},
        {"name": "Node5", "symbolSize": 50},
        {"name": "Node6", "symbolSize": 40},
        {"name": "Node7", "symbolSize": 30},
        {"name": "Node8", "symbolSize": 20},
    ]
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})
    c = (
        Graph()
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title="Graph-Basic example"))
    )
    st_pyecharts(c)


ST_GRAPH_DEMOS = {
    "Graph: Basic Graph": (
        render_basic_graph_chart,
        "https://gallery.pyecharts.org/#/Graph/graph_base",
    )
}