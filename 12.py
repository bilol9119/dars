cen = int(input("YILNI KIRITNG: "))
if cen == 0:
    print(" 0 asr")
if cen % 100:
    print((cen // 100) + 1, "asr")
else :
    print(cen // 100, "asr")