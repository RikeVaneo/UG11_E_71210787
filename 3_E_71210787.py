def hitungKata(kalimat, cari_kata):
    hasil=kalimat.count(cari_kata)

    return hasil

def cekkata(kalimat, cari_kata):
    if kalimat.count(cari_kata)==0:
        hasil=kalimat+" "+cari_kata
        print("Kata",cari_kata,"tidak terdapat di dalam string\nString diubah menjadi :\n"+hasil)
    else:
        ganti=cari_kata.upper()
        hasil=kalimat.replace(cari_kata,ganti)
    
        print("Kata",cari_kata,"terdapat dalam string\nString diubah menjadi :\n"+hasil)

def ubahKata(kalimat,cari_kata):
    kata_pengganti=str(input("Masukkan kata pengganti : "))
    print("Anda akan mengubah kata",kata,"menjadi",kata_pengganti,"sebanyak 1x")
    pilih_ubah=str(input("Apakah anda ingin mengubah jumlah total penggantian kata? (yes/no) : "))
    if pilih_ubah=="no":
        hasil=kalimat.replace(cari_kata,kata_pengganti,1)
        print("String berhasil diubah menjadi:") 
        print(hasil)
    
    if pilih_ubah=="yes":
        jumlah=int(input("Masukkan jumlah total pengggantian : "))
        hasil=kalimat.replace(cari_kata,kata_pengganti,jumlah)
        print("String berhasil diubah menjadi:") 
        print(hasil)

print("=====Program Manipulasi String=====")
print("Pilihan menu :")
print("1. Hitung kata")
print("2. Cek kata")
print("3. Ubah kata")
pilih=int(input("Pilihan anda : "))
if pilih==1:
    masukan_kalimat=str(input("Masukkan sebuah kalimat/kata : "))
    kata=str(input("Masukkan kata yang ingin dihitung : "))

    print("Terdapat sebanyak",hitungKata(masukan_kalimat,kata),"kata",kata,"di dalam string")

if pilih==2:
    masukan_kalimat=str(input("Masukkan sebuah kalimat/kata : "))
    kata=str(input("Masukkan kata yang ingin di cek : "))
    cekkata(masukan_kalimat,kata)

if pilih==3:
    masukan_kalimat=str(input("Masukkan sebuah kalimat/kata : "))
    kata=str(input("Masukkan kata yang ingin di ubah : "))
    ubahKata(masukan_kalimat,kata)
