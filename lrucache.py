#!/usr/bin/python
import sys
from collections import deque

# LRU Cache per https://box.interviewstreet.com/challenges/dashboard/#problem/4f3c42a47d165
# Cache is a dict mapping keys to nodes.
# A node is a key and value pair.
# Nodes are stored in an access-ordered deque for O(1) inserts/deletes from both ends.
class LRU:
    cache = {}
    queue = deque()
    bound = 2
    
    def set(self, k, v):
        if k in self.cache:
            self.queue.remove(self.cache[k])
        node = {'key' : k, 'val' : v}
        self.cache[k] = node
        if len(self.queue) == self.bound:
            deleted = self.queue.popleft()['key']
            del self.cache[deleted]
        self.queue.append(node)
        
    def get(self, k):
        if k in self.cache:
            node = self.cache[k]
            self.queue.remove(node)
            self.queue.append(node)
            return node['val']
        else:
            return 'NULL'
    
    def peek(self, k):
        if k in self.cache:
            return self.cache[k]['val']
        else:
            return 'NULL'
    
    def setbound(self, n):
        self.bound = n
        while len(self.queue) > self.bound:
            deleted = self.queue.popleft()['key']
            del self.cache[deleted]
        
    def dump(self):
        for key in sorted(self.cache.iterkeys()):
            sys.stdout.write(key + ' ' + self.cache[key]['val'] + '\n')

lru = LRU()
count = int(sys.stdin.readline())
for line in sys.stdin:
    count = count - 1
    cmd = line.strip().split(' ', 2)
    if cmd[0] == 'BOUND':
        lru.setbound(int(cmd[1]))
    if cmd[0] == 'SET':
        lru.set(cmd[1], cmd[2])
    if cmd[0] == 'GET':
        sys.stdout.write(lru.get(cmd[1]) + '\n')
    if cmd[0] == 'PEEK':
        sys.stdout.write(lru.peek(cmd[1]) + '\n')
    if cmd[0] == 'DUMP':
        lru.dump()
    if count == 0:
        break
