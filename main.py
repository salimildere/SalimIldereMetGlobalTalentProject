checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}


#def CalculateScore ():

def find_moves(checkers, dice1, dice2):
    locations = []
    score = {}

    # locations ile her pul değerinin konumu belirtilecek ve sonraki satırlarda kullanılacaktır.
    o = 1  # pul değerini temsil eder ve her döngüde bir artar
    for key, value in checkers.items():
        variable = value
        while variable > 0:
            locations.append(
                [o, key])  # locations dizisi içerisine ilk eleman pul numarası ikinci eleman ise konumudur.
            variable -= 1
            o += 1

    dice = [dice1, dice2, dice1]
    newlocations = []
    newlocation1 = newlocation2 = 0
    i = j = k = l = repeat = repeatNum = 0
    leng = len(locations)

    while l < 2:  # l ile hangi zarın seçileceği belirlenir
        while i < leng:
            newlocation1 = locations[i][1] + dice[l]  # seçilen pulun zar listindeki eleman ile yapılan hesaplama için
            while j < leng:
                if (locations[i][0] != locations[j][0]):
                    newlocation2 = locations[j][
                                       1] + dice[l + 1]
                    newlocations.append([locations[i][0], newlocation1,
                                         repeatNum])  # repeatNum listenin elemanlarının döngüsünü içerir. Skorlama aşamasında kullanılacaktır.
                    repeat += 1  # repeat location listesi uzunluğuna kadar 1 artarak devam edecek sonrasında ise repeatNum değerini 1 arttıracak
                    if (repeat == leng):
                        repeatNum += 1
                        repeat = 0
                    newlocations.append([locations[j][0], newlocation2, repeatNum])
                    repeat += 1
                    if (repeat == leng):
                        repeatNum += 1
                        repeat = 0
                    while k < leng:
                        if ((k != i) and (k != j) and (k != j)):
                            newlocations.append([locations[k][0], locations[k][1], repeatNum])
                            repeat += 1
                            if (repeat == leng):
                                repeatNum += 1
                                repeat = 0
                        k += 1
                    k = 0
                    newlocation2 = 0
                j += 1
            j = 0
            i += 1
            newlocation1 = 0
        l += 1

    lengNewLocations = len(newlocations)

    mainScore = pscore = k = door = l = m = h = oldloc1 = newloc1 = oldloc2 = newloc2 = z = sumLogControl = 0
    locationList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                    0, ]  # her pul kombinasyonundaki konum değerleri için kullanılacak liste
    locationCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0]  # 2 boyutlu dizi ilk elemanı konum, ikinci elemanı o konumda kaç taş bulunduğu
    locationScore = []
    log1 = []
    log2 = []
    newlocations2 = locations[:]

    #######################################################
    while l < leng:  # her kombinasyondaki taşların yerini alıyoruz
        object = locations[l]
        a = object[1]  # konum değeri alınıyor
        locationList[l] = a
        l += 1
    l = 0
    while l < leng:  # alınan taşların yerlerini sayarak locationCount dizimizi dolduruyoruz.
        loc = locationList[l]
        if (loc == 1):
            locationCount[1] += 1
        if (loc == 2):
            locationCount[2] += 1
        if (loc == 3):
            locationCount[3] += 1
        if (loc == 4):
            locationCount[4] += 1
        if (loc == 5):
            locationCount[5] += 1
        if (loc == 6):
            locationCount[6] += 1
        if (loc == 7):
            locationCount[7] += 1
        if (loc == 8):
            locationCount[8] += 1
        if (loc == 9):
            locationCount[9] += 1
        if (loc == 10):
            locationCount[10] += 1
        if (loc == 11):
            locationCount[11] += 1
        if (loc == 12):
            locationCount[12] += 1
        if (loc == 13):
            locationCount[13] += 1
        if (loc == 14):
            locationCount[14] += 1
        if (loc == 15):
            locationCount[15] += 1
        if (loc == 16):
            locationCount[16] += 1
        if (loc == 17):
            locationCount[17] += 1
        if (loc == 18):
            locationCount[18] += 1
        if (loc == 19):
            locationCount[19] += 1
        if (loc == 20):
            locationCount[20] += 1
        if (loc == 21):
            locationCount[21] += 1
        if (loc == 22):
            locationCount[22] += 1
        if (loc == 23):
            locationCount[23] += 1
        if (loc == 24):
            locationCount[24] += 1
        l += 1
    l = 0
    i = 1
    while i < 25:  # tavlanın numara değerleri üzerinde bulunan pul sayısına göre puanlama yapılmıştır
        if (locationCount[i] > 1):
            mainScore = mainScore + locationCount[i] - 1
            mainScore = mainScore + 1
            if (i == 5 or i == 6 or i == 7 or i == 8 or i == 17 or i == 18 or i == 19 or i == 20):
                mainScore = mainScore + 1
        i += 1
        #######################################################
        i = 0
        while i < 25:  # locationCount içeriğini temizliyoruz
            locationCount[i] = 0
            locationList[i] = 0
            i += 1
    while k < lengNewLocations:
        if (k > ((lengNewLocations / leng) - 1)):
            break
        p = leng * k
        z = p
        while l < leng:  # her kombinasyondaki taşların yerini alıyoruz
            if (z > lengNewLocations - 1):
                break
            object = newlocations[z]
            a = object[1]  # konum değeri alınıyor
            locationList[l] = a
            l += 1
            z += 1
        l = 0
        while l < leng:  # alınan taşların yerlerini sayarak locationCount dizimizi dolduruyoruz.
            loc = locationList[l]
            if (loc == 1):
                locationCount[1] += 1
            if (loc == 2):
                locationCount[2] += 1
            if (loc == 3):
                locationCount[3] += 1
            if (loc == 4):
                locationCount[4] += 1
            if (loc == 5):
                locationCount[5] += 1
            if (loc == 6):
                locationCount[6] += 1
            if (loc == 7):
                locationCount[7] += 1
            if (loc == 8):
                locationCount[8] += 1
            if (loc == 9):
                locationCount[9] += 1
            if (loc == 10):
                locationCount[10] += 1
            if (loc == 11):
                locationCount[11] += 1
            if (loc == 12):
                locationCount[12] += 1
            if (loc == 13):
                locationCount[13] += 1
            if (loc == 14):
                locationCount[14] += 1
            if (loc == 15):
                locationCount[15] += 1
            if (loc == 16):
                locationCount[16] += 1
            if (loc == 17):
                locationCount[17] += 1
            if (loc == 18):
                locationCount[18] += 1
            if (loc == 19):
                locationCount[19] += 1
            if (loc == 20):
                locationCount[20] += 1
            if (loc == 21):
                locationCount[21] += 1
            if (loc == 22):
                locationCount[22] += 1
            if (loc == 23):
                locationCount[23] += 1
            if (loc == 24):
                locationCount[24] += 1
            l += 1
        l = 0
        i = 1
        while i < 25:  # tavlanın numara değerleri üzerinde bulunan pul sayısına göre puanlama yapılmıştır
            if (locationCount[i] > 1):
                pscore = pscore + locationCount[i] - 1
                pscore = pscore + 1
                if (i == 5 or i == 6 or i == 7 or i == 8 or i == 17 or i == 18 or i == 19 or i == 20):
                    pscore = pscore + 1
            i += 1
        z = p
        m = 0
        while m < leng:  # İlk girdi olarak alanan konumlar ve yeni konumlar arasındaki farka bakılarak hangi pulların değiştiği bulunacak
            if (z > lengNewLocations - 1):
                break
            h = 0
            q = p
            while h < leng:
                if (q > (lengNewLocations - 1)):
                    break
                temp = newlocations[q]
                a = temp[0]
                b = temp[1]
                newlocations2[h] = [a, b]
                q += 1
                h += 1
            newlocations2 = sorted(newlocations2, key=lambda x: int(x[0]), reverse=False)
            locMain = locations[m]
            locNew = newlocations2[m]
            if (locMain[1] != locNew[1]):
                oldloc1 = locMain[1]
                newloc1 = locNew[1]
                log1.append([oldloc1, newloc1])
                n = m + 1
                y = z + 1
                while n < leng:
                    locMain = locations[n]
                    locNew = newlocations2[n]
                    if (locMain[1] != locNew[1]):
                        oldloc2 = locMain[1]
                        newloc2 = locNew[1]
                        log2.append([oldloc2, newloc2])
                        break
                    n += 1
                    y += 1
            if (len(log1) > k and len(log2) > k):
                break

            m += 1
            if (z > (lengNewLocations - 1)):
                break
        pscore = pscore - mainScore
        sumLog = [log1[k], log2[k], pscore]
        locationScore.append(sumLog)
        pscore = 0
        i = 0
        while i < 25:  # locationCount içeriğini temizliyoruz
            locationCount[i] = 0
            locationList[i] = 0
            i += 1

        k += 1
    locationScore = sorted(locationScore, key=lambda x: int(x[2]), reverse=True)
    i = 0
    finalScoreList = []
    while i < len(locationScore):
        temp = locationScore[i]
        if (temp[2] > 0):
            finalScoreList.append(temp)
        i += 1
    print(finalScoreList)

find_moves(checkers, 5, 3)
