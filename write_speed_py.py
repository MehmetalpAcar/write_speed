import time
import datetime

print("3 saniye sonra metin giriniz.")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Simdi!")
time.sleep(0.2)
before = datetime.datetime.now()
text = input("Buraya yaziniz.")
after = datetime.datetime.now()
speed = after - before
seconds = round(speed.total_seconds(), 2)
letter_per_second = round(len(text) / seconds, 1)
print("Yazma hiziniz: {} saniye.".format(seconds))
print("{} Saniye basina karakter.".format(letter_per_second))
