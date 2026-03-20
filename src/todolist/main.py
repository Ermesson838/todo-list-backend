from fastapi import FastAPI
from sentry_sdk.envelope import Item

from todolist.list_item import ListItem

app = FastAPI()
itens = []


@app.get("/items")
def read_root():
    return itens

@app.post("/items")
def create_item(item: ListItem):
    itens.append(item)
    return item
