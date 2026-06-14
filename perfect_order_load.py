from pathlib import Path as P
import models.save_card_json as scj

set_id = 24587

# 1st try: 44

for i in range(45, 125):
    if i < 10:
        card_number = f"{set_id} 00{i}"
    elif i >= 10 and i < 100:
        card_number = f"{set_id} 0{i}"
    else:
        card_number = f"{set_id} {i}"

    scj.write_card_json_custom_folder(card_number, "perfect_order")
    print(f"Wrote data for {card_number}!")