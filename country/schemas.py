from pydantic import BaseModel 

class CountryCreate(BaseModel):
    name : str
    is_deleted : bool = False

class CountryUpdate(BaseModel):
    name : str
    is_deleted : bool = False

class CountryResponse(BaseModel):
    id : int
    name : str
    is_deleted : bool = False
    
    class Config:
        from_attributes = True

class StateCreate(BaseModel):
    name : str
    country_id : int
    is_deletedz : bool = False

class StateUpdate(BaseModel):
    name : str
    country_id : int
    is_deleted : bool = False

class StateResponse(BaseModel):
    id : int
    name : str
    country_id : int
    is_deletedz : bool = False

    class Config:
        from_attributes = True

class DistrictCreate(BaseModel):
    name : str
    state_id : int
    is_deleted : bool = False

class DistrictUpdate(BaseModel):
    name : str
    state_id : int
    is_deleted : bool = False

class DistrictResponse(BaseModel):
    id : int
    name : str
    state_id : int
    is_deleted : bool = False

    class Config:
        from_attributes = True

class VillageCreate(BaseModel):
    name : str
    district_id : int
    is_deleted : bool = False

class VillageUpdate(BaseModel):
    name : str
    district_id : int
    is_deleted : bool = False

class VillageResponse(BaseModel):
    id : int
    name : str
    district_id : int
    is_deleted : bool = False

    class Config:
        from_attributes = True


class VillageHierarchyResponse(BaseModel):
    country: str
    state: str
    district: str
    village: str

    class Config:
        from_attributes = True

