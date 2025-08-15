def calculate_love_score(name1, name2):
    merged_str = (name1 + name2).upper()

    true_total = sum(merged_str.count(ch) for ch in "TRUE")
    love_total = sum(merged_str.count(ch) for ch in "LOVE")

    love_score = int(f"{true_total}{love_total}")
    print(love_score)