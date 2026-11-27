import json


def lambda_handler(event, context):
    """Итоговая версия: отзыв без текста тоже обрабатывается."""
    for record in event["Records"]:
        review = json.loads(record["body"])
        review_id = review["id"]
        rating = review["rating"]
        text = review.get("text", "")[:20]
        print(f"{review_id}: {rating}/5 {text}", flush=True)
