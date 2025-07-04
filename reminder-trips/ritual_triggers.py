=== SIVE RITUAL ALTAR PROJECT ===

ritual_triggers.py — Handle symbolic trigger phrases

def detect_trigger(user_input, codex_entries, reminder, trips): lowered = user_input.lower()

# Reminder trigger
if lowered.startswith("reminder:"):
    return reminder

# Trip trigger (e.g., "Trip D" or "Invoke Trip F")
for trip_name in trips:
    if trip_name.lower().split(".")[0] in lowered or trip_name.lower() in lowered:
        return trips[trip_name]

# Codex Entry trigger (e.g., "Entry #74")
for entry_name in codex_entries:
    if any(token in lowered for token in [entry_name.lower(), entry_name.lower().split(".")[0]]):
        return codex_entries[entry_name]

return None
