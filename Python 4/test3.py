#Python 25:
#Python reading files:
workers_file = open("workers.txt","r")
print(workers_file.readable())#readable يرجعلك boolian value اذا كان ممكن نقرأها او لا
print(workers_file.read())#read يقرأ الملف ويطبعه
print(workers_file.readlines()[1])#readlines يقرأ الملف ويطبعه على طريقة الليست وممكن تحدد السطر اللي بدك تقرأه
workers_file.close()#close يجب اغلاق الملف بعد فتحه
# Mazenabosedo
# Abosedomazen
