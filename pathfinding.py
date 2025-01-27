from collections import deque

class Pathfinding:
    def __init__(self, game):
        self.game = game
        self.map = game.map.mini_map
        self.ways = [-1, 0], [0, -1], [1, 0], [0, 1], [-1, -1], [1, -1], [1, -1], [-1, 1]
        self.graph = {}
        self.get_graph()