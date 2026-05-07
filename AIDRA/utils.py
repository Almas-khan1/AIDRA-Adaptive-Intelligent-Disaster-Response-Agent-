# =====================================================
# PRINT SEARCH RESULTS
# =====================================================

def print_search_result(name, result):

    print(f"\n===== {name} RESULT =====")

    if result is None:

        print("No path found")

        return

    print("\nPath:")
    print(result["path"])

    print(f"\nCost: {result['cost']}")

    print(f"Risk Score: {result['risk']}")

    print(f"Nodes Expanded: {result['nodes_expanded']}")


# =====================================================
# PRINT ML RESULTS
# =====================================================

def print_ml_results(results):

    print(f"\n===== {results['Model']} RESULTS =====")

    print(f"Accuracy: {results['Accuracy']:.2f}")

    print(f"Precision: {results['Precision']:.2f}")

    print(f"Recall: {results['Recall']:.2f}")

    print(f"F1 Score: {results['F1 Score']:.2f}")

    print("\nConfusion Matrix:")

    print(results["Confusion Matrix"])


# =====================================================
# PRINT SECTION TITLE
# =====================================================

def print_section(title):

    print("\n" + "=" * 50)

    print(title)

    print("=" * 50)