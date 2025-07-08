# main.py
from ai_client import generate, pull_model

def main():
    print("Ollama Client (Local)")
    print("---------------------")

    model = input("Enter model name (e.g., llama3, mistral): ").strip()

    choice = input(f"Do you want to pull '{model}' model? (y/n): ").lower()
    if choice == 'y':
        pull_model(model)

    while True:
        prompt = input("\nEnter prompt (or 'exit' to quit): ")
        if prompt.lower() == "exit":
            break
        response = generate(model, prompt)
        print(f"\n🧠 Response:\n{response}")


if __name__ == "__main__":
    main()
