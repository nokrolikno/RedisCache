from pydantic import BaseModel


class SetModel(BaseModel):
    key: str
    value: str


class ValueModel(BaseModel):
    value: str


class StateModel(BaseModel):
    state: bool
