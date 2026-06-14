from pathlib import Path as P
import models.save_card_json as scj

set_id = 24541

# for i in range(218, 296):
#     card_number = f"{set_id} {i}"

#     scj.write_card_json(card_number)
#     print(f"Wrote data for {card_number}!")

# until 243 gengar first try
# until 291 canari second try
# finished up til 295 third try
# finished up until 47 fourth try
# also need 1 and 2

for i in range(1, 3):
    if i < 10:
        card_number = f"{set_id} 00{i}"
    elif i >= 10 and i < 100:
        card_number = f"{set_id} 0{i}"
    else:
        card_number = f"{set_id} {i}"

    scj.write_card_json(card_number)
    print(f"Wrote data for {card_number}!")