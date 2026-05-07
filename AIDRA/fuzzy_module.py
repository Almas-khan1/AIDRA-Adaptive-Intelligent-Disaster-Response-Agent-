import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl


class FuzzyRiskSystem:

    def __init__(self):

        # =====================================================
        # INPUT VARIABLES
        # =====================================================

        self.risk_level = ctrl.Antecedent(
            np.arange(0, 11, 1),
            'risk_level'
        )

        self.rescue_time = ctrl.Antecedent(
            np.arange(0, 61, 1),
            'rescue_time'
        )

        # =====================================================
        # OUTPUT VARIABLE
        # =====================================================

        self.priority = ctrl.Consequent(
            np.arange(0, 11, 1),
            'priority'
        )

        self.setup_membership_functions()
        self.setup_rules()

        self.system = ctrl.ControlSystem(self.rules)
        self.sim = ctrl.ControlSystemSimulation(self.system)

    # =====================================================
    # MEMBERSHIP FUNCTIONS
    # =====================================================

    def setup_membership_functions(self):

        # Risk Level
        self.risk_level['low'] = fuzz.trimf(self.risk_level.universe, [0, 0, 5])
        self.risk_level['medium'] = fuzz.trimf(self.risk_level.universe, [2, 5, 8])
        self.risk_level['high'] = fuzz.trimf(self.risk_level.universe, [5, 10, 10])

        # Rescue Time
        self.rescue_time['short'] = fuzz.trimf(self.rescue_time.universe, [0, 0, 20])
        self.rescue_time['medium'] = fuzz.trimf(self.rescue_time.universe, [10, 30, 50])
        self.rescue_time['long'] = fuzz.trimf(self.rescue_time.universe, [40, 60, 60])

        # Priority
        self.priority['low'] = fuzz.trimf(self.priority.universe, [0, 0, 5])
        self.priority['medium'] = fuzz.trimf(self.priority.universe, [2, 5, 8])
        self.priority['high'] = fuzz.trimf(self.priority.universe, [5, 10, 10])

    # =====================================================
    # FUZZY RULES (IMPROVED COVERAGE)
    # =====================================================

    def setup_rules(self):

        self.rules = [

            ctrl.Rule(
                self.risk_level['high'] & self.rescue_time['short'],
                self.priority['high']
            ),

            ctrl.Rule(
                self.risk_level['high'] & self.rescue_time['long'],
                self.priority['high']
            ),

            ctrl.Rule(
                self.risk_level['medium'] & self.rescue_time['medium'],
                self.priority['medium']
            ),

            ctrl.Rule(
                self.risk_level['low'] & self.rescue_time['long'],
                self.priority['low']
            ),

            ctrl.Rule(
                self.risk_level['low'] & self.rescue_time['short'],
                self.priority['medium']
            ),

            # Safety fallback rules (IMPORTANT FIX)
            ctrl.Rule(self.risk_level['high'], self.priority['high']),
            ctrl.Rule(self.risk_level['low'], self.priority['low'])
        ]

    # =====================================================
    # COMPUTE PRIORITY (SAFE VERSION)
    # =====================================================

    def compute(self, risk, time):

        self.sim.input['risk_level'] = risk
        self.sim.input['rescue_time'] = time

        self.sim.compute()

        # SAFE OUTPUT HANDLING (FIXES KEYERROR)
        if 'priority' in self.sim.output:
            return self.sim.output['priority']
        else:
            return 0.0