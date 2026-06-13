from pathlib import Path as P
import models.save_card_json as scj

set_id = 24541

# for i in range(218, 296):
#     card_number = f"{set_id} {i}"

#     scj.write_card_json(card_number)
#     print(f"Wrote data for {card_number}!")

# until 243 gengar first try
# until 291 canari second try

for i in range(291, 296):
    card_number = f"{set_id} {i}"

    scj.write_card_json(card_number)
    print(f"Wrote data for {card_number}!")