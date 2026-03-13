from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

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
        size: int = len(data)
        list_data: list[int] = data
        sum_data: int = sum(list_data)
        return (f"Processed {size} numeric values, "
                f"sum={sum_data}, avg={sum_data/size}")

    def validate(self, data: Any) -> bool:
        try:
            for nb in data:
                nb = int(nb)
            return True
        except ValueError as error:
            print(error)
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result) + "\n"


class TextProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        letters: int = len(data)
        words: list[str] = data.split()
        nb_words: int = len(words)
        return (f"Processed text: {letters} characters, {nb_words} words")

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, str):
                raise TypeError
            return True
        except TypeError as error:
            print(error)
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result) + "\n"


class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        check: list[str] = data.split(":", 1)
        if check[0] == "ERROR":
            return (f"[ALERT] ERROR level detected:{check[1]}")
        elif check[0] == "INFO":
            return (f"[INFO] INFO level detected:{check[1]}")
        raise ValueError

    def validate(self, data: Any) -> bool:
        try:
            if type(data) is not str:
                raise TypeError
            return True
        except TypeError as error:
            print(error)
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result) + "\n"


if __name__ == "__main__":
    print("=== CODE NEXUS- DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    tab_nb: list[int] = [1, 2, 3, 4, 5]
    obj_num = NumericProcessor()
    print(f"Processing data: {tab_nb}")
    try:
        if obj_num.validate(tab_nb):
            print("Validation: Numeric data verified")
            result_num: str = obj_num.process(tab_nb)
            print(obj_num.format_output(result_num))
    except Exception as error:
        print(error)

    print("Initializing Text Processor...")
    text: str = "Hello Nexus World"
    obj_text = TextProcessor()
    print(f'Processing data: "{text}"')
    try:
        if obj_text.validate(text):
            print("Validation: Numeric data verified")
            result_text: str = obj_text.process(text)
            print(obj_text.format_output(result_text))
    except Exception as error:
        print(error)

    print("Initializing Log Processor...")
    log: str = "ERROR: Connection timeout"
    obj_log = LogProcessor()
    print(f'Processing data: "{log}"')
    try:
        if obj_log.validate(log):
            print("Validation: Log entry verified")
            result_log: str = obj_log.process(log)
            print(obj_log.format_output(result_log))
    except Exception as error:
        print(error)

    print("=== Polymorphic Processing Demo ===")

    processors: List[DataProcessor] = [obj_num, obj_text, obj_log]
    data: list = [[2, 2, 2], 'Hello Word!z', 'INFO: System ready']
    i: int = 1
    for processor, info in zip(processors, data):
        result: str = processor.process(info)
        print(f"Result {i}: {processor.process(info)}")
        i += 1

    print("\nFoundation systems online. Nexus ready for advanced streams.")
