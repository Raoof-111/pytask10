
"""Bir olimpiyadadır və burada iştirakçılar müxtəlif xallar qazanır. 
Biz isə onların topladığı xallara görə neçənci yeri tutduğunu print etməliyik. 
Misal üçün bizə xallar verilib. xallar = [5,3,4,2,1].
Tutduğu yerlər də qazandıqları xalların sırasına uyğun sıralanacaq. 
yerlər=['1-ci','3-cu','2-ci','4-cu','5-ci']
Sortdan istifadə etdikdə xalların sırası pozulacağı üçün yerlər də 
o pozulmuş sıraya uyğun sıralanacaq və nəticə  düzgün olmayacaq.
(taskı daha da asanlaşdırmaq üçün hərkəsin  xalı müxtəlif olacaq. Eyni xala sahib 2 şəxs olabilməz)
Verilmiş xallara uyğun tutduğu yerləri gətirən bir funksiya yazın.
    """






def winner(awards):
    aw_index = [(award, index) for index, award in enumerate(awards)]
    listed = sorted(aw_index, key=lambda x: x[0], reverse=True)
    place = [""] * len(awards)
    for yer, (award, index) in enumerate(listed, start=1):
        place[index] = f"{yer}-ci"
    return place
awards = [8, 3, 10, 2, 1]
result = winner(awards)
print(result)  