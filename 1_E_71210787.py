def pangkatAngka(bilangan,pangkat):
    hasil=bilangan**pangkat
    return hasil

def akarBilangan(bilangan,akar):
    hasil=(bilangan**(1/akar))
    return hasil

print ("Menu Program Yang Tersedia")
print ("1. pangkatkan angka")
print ("2. akarkan bilangan")
pilih=int(input("Masukkan pilihan yang diinginkan : "))
if pilih==1:
    print("Masukkan angka yang ingin di pangkatkan")
    bilangan= float(input("Angka : "))
    print("ingin memodifikasi pangkat? (yes/no)")
    ubah= str(input(":"))
    if ubah=="yes":
        pangkat=int(input("Masukkan nilai pangkat : "))
        print("Hasil dari",bilangan,"^",pangkat," = ",pangkatAngka(bilangan,pangkat))
    
    if ubah=="no":
        print("Hasil dari",bilangan,"^ 2"," = ",pangkatAngka(bilangan,2))
        
if pilih==2:
    print("Masukkan angka yang ingin di akar")
    bilangan= float(input("Angka : "))
    print("ingin memodifikasi akar? (yes/no)")
    ubah= str(input(":"))
    if ubah=="yes":
        akar=float(input("Masukkan nilai akar : "))
        print("Hasil akar pangkat",akar,"dari",bilangan," = ",akarBilangan(bilangan,akar))
    
    if ubah=="no":
        print("Hasil akar pangkat 2 dari",bilangan," = ",akarBilangan(bilangan,2))