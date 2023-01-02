import subprocess

from fastapi import APIRouter, Body, Depends, HTTPException
from starlette import status
from starlette.status import HTTP_400_BAD_REQUEST

from app.api.dependencies.authentication import get_current_user_authorizer

from app.models.domain.users import User
from app.models.schemas.debug import DoExecution, ExecutionInResponse, FlagInResponse

from app.resources.strings import Injection, DescriptionInjection

router = APIRouter()


def execute(cmd):
    if cmd.startswith("uptime"):
        p = subprocess.Popen(cmd, shell=True,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             close_fds=True)
        err = p.stderr.read()
        if "rm" in cmd:
            return 0, "Don't delete anything!"
        if "||" in cmd:
            return 0, "injection block"
        if cmd.replace(" ", "") == "uptime" or cmd.replace(" ", "") == "uptime;":
            return 1, p.stdout.read().decode()
        if cmd != "uptime" and len(err) == 0:
            return 2, p.stdout.read().decode()
        else:
            return 0, "Error"
    return 0, {"whitelist": {"commands": ['uptime']}}

@router.post(
    "",
    status_code=status.HTTP_200_OK,
    name="debug",
)
async def create_comment_for_article(
        execution: DoExecution = Body(..., embed=True, alias="body"),
        user: User = Depends(get_current_user_authorizer()),
):
    code , stdout = execute(execution.command)
    if code == 0:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail=stdout,
        )
    if code == 1:
        return ExecutionInResponse(stdout=stdout)
    if code == 2:
        return FlagInResponse(
                flag=Injection(),description=DescriptionInjection,stdout=stdout
        )

