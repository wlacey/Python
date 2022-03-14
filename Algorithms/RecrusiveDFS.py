# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 00:37:45 2021

@author: wlacey
"""

def recrusive_dfs(graph, source, path = []):
    
    if source not in path:
        path.append(source)
        
        # backtrack
        if source not in graph:
            return path
        for neighbor in graph[source]:
            path = recrusive_dfs(graph, neighbor)
    
    return path

graph = {'A':['B','C'], 'B':['E']}

path = recrusive_dfs(graph,'A')

print(' '.join(path))
