from graph import Graph
from graph.display_graph import print_console_path, print_graph

graph = Graph()

v0 = graph.add_value_as_vertex(0)
v1 = graph.add_value_as_vertex(1)
v2 = graph.add_value_as_vertex(2)
v3 = graph.add_value_as_vertex(3)

graph.connect_two_vertex(v0, v1, "from v0 to v1")
graph.connect_two_vertex(v1, v3, "from v1 to v3")

print(graph)
print_graph(graph, [], None, None, ratio=70, format='pdf', name='my graph')
