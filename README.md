# Repository 구조

## etl

Extract, Transform, Load 파이프라인 스크립트, 레벨로 나누어져 있음. 최종 PostGreSQL (pokehunter) 데이터베이스에 로드하는 목표.

### data_load

pandas 데이터 프레임 형태 테이블을 PostGreSQL pokehunter 데이터베이스로 로드하는 스크립트 모임

```
username = "student"
password = ""
```

### data_transform

### l0: data cleaning

- `l0dc_basic_info.py` --> 기조정보 테이블
- `l0dc_tcgplayer_price_info.py` --> tcgplayer 가겨정보 테이블
- `l0dc_cardmarket_price_info.py` --> cardmarket 가겨정보 테이블
- `l0dc_set_name_id_mapping.py` --> 세트 명과 ID 매핑 테이블

## files

### l0dc

데이터 클리닝 단계에서 작성한 파일 모임, 합계한 json 파일들의 csv 형태

## models

- `compile.py`: 매개 폴더 안에 모든 json 파일을 합친 json을 파일로 쓰거나 dictionary 형태로 리턴하는 모델
  - 함수 목록: `merge_json_return`, `merge_json_save`, `merge_json_return_price`, `merge_json_save_price`
  - 현재는 카드 기초 정보하고 가격 정보를 따로 나눕니다
- `query_card_info.py`: 카드 정보를 파이썬 dictionary 형태로 리턴하는 함수를 제공하는 모델.
  - 함수 목록: `fetch_card_info`
- `query_price.py`
- `save_card_json.py`: 카드 정보를 쿼리, 프린트, 파일로 쓰는 함수를 제공하는 모델
  - 함수 목록: `fetch_card_info`, `print_card_info`, `write_card_info`
