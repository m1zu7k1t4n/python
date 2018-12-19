# coding: utf-8
from flask import Flask, render_template, request, redirect, url_for
import numpy as np
from CPData import CardPack as cp


app = Flask(__name__)


# Main
class ELEMENT(object):
    def __init__(self):
        self._count = 0
        self._price = 0
        self._bronze = 0
        self._silver = 0
        self._gold = 0
        self._legend = 0

    def initialize(self):
        self._count = 0
        self._price = 0
        self._bronze = 0
        self._silver = 0
        self._gold = 0
        self._legend = 0

    def getcount(self):
        return self._count

    def setcount(self, count):
        self._count = count

    def getprice(self):
        return self._price

    def setprice(self, price):
        self._price = price

    def getbronze(self):
        return self._bronze

    def setbronze(self, bronze):
        self._bronze = bronze

    def getsilver(self):
        return self._silver

    def setsilver(self, silver):
        self._silver = silver

    def getgold(self):
        return self._gold

    def setgold(self, gold):
        self._gold = gold

    def getlegend(self):
        return self._legend

    def setlegend(self, legend):
        self._legend = legend

    count = property(getcount, setcount)
    price = property(getprice, setprice)
    bronze = property(getbronze, setbronze)
    silver = property(getsilver, setsilver)
    gold = property(getgold, setgold)
    legend = property(getlegend, setlegend)


standard = ELEMENT()
evolved = ELEMENT()
bahamut = ELEMENT()
pack_all = ELEMENT()


def pickup_cardpack(pack):
    weight_premium = [0.92, 0.08]
    pickup_card = np.random.choice(pack)
    premium_card = pickup_card + ' PREMIUM'
    choice_premium = [pickup_card, premium_card]
    pickup_premium = np.random.choice(choice_premium, p=weight_premium)
    return pickup_premium


def pickup_standard_rare():
    allrarity = ("bronze", "silver", "gold", "legend")
    nonbronze = ("silver", "gold", "legend")
    weight_all = [0.675, 0.25, 0.06, 0.015]
    weight_nonbronze = [0.925, 0.06, 0.015]
    result = []
    for v in range(7):
        pickup_rarity = np.random.choice(allrarity, p=weight_all)
        if "bronze" in pickup_rarity:
            result.append('Bron:' + pickup_cardpack(cp.standard_bronze))
            standard.bronze += 1
            pack_all.bronze += 1
        elif "silver" in pickup_rarity:
            result.append('Silv:' + pickup_cardpack(cp.standard_silver))
            standard.silver += 1
            pack_all.silver += 1
        elif "gold" in pickup_rarity:
            result.append('Gold:' + pickup_cardpack(cp.standard_gold))
            standard.gold += 1
            pack_all.gold += 1
        elif "legend" in pickup_rarity:
            result.append('Lege:' + pickup_cardpack(cp.standard_legend))
            standard.legend += 1
            pack_all.legend += 1
    for v in range(1):
        pickup_rarity = np.random.choice(nonbronze, p=weight_nonbronze)
        if "silver" in pickup_rarity:
            result.append('Silv:' + pickup_cardpack(cp.standard_silver))
            standard.silver += 1
            pack_all.silver += 1
        elif "gold" in pickup_rarity:
            result.append('Gold:' + pickup_cardpack(cp.standard_gold))
            standard.gold += 1
            pack_all.gold += 1
        elif "legend" in pickup_rarity:
            result.append('Lege:' + pickup_cardpack(cp.standard_legend))
            standard.legend += 1
            pack_all.legend += 1
    return result


