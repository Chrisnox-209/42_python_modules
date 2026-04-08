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
    name: str = Field(min_length=2, max_length=50)
    rank: CrewRanks
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
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
            if (member.rank.value == "commander" or
               member.rank.value == "captain"):
                verif = True
        if verif is not True:
            raise ValueError("Mission must have at least one Commander "
                             "or Captain")
        return self

    @model_validator(mode='after')
    def check_experience(self) -> Self:
        total_experience: int = 0
        for member in self.crew:
            if member.years_experience >= 5:
                total_experience += 1
        ratio_experience: float = total_experience / len(self.crew)
        if self.duration_days > 365:
            if ratio_experience < 0.5:
                raise ValueError("The experience of the team"
                                 "members must be at least 50%")
        return self

    @model_validator(mode='after')
    def check_member(self) -> Self:
        cmp:  int = 0
        for member in self.crew:
            if member.is_active is not True:
                cmp += 1
        if cmp != 0:
            raise ValueError("All crew members must be active 'True'")
        return self


def main() -> None:
    print("Space Mission Crew Validation\n"
          "========================================")
    sarah = CrewMember(member_id="C001",
                       name="Sarah Connor",
                       rank=CrewRanks.COMMANDER,
                       age=22,
                       specialization="Mission Command",
                       years_experience=5,
                       is_active=True)

    john = CrewMember(member_id="L001",
                      name="John Smith",
                      rank=CrewRanks.LIEUTENANT,
                      age=31,
                      specialization="Navigation",
                      years_experience=8,
                      is_active=True)

    alice = CrewMember(member_id="O001",
                       name="Alice Johnson",
                       rank=CrewRanks.OFFICER,
                       age=56,
                       specialization="Engineering",
                       years_experience=30,
                       is_active=True)

    try:
        mission = SpaceMission(mission_id="M2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars",
                               launch_date=datetime.now(),
                               duration_days=900,
                               crew=[sarah, john, alice],
                               mission_status="planned",
                               budget_millions=2500.0)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")
        print("\n========================================")
    except ValidationError as error:
        print(f"Expected validation error:\n{error.errors()[0]['msg']}")

    try:
        mission = SpaceMission(mission_id="M2024_MARS",
                               mission_name="Mars Colony Establishment",
                               destination="Mars",
                               launch_date=datetime.now(),
                               duration_days=900,
                               crew=[john, alice],
                               mission_status="planned",
                               budget_millions=2500.0)
        print("Valid mission created:")
        print(f"Mission: {mission.mission_name}")
        print(f"ID: {mission.mission_id}")
        print(f"Destination: {mission.destination}")
        print(f"Duration: {mission.duration_days} days")
        print(f"Budget: ${mission.budget_millions}M")
        print(f"Crew size: {len(mission.crew)}")
        for member in mission.crew:
            print(f"- {member.name} ({member.rank.value}) "
                  f"- {member.specialization}")
        print("\n========================================")
    except ValidationError as error:
        print(f"Expected validation error:\n{error.errors()[0]['msg']}")


if __name__ == "__main__":
    main()
