from node import Node


class Graph:
    """Граф
    """
    def __init__(self, is_oriented=False):
        """Инициализация графа

        Args:
            is_oriented (bool, optional): Ориентированность графа. Defaults to False.
        """
        self.nodes = {}
        self.is_oriented = is_oriented

    def add_vertex(self, name: int | str) -> None:
        """Добавление вершины

        Args:
            name (int | str): Название вершины
        """
        if name not in self.nodes:
            self.nodes[name] = Node(name)

    def remove_vertex(self, name: int | str) -> None:
        """Удаление вершины

        Args:
            name (int | str): Название вершины
        """
        if name in self.nodes:
            # Удаляем вершину из всех её соседей
            for node in self.nodes.values():
                node.remove_edge(name)
            # Удаляем саму вершину
            del self.nodes[name]

    def add_edge(self, u: int | str, v: int | str, weight=1) -> None:
        """Добавить ребро

        Args:
            u (int | str): Вершина 1
            v (int | str): Вершина 2
            weight (int, optional): Вес ребра. Defaults to 1.
        """
        self.add_vertex(u)
        self.add_vertex(v)
        self.nodes[u].add_edge(v, weight)
        if not self.is_oriented:
            self.nodes[v].add_edge(u, weight)

    def remove_edge(self, u: int | str, v: int | str) -> None:
        """Удалить ребро

        Args:
            u (int | str): Вершина 1
            v (int | str): Вершина 2
        """
        if u in self.nodes:
            self.nodes[u].remove_edge(v)
        if not self.is_oriented and v in self.nodes:
            self.nodes[v].remove_edge(u)

    def get_neighbors(self, name: int | str) -> list:
        """Получить соседей вершины

        Args:
            name (int | str): Название вершины

        Returns:
            list: Соседи вершины
        """
        if name in self.nodes:
            return self.nodes[name].get_neighbors()
        return []

    def get_weight(self, u: int | str, v: int | str) -> float:
        """Получить вес ребра

        Args:
            u (int | str): Вершина 1
            v (int | str): Вершина 2

        Returns:
            float: Вес ребра
        """
        if u in self.nodes:
            return self.nodes[u].get_weight(v)
        return None

    def is_adjacent(self, u: int | str, v: int | str) -> bool:
        """Проверка вершин на связность

        Args:
            u (int | str): Вершина 1
            v (int | str): Вершина 2

        Returns:
            bool: Связность вершин
        """
        for neigbor, weight in self.get_neighbors(u):
            if neigbor == v:
                return True
        return False

    def __str__(self):
        """Вывод графа

        Returns:
            str: Граф
        """
        result = ""
        for node in self.nodes.values():
            result += f"{node}\n"
        return result