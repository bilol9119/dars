sec = int(input("Secund kiriting: "))
hour = sec // 3600
sec = sec % 3600
min = sec // 60
sec = sec - (min * 60)
print(hour, "hour(s) ", min, "minute(s) ", sec, "secund(s)")
