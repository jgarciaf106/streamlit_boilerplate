import os
from py_scdb import Store


class EnhancedStore:
    def __init__(
        self,
        store_path: str = "db",
        max_keys: int = 1000000,
        redundant_blocks: int = 1,
        pool_capacity: int = 10,
        compaction_interval: int = 1800,
        is_search_enabled: bool = True,
    ) -> None:
        try:
            os.makedirs(store_path, exist_ok=True)
        except OSError:
            print(f"Error creating store directory: {store_path}")
            raise

        self.store: Store = Store(
            store_path=store_path,
            max_keys=max_keys,
            redundant_blocks=redundant_blocks,
            pool_capacity=pool_capacity,
            compaction_interval=compaction_interval,
            is_search_enabled=is_search_enabled,
        )

    def close(self) -> None:
        self.store.close()

    def get(self, key: str) -> bytes:
        return self.store.get(key)

    def set(self, key: str, value: bytes) -> None:
        self.store.set(key, value)

    def delete(self, key: str) -> None:
        self.store.delete(key)


# enable stored across all app
store: EnhancedStore = EnhancedStore()