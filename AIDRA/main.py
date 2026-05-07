from environment import DisasterEnvironment
from search_algorithms import SearchAlgorithms
from csp_allocator import CSPAllocator
from ml_module import MLModule
from fuzzy_module import FuzzyRiskSystem


def main():

    env = DisasterEnvironment()
    env.display_environment()

    ml = MLModule("dataset/synthetic_medical_triage.csv")
    print("ML:", ml.run())

    csp = CSPAllocator(env)
    print(csp.allocate_resources())
    csp.display()

    search = SearchAlgorithms(env)

    start = env.base_location
    goal = env.victims["V1"]["location"]

    print(search.a_star(start, goal))

    fuzzy = FuzzyRiskSystem()
    print("Fuzzy Priority:", fuzzy.compute(7, 20))


if __name__ == "__main__":
    main()