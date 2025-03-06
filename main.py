from Agents.supervisor import supervisor



graph = supervisor.compile()
graph.get_graph().draw_mermaid_png(output_file_path="graph.png")
print('Graph created')


# Testing

# for chunk in graph.stream(
#     {"messages": [("human", "IOT")]}, stream_mode="values"
# ):
#     chunk["messages"][-1].pretty_print()
#
#