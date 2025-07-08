import requests

OLLAMA_BASE_URL = "http://localhost:11434"

def generate(model: str, prompt: str, stream: bool = False):
    url = f"{OLLAMA_BASE_URL}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream
    }

    response = requests.post(url, json=payload, stream=stream)

    if stream:
        for line in response.iter_lines():
            if line:
                data = line.decode('utf-8')
                print(data)
    else:
        data = response.json()
        return data.get("response", "")


def list_models():
    url = f"{OLLAMA_BASE_URL}/api/tags"
    response = requests.get(url)
    return response.json()


def pull_model(model: str):
    url = f"{OLLAMA_BASE_URL}/api/pull"
    payload = {"name": model}
    response = requests.post(url, json=payload, stream=True)
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))


def main():
    print("Ollama Client (Local)")
    print("---------------------")

    model = input("Enter model name (e.g., llama3, mistral): ").strip()

    # Optionally pull the model
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
