from pydantic import BaseModel, Field, ValidationError, model_validator
from enum import Enum
from datetime import datetime
from typing import Self


class ContactType(str, Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def check_contact(self) -> Self:
        id: str = self.contact_id
        if id[:2] != "AC":
            raise ValueError("contact_id does not "
                             "start with 'AC'")
        return self

    @model_validator(mode='after')
    def check_physical(self) -> Self:
        if (self.contact_type == ContactType.PHYSICAL
           and not self.is_verified):
            raise ValueError("is_verified is not 'True'")
        if (self.contact_type == ContactType.TELEPATHIC
           and self.witness_count < 3):
            raise ValueError("witness_count is 3 or more")
        return self

    @model_validator(mode='after')
    def check_signal(self) -> Self:
        if (self.signal_strength > 7.0 and
           (self.message_received == "" or self.message_received is None)):
            raise ValueError("Telepathic contact requires at least 3 "
                             "witnesses")
        return self


def main() -> None:
    print("Alien Contact Log Validation\n"
          "========================================")
    try:
        alien = AlienContact(contact_id="AC_2024_001",
                             timestamp=datetime.now(),
                             location="Area 51, Nevada",
                             contact_type=ContactType.RADIO,
                             signal_strength=8.5,
                             duration_minutes=45,
                             witness_count=5,
                             message_received="Greetings from Zeta Reticuli",
                             is_verified=True)
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
        print("\n========================================")
    except ValidationError as error:
        print(f"Expected validation error:\n{error.errors()[0]['msg']}")

    try:
        alien = AlienContact(contact_id="AC_2024_001",
                             timestamp=datetime.now(),
                             location="Area 51, Nevada",
                             contact_type=ContactType.TELEPATHIC,
                             signal_strength=8.5,
                             duration_minutes=45,
                             witness_count=2,
                             message_received="Greetings from Zeta Reticuli",
                             is_verified=True)
        print("Valid contact report:")
        print(f"ID: {alien.contact_id}")
        print(f"Type: {alien.contact_type.value}")
        print(f"Location: {alien.location}")
        print(f"Signal: {alien.signal_strength}/10")
        print(f"Duration: {alien.duration_minutes} minutes")
        print(f"Witnesses: {alien.witness_count}")
        print(f"Message: '{alien.message_received}'")
        print("\n========================================")
    except ValidationError as error:
        print(f"Expected validation error:\n{error.errors()[0]['msg']}")


if __name__ == "__main__":
    main()
