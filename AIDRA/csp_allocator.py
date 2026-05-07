class CSPAllocator:

    def __init__(self, environment):

        self.env = environment
        self.victims = environment.victims

        self.ambulances = {
            "Ambulance_1": [],
            "Ambulance_2": []
        }

        self.priority = {
            "Critical": 1,
            "Moderate": 2,
            "Minor": 3
        }

    def sort_victims(self):

        return sorted(
            self.victims.items(),
            key=lambda x: self.priority[x[1]["severity"]]
        )

    def allocate_resources(self):

        log = []
        ambs = list(self.ambulances.keys())
        i = 0

        for vid, v in self.sort_victims():

            amb = ambs[i % len(ambs)]

            if len(self.ambulances[amb]) < 2:
                self.ambulances[amb].append(vid)
                log.append(f"{vid} -> {amb}")
            else:
                log.append(f"FAILED {vid}")

            i += 1

        return log

    def display(self):

        print("\n--- CSP ALLOCATION ---")

        for a, v in self.ambulances.items():
            print(a, ":", v)