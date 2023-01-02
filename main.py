from alembic.config import Config
from alembic import command
import uvicorn
from app.main import get_application

alembic_cfg = Config("alembic.ini")
command.current(alembic_cfg, verbose=True)
command.upgrade(alembic_cfg, "fdf8821871d7")

app = get_application()
uvicorn.run(app, host='0.0.0.0')
