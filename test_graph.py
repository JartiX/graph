import pytest
from graph import Graph
from graph.node import Node


def test_node_creation():
    node = Node("A")
    assert node.name == "A"
    assert node.edges == []


def test_add_edge():
    node = Node("A")
    node.add_edge("B", 5)
    assert node.edges == [("B", 5)]
    node.add_edge("C", 3)
    assert node.edges == [("B", 5), ("C", 3)]
    node.add_edge("B", 5)  # Повторное добавление не должно изменить список
    assert node.edges == [("B", 5), ("C", 3)]


def test_remove_edge():
    node = Node("A")
    node.add_edge("B", 5)
    node.add_edge("C", 3)
    node.remove_edge("B")
    assert node.edges == [("C", 3)]
    node.remove_edge("C")
    assert node.edges == []


def test_get_neighbors():
    node = Node("A")
    node.add_edge("B", 5)
    node.add_edge("C", 3)
    assert node.get_neighbors() == [("B", 5), ("C", 3)]


def test_get_weight():
    node = Node("A")
    node.add_edge("B", 5)
    node.add_edge("C", 3)
    assert node.get_weight("B") == 5
    assert node.get_weight("C") == 3
    assert node.get_weight("D") is None


def test_graph_creation():
    graph = Graph()
    assert graph.nodes == {}
    assert graph.is_oriented is False


def test_add_vertex():
    graph = Graph()
    graph.add_vertex("A")
    assert "A" in graph.nodes
    assert isinstance(graph.nodes["A"], Node)


def test_remove_vertex():
    graph = Graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_edge("A", "B")
    graph.remove_vertex("A")
    assert "A" not in graph.nodes
    assert "B" in graph.nodes
    assert graph.nodes["B"].edges == []


def test_add_edge():
    graph = Graph()
    graph.add_edge("A", "B", 2)
    assert "A" in graph.nodes
    assert "B" in graph.nodes
    assert graph.nodes["A"].edges == [("B", 2)]
    assert graph.nodes["B"].edges == [("A", 2)]


def test_remove_edge():
    graph = Graph()
    graph.add_edge("A", "B", 2)
    graph.remove_edge("A", "B")
    assert graph.nodes["A"].edges == []
    assert graph.nodes["B"].edges == []


def test_get_neighbors():
    graph = Graph()
    graph.add_edge("A", "B", 2)
    graph.add_edge("A", "C", 3)
    assert graph.get_neighbors("A") == [("B", 2), ("C", 3)]


def test_get_weight():
    graph = Graph()
    graph.add_edge("A", "B", 2)
    assert graph.get_weight("A", "B") == 2
    assert graph.get_weight("B", "A") == 2
    assert graph.get_weight("A", "C") is None


def test_is_adjacent():
    graph = Graph()
    graph.add_edge("A", "B", 2)
    assert graph.is_adjacent("A", "B") is True
    assert graph.is_adjacent("B", "A") is True
    assert graph.is_adjacent("A", "C") is False
