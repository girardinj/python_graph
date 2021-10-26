from graph import Graph

graph = Graph()

v0 = graph.add_value_as_vertex(0)
v1 = graph.add_value_as_vertex(1)
v2 = graph.add_value_as_vertex(2)
v3 = graph.add_value_as_vertex(3)

graph.connect_two_vertex(v0, v1, "salut")
graph.connect_two_vertex(v1, v3, "Bonjour")

print(graph)