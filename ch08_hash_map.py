from dataclasses import dataclass
import random

@dataclass
class KVPair[TKey, TValue]:
    key: TKey
    value: TValue

class HashMap[TKey, TValue]:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.buckets: list[list[KVPair[TKey, TValue]]] = [[] for _ in range(capacity)]
        self.size = 0

    def __contains__(self, key: TKey) -> bool:
        index: int = self._index(key)
        for pair in self.buckets[index]:
            if pair.key == key:
                return True
        return False

    def __len__(self):
        return self.size

    def _index(self, key: TKey) -> int:
        return hash(key) % self.capacity

    def set(self, key: TKey, value: TValue) -> None:
        index: int = self._index(key)
        for pair in self.buckets[index]:
            if pair.key == key:
                pair.value = value
                return
        self.buckets[index].append(KVPair(key, value))
        self.size += 1

        if (self.size / self.capacity) > 0.75:
            self.capacity = self.capacity * 2
            new_list: list[list[KVPair[TKey, TValue]]] = [[] for _ in range(self.capacity)]
            for bucket in self.buckets:
                for pair in bucket:
                    new_idx = self._index(pair.key)
                    new_list[new_idx].append(pair)
            self.buckets = new_list


    def get(self, key: TKey) -> TValue:
        index = self._index(key)
        for pair in self.buckets[index]:
            if key == pair.key:
                return pair.value
        raise KeyError(key)

    def delete(self, key: TKey) -> None:
        index = self._index(key)
        for pair in self.buckets[index]:
            if pair.key == key:
                self.buckets[index].remove(pair)
                self.size = self.size - 1
                return
        raise KeyError(key)

    def keys(self) -> list[TKey]:
        key_list: list[TKey] = []
        for bucket in self.buckets:
            for pair in bucket:
                key_list.append(pair.key)
        return key_list

list_of_subjects: list[str] = ["math", "science", "computer science", "art", "history", "georgraphy", "design technology", "psychology"]

m: HashMap[str, str] = HashMap(8)

N_CASES = 100

test_cases = [
    (
        str(i),
        list_of_subjects[random.randint(0, len(list_of_subjects) - 1)],
    ) 
    for i in range(N_CASES)
]

for k, v in test_cases:
    m.set(k, v)

correct = 0
for k, v in test_cases:
    retrieved = m.get(k)
    correct += int(retrieved == v)

print(f"Accuracy: {correct}/{N_CASES}")