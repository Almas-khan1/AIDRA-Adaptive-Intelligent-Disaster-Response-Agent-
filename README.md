# AIDRA-Adaptive-Intelligent-Disaster-Response-Agent-
AIDRA (Adaptive Intelligent Disaster Response Agent) is an AI-based system that simulates disaster scenarios using a grid environment. It integrates machine learning for victim triage, search algorithms for pathfinding, and CSP for resource allocation. The system demonstrates intelligent, adaptive decision-making for emergency rescue operations.


Here is a clean, professional, easy-English `README.md` for your AIDRA project:



# AIDRA - Adaptive Intelligent Disaster Response Agent

## Project Description

AIDRA is an AI-based disaster management system designed to support emergency response operations during natural or man-made disasters. The system simulates a disaster environment and applies multiple artificial intelligence techniques to optimize rescue operations, resource allocation, and decision-making.

The project integrates Machine Learning, Search Algorithms, Constraint Satisfaction Problems (CSP), and Fuzzy Logic to create an intelligent and adaptive rescue system.



## Objectives

* Simulate a disaster environment using a grid-based model
* Predict patient triage priority using machine learning
* Find optimal rescue paths using search algorithms
* Allocate emergency resources efficiently using CSP
* Handle uncertainty using fuzzy logic
* Adapt to dynamic changes in the environment through replanning



## Features

* Grid-based disaster environment simulation
* Victim classification based on severity levels
* Pathfinding using BFS and A* algorithms
* Resource allocation using constraint satisfaction approach
* Machine learning models (KNN and Naive Bayes) for prediction
* Fuzzy logic system for priority evaluation
* Dynamic replanning when environment changes



## Technologies Used

* Python
* NumPy
* Pandas
* Scikit-learn
* Scikit-fuzzy
* Matplotlib



## Project Structure

AIDRA/

* main.py
* environment.py
* search_algorithms.py
* csp_allocator.py
* ml_module.py
* fuzzy_module.py
* replanning.py
* utils.py
* requirements.txt
* dataset/

  * synthetic_medical_triage.csv


## Modules Explanation

### 1. Environment Module

Creates a grid-based disaster simulation environment containing victims, hazards, blocked roads, hospitals, and a rescue base.

### 2. Machine Learning Module

Uses classification algorithms to predict medical triage priority based on patient data.

### 3. Search Algorithms Module

Implements BFS, DFS, Greedy Best First Search, and A* for optimal path planning.

### 4. CSP Module

Allocates victims to available ambulances based on priority constraints.

### 5. Fuzzy Logic Module

Handles uncertainty in disaster conditions and calculates priority scores.

### 6. Replanning Module

Updates routes dynamically when new obstacles are introduced.



## Dataset

The system uses a synthetic medical triage dataset containing:

* Age
* Heart rate
* Blood pressure
* Oxygen saturation
* Temperature
* Pain level
* Medical history indicators
* Arrival mode
* Triage level (target variable)



## Output

The system provides:

* ML model accuracy comparison
* Optimal rescue paths
* Resource allocation plan
* Fuzzy priority score
* Dynamic route replanning results



## Conclusion

AIDRA demonstrates how multiple artificial intelligence techniques can be integrated into a single system for efficient disaster response management. It combines learning, reasoning, optimization, and uncertainty handling to simulate real-world emergency scenarios.

