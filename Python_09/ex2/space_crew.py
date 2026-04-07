from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Self


class CrewRanks(str, Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(in_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=False)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: str = Field(min_length=1, max_length=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default="planned")
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def check_id(self) -> Self:
        if self.mission_id[:1] != "M":
            raise ValueError("mission_id does not "
                             "start with 'M'")
        return self

    @model_validator(mode='after')
    def check_crew(self) -> Self:
        verif: bool = False
        for member in self.crew:
            if (member == CrewRanks.COMMANDER or
               member == CrewRanks.CAPTAIN):
                verif = True
        if verif is not True:
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")
        return self

    @model_validator(mode='after')
    def check_mission(self) -> Self:
        total_experience: int = 0
        for member, i in enumerate(self.crew):
            total_experience += member.years_experience
            ratio_experience: float = i / total_experience
        if self.duration_days > 365:
            if ratio_experience < 0.5:
                raise ValueError("The experience of the team"
                                 "members must be at least 50%")
        return self

    @classmethod
    @model_validator(mode='after')
    def check_member(self) -> type[Self]:
        cmp:  int = 0
        for member in self.crew:
            if member.is_active is not True:
                cmp += 1
        if cmp != 0:
            raise ValueError("All crew members must be active 'True'")
        return self

def main() -> None:
    sarah = CrewMember()
    
    
if __name__ == "__main__":
    