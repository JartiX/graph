
class Node:
    """Вершина
    """
    def __init__(self, name: int | str):
        """Инициализация вершины

        Args:
            name (int / str): Название вершины
        """
        self.name = name
        self.edges = []

    def add_edge(self, neighbor: int | str, weight=1):
        """Добавление ребра

        Args:
            neighbor (int | str): Название соседней вершины
            weight (int, optional): Вес ребра. Defaults to 1.
        """
        if (neighbor, weight) not in self.edges:
            self.edges.append((neighbor, weight))

    def remove_edge(self, neighbor: int | str):
        """Удаление связи с вершиной

        Args:
            neighbor (int | str): Название соседней вершины
        """
        self.edges = [edge for edge in self.edges if edge[0] != neighbor]

    def get_neighbors(self) -> list:
        """Получить все соседние вершины

        Returns:
            list: Список соседних вершин
        """
        return [(neighbor, weight) for neighbor, weight in self.edges]

    def get_weight(self, neighbor: int | str):
        """Получить вес ребра

        Args:
            neighbor (int | str): Навание соседней вершины

        Returns:
            _type_: _description_
        """
        for n, weight in self.edges:
            if n == neighbor:
                return weight
        return None

    def __str__(self):
        """Вывод вершины

        Returns:
            str: Вершина
        """
        return f"Node({self.name}, Edges: {self.edges})"
