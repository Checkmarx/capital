from typing import Optional

from app.models.schemas.rwschema import RWSchema


class ExecutionInResponse(RWSchema):
    stdout: str

class FlagInResponse(ExecutionInResponse):
    flag: str
    description: str

class DoExecution(RWSchema):
    command: str
