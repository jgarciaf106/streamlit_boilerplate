from py_scdb import Store


# enable stored across all app
store = Store(
            store_path="db", 
            max_keys=1000000, 
            redundant_blocks=1, 
            pool_capacity=10, 
            compaction_interval=1800,
            is_search_enabled=True,
        )