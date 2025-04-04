from util import markdown_to_blocks, text_to_nodes, text_node_to_html_node


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    textnodes = list(map(text_to_nodes, blocks))
    html_nodes = list(map(text_node_to_html_node, textnodes))
