import logging

from fastapi import FastAPI

import redis_interaction
from models import SetModel, ValueModel, StateModel

logging.basicConfig(format="%(asctime)s %(message)s",
                    datefmt="%I:%M:%S %p", level=logging.INFO)

app = FastAPI()


@app.on_event("startup")
def startup():
    """Function running on server startup"""
    logging.info("Running server startup")

    logging.info("Startup done")


@app.post("/set", response_model=StateModel)
async def set_key_value(data: SetModel):
    key = data.key
    value = data.value
    logging.info(f"Adding key-value pair: {key} -- {value}")
    state = redis_interaction.r_set(key, value)
    return StateModel(state=state)


@app.get("/get", response_model=ValueModel)
async def get_value(key: str):
    value = redis_interaction.r_get(key)
    return ValueModel(value=value)
