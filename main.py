import requests
import datetime
from pprint import pprint


def stackoverflow_requests():
    url = "https://api.stackexchange.com/2.3/questions?fromdate=1656028800&todate=1656201600&sort=creation&tagged" \
          "=python&site=stackoverflow"
    response = requests.get(url)
    questions = response.json()
    question_quantity = 0
    for question in questions['items']:
        question_quantity += 1
        print(f"id вопроса : {question['question_id']}\nдата размещения на сайте : {datetime.datetime.fromtimestamp(question['creation_date'], tz=datetime.timezone.utc)}\n")
    pprint(f"Всего в пероид с 2022-06-24 по 2022-06-26 на сайте было размещено {question_quantity} вопросов")


if __name__ == '__main__':
    stackoverflow_requests()
