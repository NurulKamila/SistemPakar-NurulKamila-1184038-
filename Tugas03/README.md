# SistemPakar-NurulKamila-1184038-

# Kali ini kita akan menggunakan Algoritma Naive Bayesian untuk mengklasifikasikan peluang terjadinya sesuatu berdasarkan data yang dimiliki sebelumnya.
Persoalan yang akan diklasifikasikan dengan Algoritma Naive Bayesian yaitu mengenai Penyakit kardiovaskular (CVD) 
Dataset yang digunakan yaitu heart_failure_clinical_records_dataset.csv yang didapatkan dari https://www.kaggle.com/andrewmvd/heart-failure-clinical-data
Data set ini memiliki 13 attrbute yaitu age, anaemia, creatinine_phosphokinase,diabetes, ejection_fraction , high_blood_pressure,platelets, serum_creatinine, serum_sodium, sex, smoking, DEATH_EVENT
Label yang digunakan adalah DEATH_EVENT yang dapat digunakan untuk memprediksi kematian akibat gagal jantung.
Hasil prediksi dari Algoritma Naive Bayesian ini akan menghasilkan bernilai 1 dan 0. Jika bernilai 1 maka mengakibatkan kematian ,namun jika bernilai 0 maka tidak mengakibatkan kematian.

# import pandas as pd
digunakan untuk mengimport library pandas

# import numpy as np
digunakan untuk mengimport library numpy

# kardiovaskular = pd.read_csv("heart_failure_clinical_records_dataset.csv")
digunakan untuk membaca data dari data set heart_failure_clinical_records_dataset.csv

# kardiovaskular.head()
digunakan digunakan untuk menampilkan data tertas pada dataset

# Variabel independen
x = kardiovaskular.drop(["DEATH_EVENT"], axis = 1)
digunakan untuk menghapus attribute DEATH_EVENT

# x.head()
menampilkan data dari variabel independen

# Variabel dependen
y = kardiovaskular["DEATH_EVENT"]
digunakan untuk mepresentasikan variabel dependen yaitu kardiovaskular yang digunakan untuk menunjukan apakah mengakibatkan kematian atau tidak

# y.head()
menampilkan data dari variabel y

# from sklearn.model_selection import train_test_split
mengimport library train_test split dari library sklearn,mode_selection

# x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 123)
digunakan untuk mempresetasikan variabel training dan testing

# from sklearn.naive_bayes import GaussianNB
Mengaktifkan/memanggil/membuat fungsi klasifikasi Naive Bayes

# modelnb = GaussianNB()
Memasukkan data training pada fungsi klasifikasi Naive Bayes

# nbtrain = modelnb.fit(x_train, y_train)
melakukan proses training

Menentukan hasil prediksi dari x_test
# y_pred = nbtrain.predict(x_test) 
mempresentasikan hasil dari prediksi y_pred 
# np.array(y_test)
mempresentasikan hasil aktualnya y_test

Menentukan probabilitas hasil prediksi
# nbtrain.predict_proba(x_test) 
# from sklearn.metrics import confusion_matrix
mengimport library confusion_matrix
# confusion_matrix(y_test, y_pred)
mempresentasikan confussiona_matrix dari t_test dan y_pred

Merapikan hasil confusion matrix
# y_actual = pd.Series([0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0], name = "actual") y_pred = pd.Series([1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0], name = "prediction") df_confusion = pd.crosstab(y_actual, y_pred)
mempresentasikan hasil prediksi dan aktual dalam berbentuk cross tab

# from sklearn.metrics import classification_report
mengimport library classification_report dari sklearn_metrics
# print(classification_report(y_actual, y_pred))
mencetak hasil dari prediksi

