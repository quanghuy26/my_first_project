try:
   fh = open("testfile.txt", "w")
   fh.write("Day la mot kiem tra nho ve xu ly ngoai le!!")
except IOError:
   print ("Error: Khong tim thay file")
else:
   print ("Thanh cong ghi noi dung vao file")
   fh.close()
