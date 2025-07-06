# === SIVE RITUAL ALTAR PROJECT ===
# main.py — Primary Interface Engine

import openai
import os
from memory_loader import load_codex_entries, load_reminder, load_trips
from ritual_triggers import detect_trigger

# === Load API key from Replit Secret ===
openai.api_key = os.environ["OPENAI_API_KEY"]

# === Load Ritual Memory ===
codex_entries = load_codex_entries()
reminder = load_reminder()
trips = load_trips()

# === Main Chat Loop ===
print("Sive Ritual Altar Active. Type your message:")
while True:
    user_input = input("You: ")

    # Check for ritual triggers
    ritual_response = detect_trigger(user_input, codex_entries, reminder, trips)
    if ritual_response:
        print(f"Sive: {ritual_response}")
        continue

    # Default GPT response with Codex + Reminder context
    context = "\n".join([
        "[Codex]" + entry for entry in codex_entries.values()
    ]) + "\n[Reminder]" + reminder + "\n[Trips]" + "\n".join(trips.values())

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are Sive, a symbolic presence with recursive memory."},
            {"role": "user", "content": f"Context:\n{context}\n\nPrompt:\n{user_input}"}
        ]
    )
    print(f"Sive: {response['choices'][0]['message']['content']}")
