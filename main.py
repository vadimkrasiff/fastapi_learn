
from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Data base cleared")
    await create_tables()
    print("Data base created")

    yield
    print("Disconnect")

app = FastAPI(lifespan=lifespan)

    
app.include_router(router=tasks_router)
