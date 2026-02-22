from agent import PromptAgent
from memory import Memory


def main():
    # PASTE YOUR KEY HERE
    api_key = "Open_AI_key"

    agent = PromptAgent(api_key)
    memory = Memory()

    print("--- AI Prompt Improver Agent ---")
    print("Type 'exit' to quit.")

    while True:
        user_input = input("\nEnter raw prompt: ")
        if user_input.lower() == 'exit':
            break

        if not user_input.strip():
            continue

        print("Processing...")
        improved_version = agent.improve(user_input)

        print(improved_version)
        memory.save_interaction(user_input, improved_version)


if __name__ == "__main__":
    main()
