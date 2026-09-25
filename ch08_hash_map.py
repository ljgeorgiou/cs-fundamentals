import random

class KVPair[TKey, TValue]:
    def __init__(self, key: TKey, value: TValue) -> None:
        self.key = key
        self.value = value

class Bucket[TKey, TValue]:
    def __init__(self) -> None:
        self.bucket: list[KVPair[TKey, TValue]] = []

    def set(self, key: TKey, value: TValue) -> bool:
        for pair in self.bucket:
            if pair.key == key:
                pair.value = value
                return False
        self.bucket.append(KVPair(key, value))
        return True

    def delete(self, key: TKey) -> bool:
        for pair in self.bucket:
            if pair.key == key:
                self.bucket.remove(pair)
                return True
        raise KeyError(key)

    def get(self, key: TKey) -> TValue:
        for pair in self.bucket:
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def keys(self) -> list[TKey]:
        key_list: list[TKey] = []
        for pair in self.bucket:
            key_list.append(pair.key)
        return key_list

    def __contains__(self, key: TKey) -> bool:
        for pair in self.bucket:
            if pair.key == key:
                return True
        return False


class HashMap[TKey, TValue]:
    def __init__(self, capacity: int = 8) -> None:
        self.capacity = capacity
        self.buckets: list[Bucket[TKey, TValue]] = [Bucket() for _ in range(capacity)]
        self.size = 0

    def _index(self, key: TKey) -> int:
        return hash(key) % self.capacity

    def set(self, key: TKey, value: TValue) -> None:
        index: int = self._index(key)
        if self.buckets[index].set(key, value):
            self.size += 1

        if self.size / self.capacity > 0.75:
            self.capacity = self.capacity * 2
            new_list: list[Bucket[TKey, TValue]] = [Bucket() for _ in range(self.capacity)]
            for bucket in self.buckets:
                for pair in bucket.bucket:
                    new_idx: int = self._index(pair.key)
                    new_list[new_idx].set(pair.key, pair.value)
            self.buckets = new_list

    def get(self, key: TKey) -> TValue:
        index: int = self._index(key)
        return self.buckets[index].get(key)

    def delete(self, key: TKey) -> None:
        index: int = self._index(key)
        if self.buckets[index].delete(key):
            self.size -= 1
                
    def __len__(self) -> int:
        return self.size

    def keys(self) -> list[TKey]:
        key_list: list[TKey] = []
        for bucket in self.buckets:
            key_list.extend(bucket.keys())
        return key_list

    def __contains__(self, key: TKey) -> bool:
        index: int = self._index(key)
        return key in self.buckets[index]

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
print(m.size) #100