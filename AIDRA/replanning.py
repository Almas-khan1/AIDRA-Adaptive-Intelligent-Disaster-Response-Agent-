from search_algorithms import SearchAlgorithms


class DynamicReplanner:

    def __init__(self, environment):

        self.env = environment

        self.search_agent = SearchAlgorithms(
            self.env
        )

    # =====================================================
    # BLOCK ROAD DYNAMICALLY
    # =====================================================

    def add_dynamic_obstacle(self, obstacle):

        self.env.grid[
            obstacle[0]
        ][
            obstacle[1]
        ] = self.env.BLOCKED

        print(f"\nNew obstacle added at {obstacle}")

    # =====================================================
    # REPLAN ROUTE
    # =====================================================

    def replan_route(self, start, goal):

        print("\n===== REPLANNING ROUTE =====")

        result = self.search_agent.a_star(
            start,
            goal
        )

        if result:

            print("\nNEW PATH FOUND:")

            print(result["path"])

            print(f"\nNew Cost: {result['cost']}")

            print(f"Risk Score: {result['risk']}")

            print(f"Nodes Expanded: {result['nodes_expanded']}")

        else:

            print("\nNO PATH AVAILABLE")

        return result