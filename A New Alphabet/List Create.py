x = "@ 8 ( |) 3 # 6 [-] | _| |< 1 []\/[] []\[] 0 |D (,) |Z $ ‘][‘ |_| \/ \/\/ }{ ‘/ 2"
out = "["
for i in x.split(' '):
    out += "'{0}',".format(str(i))

out+="]"
print (out)
