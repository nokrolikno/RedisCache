import logging

from fastapi import FastAPI

from models import SetModel, GetModel, ValueModel, StateModel

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
    return StateModel(state=True)


@app.get("/get", response_model=ValueModel)
async def get_value(data: GetModel):
    key = data.key
    return ValueModel(value=key)
