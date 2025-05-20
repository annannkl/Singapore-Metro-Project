def get_station_code_by_name(graph, prompt):
    name = input(f"\n📍 {prompt} ").strip().lower()
    matches = [v for v in graph.vertices.values() if v.data.lower() == name]

    if not matches:
        print(f"\n\033[91m❌ No station named '{name.title()}'. Please try again.\033[0m")
        return get_station_code_by_name(graph, prompt)

    if len(matches) == 1:
        print(f"\n\033[92m✅ Found: {matches[0].data} (Code: {matches[0].key})\033[0m")
        return matches[0].key

    print(f"\n\033[93m🔎 Multiple stations found with the name '{name.title()}':\033[0m")
    print("-" * 60)
    for v in matches:
        print(f"• 📌 Station: \033[96m{v.data}\033[0m | 🆔 Code: \033[95m{v.key}\033[0m | 🚆 Line: {v.key[:2]}")
    print("-" * 60)

    code = input("🔡 Please enter the \033[95mstation code\033[0m from the list above: ").strip().upper()
    if code in graph.vertices:
        print(f"\n\033[92m✅ You selected: {graph.vertices[code].data} (Code: {code})\033[0m")
        return code
    else:
        print(f"\n\033[91m❌ Invalid code '{code}'. Please try again.\033[0m")
        return get_station_code_by_name(graph, prompt)