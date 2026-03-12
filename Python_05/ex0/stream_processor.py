from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    def __init__(self, data: Any) -> None:
        self.data: Any = data

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        size: int = len(self.data)
        list_data: list[int] = self.data
        sum_data: int = sum(list_data)
        return (f"Processed {size} numeric values, "
                f"sum={sum_data}, avg={sum_data/size}")

    def validate(self, data: Any) -> bool:
        try:
            for nb in self.data:
                nb = int(nb)
            return True
        except ValueError as error:
            print(error)
            return False

    def format_output(self, result: str) -> str:
        self.result: str = result
        return super().format_output(result) + "\n"


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        letters: int = len(self.data)
        words: list[str] = self.data.split()
        nb_words: int = len(words)
        return (f"Processed text: {letters} characters, {nb_words} words")

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(self.data, str):
                raise TypeError
            return True
        except TypeError as error:
            print(error)
            return False

    def format_output(self, result: str) -> str:
        self.result: str = result
        return super().format_output(result) + "\n"


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        check: list[str] = self.data.split(":", 1)
        if check[0] == "ERROR":
            message: str = "[ALERT]"
        return (f"{message} ERROR level detected:{check[1]}")

    def validate(self, data: Any) -> bool:
        try:
            if type(self.data) is not str:
                raise TypeError
            return True
        except TypeError as error:
            print(error)
            return False

    def format_output(self, result: str) -> str:
        self.result: str = result
        return super().format_output(result) + "\n"


if __name__ == "__main__":
    print("=== CODE NEXUS- DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    tab_nb: list[int] = [1, 2, 3, 4, 5]
    obj_num = NumericProcessor(tab_nb)
    print(f"Processing data: {tab_nb}")
    try:
        if obj_num.validate(obj_num.data):
            print("Validation: Numeric data verified")
            result_num: str = obj_num.process(obj_num.data)
            print(obj_num.format_output(result_num))
    except Exception as error:
        print(error)

    print("Initializing Text Processor...")
    text: str = "Hello Nexus World"
    obj_text = TextProcessor(text)
    print(f'Processing data: "{text}"')
    try:
        if obj_text.validate(obj_text.data):
            print("Validation: Numeric data verified")
            result_text: str = obj_text.process(obj_text.data)
            print(obj_text.format_output(result_text))
    except Exception as error:
        print(error)

    print("Initializing Log Processor...")
    log: str = "ERROR: Connection timeout"
    obj_log = LogProcessor(log)
    print(f'Processing data: "{log}"')
    try:
        if obj_log.validate(obj_log.data):
            print("Validation: Log entry verified")
            result_log: str = obj_log.process(obj_log.data)
            print(obj_log.format_output(result_log))
    except Exception as error:
        print(error)

    print("=== Polymorphic Processing Demo ===")

    processors: List[DataProcessor] = [obj_num, obj_text, obj_log]

    for i, processor in enumerate(processors, start=1):
        print(f"Result {i}: {processor.process(processor.data)}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")
