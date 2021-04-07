# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 10:17:04 2021

@author: Nurul Kamila (1184038)
"""
# Program Python3 untuk mencetak BFS traversal dari simpul sumber tertentu. BFS (int s)
from collections import defaultdict
 
# Kelas ini mewakili grafik berarah dan menggunakan representasi daftar kedekatan
class Graph:
 
    # Membuat
    def __init__(self):
 
        # kamus default untuk menyimpan grafik
        self.graph = defaultdict(list)
 
   # berfungsi untuk menambahkan tepi ke grafik
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    
     # Berfungsi untuk mencetak BFS grafik
    def BFS(self, s):
 
        # Tandai semua simpul sebagai tidak dikunjungi
        visited = [False] * (max(self.graph) + 1)
 
       # Membuat antrian untuk BFS
        queue = []
 
        # Tandai node sebagai sumber mengunjungi dan mengantrekannya
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Simpul dari antrian dan cetak
            s = queue.pop(0)
            print (s, end = " ")
 
            # Dapatkan semua simpul yang berdekatan dari simpul antrean s. 
            #Jika berbatasan belum dikunjungi, lalu tandai mengunjungi dan mengantrekannya
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
# Menjalankan kode
 
# Buat grafik yang diberikan
# diagram di atas
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 6)
g.addEdge(6, 0)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 0)
 
print ("Hasil dari Breadth First Traversal")
g.BFS(0)



