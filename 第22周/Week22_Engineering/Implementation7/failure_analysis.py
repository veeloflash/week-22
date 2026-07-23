def analyze_failure(query, retrieved, correct):
    if correct not in retrieved:
        return "Retrieval failure: correct answer not found."
    if len(retrieved) == 0:
        return "Empty retrieval: no context returned."
    return "Context mismatch or LLM misinterpretation."

if __name__ == "__main__":
    print(analyze_failure("python", ["java info"], "python info"))
