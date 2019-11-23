from .constants import NodeType


class Node:
    type: NodeType
    name: str


class Edge:
    src: Node
    dst: Node
    weight: int
