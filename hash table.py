from linkedlist import TuplesLinkedList


class HashTable:
    def __init__(self, capacity=17):
        self.capacity = capacity
        self.buckets = [TuplesLinkedList() for i in range(capacity)]

    def hashcode(self, key):
        return hash(key) % self.capacity

    def get(self, key):
        pass

    def put(self, key, value):
        pass
