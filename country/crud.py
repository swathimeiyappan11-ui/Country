from sqlalchemy import select
from sqlalchemy.orm import selectinload
from models import Country, State, District, Village
from fastapi import HTTPException


# Country

async def create_country(db, country):
    obj = Country(name=country.name)
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get_country(db):
    result = await db.execute(select(Country))
    return result.scalars().all()


async def update_country(db, country_id, country):
    result = await db.execute(
        select(Country).where(
            Country.id == country_id,
            Country.is_deleted == False
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    obj.name = country.name
    await db.commit()
    await db.refresh(obj)
    return obj


async def soft_delete_country(db, country_id):
    result = await db.execute(
        select(Country).where(
            Country.id == country_id,
            Country.is_deleted == False
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    obj.is_deleted = True
    await db.commit()
    return obj


async def hard_delete_country(db, country_id):
    result = await db.execute(
        select(Country).where(
            Country.id == country_id
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj

# State

async def create_state(db, state):
    obj = State(
        name=state.name,
        country_id=state.country_id
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get_states(db):
    result = await db.execute(select(State))
    return result.scalars().all()


async def update_state(db, state_id, state):
    result = await db.execute(
        select(State).where(
            State.id == state_id,
            State.is_deleted == False
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    obj.name = state.name
    obj.country_id = state.country_id
    await db.commit()
    await db.refresh(obj)
    return obj


async def soft_delete_state(db, state_id):
    result = await db.execute(
        select(State).where(
            State.id == state_id,
            State.is_deleted == False
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    obj.is_deleted = True
    await db.commit()
    return obj


async def hard_delete_state(db, state_id):
    result = await db.execute(
        select(State).where(State.id == state_id)
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


# District

async def create_district(db, district):
    obj = District(
        name=district.name,
        state_id=district.state_id
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get_districts(db):
    result = await db.execute(select(District))
    return result.scalars().all()


async def update_district(db, district_id, district):
    result = await db.execute(
        select(District).where(
            District.id == district_id,
            District.is_deleted == False
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    obj.name = district.name
    obj.state_id = district.state_id
    await db.commit()
    await db.refresh(obj)
    return obj


async def soft_delete_district(db, district_id):
    result = await db.execute(
        select(District).where(
            District.id == district_id,
            District.is_deleted == False
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    obj.is_deleted = True
    await db.commit()
    return obj


async def hard_delete_district(db, district_id):
    result = await db.execute(
        select(District).where(District.id == district_id)
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


# Village

async def create_village(db, village):
    obj = Village(
        name=village.name,
        district_id=village.district_id
    )
    db.add(obj)
    await db.commit()
    await db.refresh(obj)
    return obj


async def get_villages(db):
    result = await db.execute(select(Village))
    return result.scalars().all()


async def update_village(db, village_id, village):
    result = await db.execute(
        select(Village).where(
            Village.id == village_id,
            Village.is_deleted == False
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    obj.name = village.name
    obj.district_id = village.district_id
    await db.commit()
    await db.refresh(obj)
    return obj


async def soft_delete_village(db, village_id):
    result = await db.execute(
        select(Village).where(
            Village.id == village_id,
            Village.is_deleted == False
        )
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    obj.is_deleted = True
    await db.commit()
    return obj


async def hard_delete_village(db, village_id):
    result = await db.execute(
        select(Village).where(Village.id == village_id)
    )
    obj = result.scalar_one_or_none()
    if not obj:
        return None
    await db.delete(obj)
    await db.commit()
    return obj


#Village Hirarchy

async def get_village_details(db, village_id: int):
    result = await db.execute(
        select(Village)
        .options(
            selectinload(Village.district)
            .selectinload(District.state)
            .selectinload(State.country)
        )
        .where(Village.id == village_id)
    )
    village = result.scalar_one_or_none()
    if not village:
        raise HTTPException(status_code=404,detail="This village does not exist or has been deleted")
    else:
        return {
            "country": village.district.state.country.name,
            "state": village.district.state.name,
            "district": village.district.name,
            "village": village.name
        }
    
