from store import search

questions = [
    "Which Physics class has the least amount of classwork?",
    "How many credits do I need to take to declare my major?",
    "What is the university policy for snow days?",
    "How far is the university clinic from the library on campus?",
    "When is it a good time go the university dining hall on a Tuesday evening?",
]

for i, q in enumerate(questions, 1):
    results = search(q)
    top = results[0]
    print("=" * 80)
    print(f"Q{i}: {q}")
    print("-" * 80)
    print(top)
    print()
