from pathlib import Path as P
import models.save_card_json as scj

set_id = 23821

for i in range(100, 181):
    card_number = f"{set_id} {i}"

    scj.write_card_json(card_number)
    print(f"Wrote data for {card_number}!")
