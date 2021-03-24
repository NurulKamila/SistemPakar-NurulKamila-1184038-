# SistemPakar-NurulKamila-1184038-
# Depth-First Search
Depth-First Search adalah algoritma untuk melintasi atau mencari struktur data pohon atau grafik. Algoritme dimulai pada simpul akar dan mengeksplorasi sejauh mungkin di sepanjang cabang sebelum mundur. Merupakan salah satu algoritma yang digunakan untuk pencarian jalur. Caranya berawal dari node root atau akar bergerak untuk memeriksa dahulu semua anak atau turunan dari suatu cabang sebelum beralih ke cabang lain. Gambaran pada DFS_1184038 yang saya buat adalah berawal dari 0 ke 1, 0 ke 2, 1 ke 6, 6 ke 0, 1 ke 2, 2 ke 3, 3 ke 4, 4 ke 5, dan 5 ke 0. Pada DFS_1184038 ini, hasilnya seperti berikut :

Apabila dirun dari (0) maka hasilnya yaitu 0 1 6 2 3 4 5 
Apabila dirun dari (1) maka hasilnya yaitu 1 6 0 2 3 4 5
Apabila dirun dari (2) maka hasilnya yaitu 2 3 4 5 0 1 6
Apabila dirun dari (3) maka hasilnya yaitu 3 4 5 0 1 6 2
Apabila dirun dari (6) maka hasilnya yaitu 6 0 1 2 3 4 5
Apabila dirun dari (4) maka hasilnya yaitu 4 5 0 1 6 2 3


# Breadth-first search
Breadth-first search adalah algoritma untuk melintasi atau mencari struktur data pohon atau grafik. Ini dimulai di akar pohon, dan menjelajahi semua node tetangga pada kedalaman saat ini sebelum beralih ke node di tingkat kedalaman berikutnya. Merupakan salah satu algoritma yang digunakan untuk pencarian jalur. Bedanya, cara BFS ini mengecek per level bukan mengecek kedalaman tiap level. Gambaran pada BFS_1184038 ini saya buat sama dengan DFS_1184038. Pada BFS_1184038 hasilnya akan seperti berikut ini :

Apabila dirun dari (0) maka hasilnya yaitu 0 1 2 6 3 4 5
Apabila dirun dari (1) maka hasilnya yaitu 1 6 2 0 3 4 5
Apabila dirun dari (2) maka hasilnya yaitu 2 3 4 5 0 1 6
Apabila dirun dari (3) maka hasilnya yaitu 3 4 5 0 1 2 6
Apabila dirun dari (6) maka hasilnya yaitu 6 0 1 2 3 4 5
Apabila dirun dari (4) maka hasilnya yaitu 4 5 0 1 2 6 3