import json


def lambda_handler(event, context):
    """Первая версия: ожидает, что поле text есть в каждом отзыве."""
    for record in event["Records"]:
        review = json.loads(record["body"])
        review_id = review["id"]
        rating = review["rating"]
        text = review["text"][:20]  # KeyError для отзыва без текста
        print(f"{review_id}: {rating}/5 {text}", flush=True)
