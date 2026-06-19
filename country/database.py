from sqlalchemy.ext.asyncio import AsyncSession,create_async_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_async_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)
Base = declarative_base()
import models
async def init_all():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
async def get_db():
    async with SessionLocal() as session:
        yield session
        