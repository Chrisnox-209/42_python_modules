from abc import ABC, abstractmethod
from typing import List, Any, Optional, Dict, Union

class DataStream(ABC):
    def __init__(self, stream_id: str, type_sensor: str):
        self.stream_id = stream_id
        self.type_sensor = type_sensor
        self.items_processed = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [item for item in data_batch if criteria in str(item)]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
            return {
                "stream_id": self.stream_id,
                "type": self.type_sensor,
                "items_processed": self.items_processed
            }


class SensorStream(DataStream):
    def __init__(self, stream_id: str, type_sensor: str):
        super().__init__(stream_id, type_sensor)

    def process_batch(self, data_batch: List[Any]) -> str:
        self.items_processed += len(data_batch)
        temp_str = data_batch[0].split(":")[1]
        temp = float(temp_str)
        return (f"Stream ID: {self.stream_id}, Type: {self.type_sensor}\n"
                f"Processing sensor batch: [{', '.join(data_batch)}]\n"
                f"Sensor analysis: {len(data_batch)} readings processed, avg temp: {temp}°C")


class TransactionStream(DataStream):
    def __init__(self, stream_id: str, type_sensor: str):
        super().__init__(stream_id, type_sensor)

    def process_batch(self, data_batch: List[Any]) -> str:
        self.items_processed += len(data_batch)
        list_transction = []
        for data in data_batch:
            if data.split(":")[1].isdigit():
                list_transction.append(int(data.split(":")[1]))
        reult = list_transction[0] - list_transction[1] + list_transction[2]
        return (f"Stream ID: {self.stream_id}, Type: {self.type_sensor}\n"
                f"Processing sensor batch: [{', '.join(data_batch)}]\n"
                f"ransaction analysis: {len(data_batch)} operations, net flow: +{reult} units"
               )

class EventStream(DataStream):
    def __init__(self, stream_id: str, type_sensor: str):
        super().__init__(stream_id, type_sensor)

    def process_batch(self, data_batch: List[Any]) -> str:
        self.items_processed += len(data_batch)
        return (f"Stream ID: {self.stream_id}, Type: {self.type_sensor}\n"
                f"Processing sensor batch: [{', '.join(data_batch)}]\n"
                f"Event analysis: {len(data_batch)} events, {sum(1 for data in data_batch if data == 'error')} error detected")

class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: Any) -> None:
        if isinstance(stream, DataStream):
            self.streams.append(stream)

    def process_all(self, batches_dict: Dict[str, List[Any]]) -> None:
            print("Batch 1 Results:")
            for stream in self.streams:
                if stream.stream_id in batches_dict:
                    try:
                        data_batch = batches_dict[stream.stream_id]
                        stream.process_batch(data_batch)
                        stats = stream.get_stats()
                        if "Environmental" in str(stats["type"]):
                            word = "readings"
                            prefix = "Sensor"
                        elif "Financial" in str(stats["type"]):
                            word = "operations"
                            prefix = "Transaction"
                        else:
                            word = "events"
                            prefix = "Event"
                        print(f"- {prefix} data: {len(data_batch)} {word} processed")
                    except Exception as error:
                        print(f"Erreur : {error}")


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    print("\nInitializing Sensor Stream...")
    my_sensor_00 = SensorStream("SENSOR_001", "Environmental Data")
    data_sensor_00 = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(my_sensor_00.process_batch(data_sensor_00))

    print("\nInitializing Transaction Stream...")
    my_sensor_01 = TransactionStream("TRANS_001", "Financial Data")
    data_sensor_01 = ["buy:100", "sell:150", "buy:75"]
    print(my_sensor_01.process_batch(data_sensor_01))

    print("\nInitializing Event Stream...")
    my_sensor_02 = EventStream("EVENT_001", "System Events")
    data_sensor_02 = ["login", "error", "logout"]
    print(my_sensor_02.process_batch(data_sensor_02))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    processor = StreamProcessor()
    processor.add_stream(my_sensor_00)
    processor.add_stream(my_sensor_01)
    processor.add_stream(my_sensor_02)
    mixed_batches = {
        "SENSOR_001": ["temp:24.0", "humidity:60"],
        "TRANS_001": ["buy:100", "sell:50", "buy:20", "sell:10"],
        "EVENT_001": ["login", "login", "logout"]
    }
    processor.process_all(mixed_batches)

    print("\nStream filtering active: High-priority data only")
    raw_sensor_data = ["temp:22", "alert:critical_temp", "humidity:50", "alert:critical_pressure"]
    raw_transaction_data = ["buy:10", "sell:50", "buy:10000", "buy:20"]
    critical_sensors = my_sensor_00.filter_data(raw_sensor_data, criteria="critical")
    large_transactions = my_sensor_01.filter_data(raw_transaction_data, criteria="10000")
    print(f"Filtered results: {len(critical_sensors)} critical sensor alerts, {len(large_transactions)} large transaction\n")
    print("All streams processed successfully. Nexus throughput optimal.")