def pickup_evolved_rare():
    allrarity = ("bronze", "silver", "gold", "legend")
    nonbronze = ("silver", "gold", "legend")
    weight_all = [0.675, 0.25, 0.06, 0.015]
    weight_nonbronze = [0.925, 0.06, 0.015]
    result = []
    for v in range(7):
        pickup_rarity = np.random.choice(allrarity, p=weight_all)
        if "bronze" in pickup_rarity:
            result.append(pickup_cardpack(cp.evolved_bronze))
            evolved.bronze += 1
            pack_all.bronze += 1
        elif "silver" in pickup_rarity:
            result.append(pickup_cardpack(cp.evolved_silver))
            evolved.silver += 1
            pack_all.silver += 1
        elif "gold" in pickup_rarity:
            result.append(pickup_cardpack(cp.evolved_gold))
            evolved.gold += 1
            pack_all.gold += 1
        elif "legend" in pickup_rarity:
            result.append(pickup_cardpack(cp.evolved_legend))
            evolved.legend += 1
            pack_all.legend += 1
    for v in range(1):
        pickup_rarity = np.random.choice(nonbronze, p=weight_nonbronze)
        if "silver" in pickup_rarity:
            result.append(pickup_cardpack(cp.evolved_silver))
            evolved.silver += 1
            pack_all.silver += 1
        elif "gold" in pickup_rarity:
            result.append(pickup_cardpack(cp.evolved_gold))
            evolved.gold += 1
            pack_all.gold += 1
        elif "legend" in pickup_rarity:
            result.append(pickup_cardpack(cp.evolved_legend))
            evolved.legend += 1
            pack_all.legend += 1
    return result


def pickup_bahamut_rare():
    allrarity = ("bronze", "silver", "gold", "legend")
    nonbronze = ("silver", "gold", "legend")
    weight_all = [0.675, 0.25, 0.06, 0.015]
    weight_nonbronze = [0.925, 0.06, 0.015]
    result = []
    for v in range(7):
        pickup_rarity = np.random.choice(allrarity, p=weight_all)
        if "bronze" in pickup_rarity:
            result.append(pickup_cardpack(cp.bahamut_bronze))
            bahamut.bronze += 1
            pack_all.bronze += 1
        elif "silver" in pickup_rarity:
            result.append(pickup_cardpack(cp.bahamut_silver))
            bahamut.silver += 1
            pack_all.silver += 1
        elif "gold" in pickup_rarity:
            result.append(pickup_cardpack(cp.bahamut_gold))
            bahamut.gold += 1
            pack_all.gold += 1
        elif "legend" in pickup_rarity:
            result.append(pickup_cardpack(cp.bahamut_legend))
            bahamut.legend += 1
            pack_all.legend += 1
    for v in range(1):
        pickup_rarity = np.random.choice(nonbronze, p=weight_nonbronze)
        if "silver" in pickup_rarity:
            result.append(pickup_cardpack(cp.bahamut_silver))
            bahamut.silver += 1
            pack_all.silver += 1
        elif "gold" in pickup_rarity:
            result.append(pickup_cardpack(cp.bahamut_gold))
            bahamut.gold += 1
            pack_all.gold += 1
        elif "legend" in pickup_rarity:
            result.append(pickup_cardpack(cp.bahamut_legend))
            bahamut.legend += 1
            pack_all.legend += 1
    return result


def buy_standard():
    standard.price += 240
    standard.count += 1
    pack_all.price += 240
    pack_all.count += 1
    return pickup_standard_rare()


def buy_evolved():
    evolved.price += 240
    evolved.count += 1
    pack_all.price += 240
    pack_all.count += 1
    return pickup_evolved_rare()


def buy_bahamut():
    bahamut.price += 240
    bahamut.count += 1
    pack_all.price += 240
    pack_all.count += 1
    return pickup_bahamut_rare()


def count_reset():
    standard.initialize()
    evolved.initialize()
    bahamut.initialize()
    pack_all.initialize()


# Routing
@app.route('/')
def index():
    title = "しゃどばがちゃしみゅ"
    message = "全3弾のパックをシミュレート！"
    return render_template('index.html', message=message, title=title)


@app.route('/post', methods=['POST', 'GET'])
def post():
    message = ""
    if request.method == 'POST':
        result = []
        if 'standard' in request.form:
            title = "しゃどばがちゃしみゅ"
            result = buy_standard()
        if 'evolved' in request.form:
            title = "しゃどばがちゃしみゅ"
            result = buy_evolved()
        if 'bahamut' in request.form:
            title = "しゃどばがちゃしみゅ"
            result = buy_bahamut()
        if 'reset' in request.form:
            title = "しゃどばがちゃしみゅ"
            count_reset()
            result = ""
            message = "ぜーんぶきえちゃったっ！"
        return render_template('index.html', result=result,
                                standard=standard, evolved=evolved,
                                bahamut=bahamut, pack_all=pack_all,
                                title=title, message=message)
    else:
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')