from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import engine, Base, get_db
from schemas import (
    CountryCreate,
    CountryUpdate,
    CountryResponse,
    StateCreate,
    StateUpdate,
    StateResponse,
    DistrictCreate,
    DistrictUpdate,
    DistrictResponse,
    VillageCreate,
    VillageUpdate,
    VillageResponse,
    VillageHierarchyResponse
    )

import crud

app = FastAPI()


@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


# Country

@app.post("/country", response_model=CountryResponse)
async def create_country(
    country: CountryCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_country(db, country)


@app.get("/country", response_model=list[CountryResponse])
async def get_country(
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_country(db)


@app.put("/country/{country_id}",response_model=CountryResponse)
async def update_country(
    country_id: int,
    country: CountryUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_country(
        db,
        country_id,
        country
    )


@app.delete("/country/{country_id}")
async def soft_delete_country(
    country_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.soft_delete_country(
        db,
        country_id
    )


@app.delete("/country/hard/{country_id}")
async def hard_delete_country(
    country_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.hard_delete_country(
        db,
        country_id
    )


# State

@app.post("/states", response_model=StateResponse)
async def create_state(
    state: StateCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_state(db, state)


@app.get("/states", response_model=list[StateResponse])
async def get_states(
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_states(db)


@app.put("/states/{state_id}",
         response_model=StateResponse)
async def update_state(
    state_id: int,
    state: StateUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_state(
        db,
        state_id,
        state
    )


@app.delete("/states/{state_id}")
async def soft_delete_state(
    state_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.soft_delete_state(
        db,
        state_id
    )


@app.delete("/states/hard/{state_id}")
async def hard_delete_state(
    state_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.hard_delete_state(
        db,
        state_id
    )


# District

@app.post("/districts", response_model=DistrictResponse)
async def create_district(
    district: DistrictCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_district(db, district)


@app.get("/districts", response_model=list[DistrictResponse])
async def get_districts(
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_districts(db)

@app.put("/districts/{district_id}",
         response_model=DistrictResponse)
async def update_district(
    district_id: int,
    district: DistrictUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_district(
        db,
        district_id,
        district
    )


@app.delete("/districts/{district_id}")
async def soft_delete_district(
    district_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.soft_delete_district(
        db,
        district_id
    )


@app.delete("/districts/hard/{district_id}")
async def hard_delete_district(
    district_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.hard_delete_district(
        db,
        district_id
    )


# Village

@app.post("/villages", response_model=VillageResponse)
async def create_village(
    village: VillageCreate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.create_village(db, village)


@app.get("/villages", response_model=list[VillageResponse])
async def get_villages(
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_villages(db)

@app.put("/villages/{village_id}",
         response_model=VillageResponse)
async def update_village(
    village_id: int,
    village: VillageUpdate,
    db: AsyncSession = Depends(get_db)
):
    return await crud.update_village(
        db,
        village_id,
        village
    )


@app.delete("/villages/{village_id}")
async def soft_delete_village(
    village_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.soft_delete_village(
        db,
        village_id
    )


@app.delete("/villages/hard/{village_id}")
async def hard_delete_village(
    village_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.hard_delete_village(
        db,
        village_id
    )


#Village Hirarchy

@app.get("/villages/{village_id}",response_model=VillageHierarchyResponse)
async def get_village(
    village_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await crud.get_village_details(
        db,
        village_id
    )
