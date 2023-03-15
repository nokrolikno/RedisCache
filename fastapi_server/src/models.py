from pydantic import BaseModel


class SetModel(BaseModel):
    key: str
    value: str


class GetModel(BaseModel):
    key: str


class ValueModel(BaseModel):
    value: str


class StateModel(BaseModel):
    state: bool
