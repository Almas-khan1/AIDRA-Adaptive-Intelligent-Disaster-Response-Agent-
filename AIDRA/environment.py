import matplotlib.pyplot as plt
import numpy as np


class DisasterEnvironment:

    def __init__(self, size=10):

        self.size = size
        self.grid = np.zeros((size, size))

        # Cell types
        self.EMPTY = 0
        self.BLOCKED = 1
        self.HAZARD = 2
        self.HOSPITAL = 3
        self.VICTIM = 4
        self.BASE = 5

        # Base
        self.base_location = (0, 0)
        self.grid[self.base_location] = self.BASE

        # Hospitals
        self.hospitals = [(9, 9), (0, 9)]
        for h in self.hospitals:
            self.grid[h] = self.HOSPITAL

        # Victims (SOURCE OF TRUTH)
        self.victims = {
            "V1": {"location": (2, 7), "severity": "Critical"},
            "V2": {"location": (8, 3), "severity": "Critical"},
            "V3": {"location": (6, 9), "severity": "Moderate"},
            "V4": {"location": (1, 5), "severity": "Moderate"},
            "V5": {"location": (7, 7), "severity": "Minor"}
        }

        for v in self.victims.values():
            self.grid[v["location"]] = self.VICTIM

        # Hazards
        self.hazards = [(4, 4), (4, 5), (5, 5), (6, 5)]
        for h in self.hazards:
            self.grid[h] = self.HAZARD

        # Blocked roads
        self.blocked_roads = [(3, 3), (3, 4), (7, 2)]
        for b in self.blocked_roads:
            self.grid[b] = self.BLOCKED

    def display_environment(self):

        plt.figure(figsize=(7, 7))

        for x in range(self.size):
            for y in range(self.size):

                val = self.grid[x, y]

                color = "white"

                if val == self.BLOCKED:
                    color = "black"
                elif val == self.HAZARD:
                    color = "red"
                elif val == self.HOSPITAL:
                    color = "green"
                elif val == self.VICTIM:
                    color = "orange"
                elif val == self.BASE:
                    color = "blue"

                plt.scatter(y, self.size - x - 1, c=color, s=500, edgecolors="black")

        plt.title("AIDRA Environment")
        plt.grid(True)
        plt.xticks(range(self.size))
        plt.yticks(range(self.size))
        plt.show()