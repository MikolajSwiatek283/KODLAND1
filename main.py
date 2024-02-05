meme_dict = {
            "CRINGE": "coś dziwnego lub wstydliwego",
            "LOL": "odpowiedź na coś zabawnego",
            "SHEESH": "lekka dezaprobata",
            "CREEPY": "straszny, złowieszczy",
            "AGGRO": "stać się agresywnym/zły"
            }
while True:
    word = input('Wpisz słowo, którego nie rozumiesz')
    if word in meme_dict.keys():
       print(meme_dict[word])
    else:
        print("Nie znaleziono tego słowa")
