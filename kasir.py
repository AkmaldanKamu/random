print('|=====================|')
print('|    TOKO SEDERHANA   |')
print('|=====================|')

nama = input("Masukan Nama Barang : ")
harga = int(input('Masukan Harga Barang : '))
jumlah = int(input('Jumlah Barang yang dibeli : '))

total = harga * jumlah 
print("Total pembelian Rp.",total)

pembayaran = int(input("Masukan Pembayaran Anda : "))
kembalian = pembayaran - total
print("Kembalian Anda Rp.",kembalian)