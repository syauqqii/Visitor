## TUJUAN
  Untuk memanipulasi jumlah pengunjung pada badge visitor di halaman GitHub
penerapan dengan menggunakan python serta didasari dengan konsep multithreading
supaya dapat menghemat waktu (lebih efektif & efisien) meskipun memakan resources
yang tidak sedikit. (Pembuatnya gaada kerjaan jadinya buat program gajelas gini)

## INSTAL PROGRAM
#### Kita clone dulu repo ini ke local pc kita
```
git clone https://github.com/syauqqii/Visitor
```
#### Masuk ke folder Visitor
```
cd Visitor
```
#### Download beberapa library yang dibutuhkan
```
pip install requests / pip3 install requests
```

## PENGGUNAAN
#### Cara ke-1
```
python main.py --username {username_github} --iterasi {jumlah_iterasi}
```
```
python main.py -U {username_github} -I {jumlah_iterasi}
```
isi {username_github} dengan username github kalian
isi {jumlah_iterasi} sesuai kebutuhan kalian
  -> iterasi berarti berapa kali program dijalankan
  
#### Contoh ke-1
```
python main.py --username syauqqii --iterasi 15
```

<h1> </h1>

#### Cara ke-2
```
python main.py --username {username_github}
```
```
python main.py -U {username_github}
```
isi {username_github} dengan username github kalian

disini kita tidak mengisi argument jumlah_iterasi,
maka secara default iterasi akan di set ke 10

#### Contoh ke-2
```
python main.py --username syauqqii
```

<h1> </h1>

#### Cara ke-3 (beserta contoh penggunaan langsung)
```
python main.py
```
disini kita tidak mengisi argument apapun,
maka username di set dengan username pembuat 'syauqqii'
serta iterasi akan default di set ke 10

## PEMBUAT
Pake Nanya Lagi.. [Klik Sini](mailto:0xd1m5@gmail.com)
