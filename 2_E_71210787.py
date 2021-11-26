def hurufTengah(kata):
    bagi=len(kata)//2

    if (len(kata)%2==0) and ((len(kata)/2)%2==0):
        return kata[(bagi)//2 : ((bagi)//2)*-1]
    elif (len(kata)%2==0) and ((len(kata)/2)%2!=0):
        return kata[((bagi)//2)+1 : (((bagi)//2)+1)*-1]
    else:
        return kata[(((bagi)+1)//2) : (((bagi)+1)//2)*-1]

kata=str(input("Masukkan kata : "))
print("Huruf tengah pada kata",kata,"adalah",hurufTengah(kata))