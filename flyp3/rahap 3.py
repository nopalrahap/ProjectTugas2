umur = int(input('masukan umur:'))

if umur >= 65:
    print('usia pensiun')
elif umur >= 25:
    print('usia produktif')
elif umur >= 15:
    print('usia remaja')
elif umur >= 1:
    print('usia anak anak')
else:
    print('kondisi salah')