# Problem set - 3
# The final Problem set is to use the File I/O.
# you will create a file Me.txt and write some lines. At the end, you’ll have txt files look like this :
# Nama : Ceb
# NIM : 1211....
# Resolusi Saya di Tahun ini : ....

# Open the file in 'w' (write) mode
with open('Me.txt', 'w') as fxck:
    # Write lines to the file
    fxck.write("Nama : Aziz Kurniawan\n")
    fxck.write("NIM : 122140097\n")
    fxck.write("Resolusi Saya di Tahun ini : Punya pacar, Tidak membohongi diri sendiri, Rajin menabung, Lebih zen.\n")