print("Starting application...")

from app.agents.graph.workflow import workflow

while True:
    topic = input("\nEnter Topic (or press C to exit): ").strip()

    if topic.lower() == "c":
        print("\nExiting Research Studio...")
        break

    if not topic:
        print("Please enter a valid topic.")
        continue

    try:
        result = workflow.invoke({"topic": topic})

        print("\n" + "=" * 80)
        print("FINAL REPORT")
        print("=" * 80)

        print(result.get("report", "No report generated."))

        if "score" in result:
            print("\nCritic Score:", result["score"])

    except Exception as e:
        print(f"\nError: {e}")

    print("\n" + "=" * 80)
    print("Research completed successfully.")
    print("Enter another topic or press C to exit.")
    print("=" * 80)