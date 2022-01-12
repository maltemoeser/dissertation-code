import blocksci
from enum import Enum
from itertools import zip_longest

def blocksci_config():
    return "/home/ubuntu/btc.json"

def latest_clustering():
    return "/home/ubuntu/Data/clusters/20210715-base-clustering"

def latest_groundtruth():
    return "/home/ubuntu/Data/groundtruth/20210715-4-final"

def latest_smart_prediction():
    return "/home/ubuntu/Data/heuristics/20210709_smart_prediction.csv"

def latest_regular_prediction():
    return "/home/ubuntu/Data/heuristics/20210709_heuristics_prediction.csv"

def latest_fingerprints():
    return "/home/ubuntu/Data/fingerprints/20210715-fingerprints"

def latest_outputs():
    return None

def latest_standard_txes():
    return None

def remaining_txes():
    return "/home/ubuntu/Data/remaining/20210719-two-out"

def get_heuristics(fp):
    return {
        "optimal_change": blocksci.heuristics.change.optimal_change,
        "address_type": blocksci.heuristics.change.address_type,
        "power_of_ten_2": blocksci.heuristics.change.power_of_ten_value(2),
        "power_of_ten_3": blocksci.heuristics.change.power_of_ten_value(3),
        "power_of_ten_4": blocksci.heuristics.change.power_of_ten_value(4),
        "power_of_ten_5": blocksci.heuristics.change.power_of_ten_value(5),
        "power_of_ten_6": blocksci.heuristics.change.power_of_ten_value(6),
        "power_of_ten_7": blocksci.heuristics.change.power_of_ten_value(7),
        "output_count": blocksci.heuristics.change.smart_fingerprint(fp, get_fp_mask(Fingerprint.OUTPUT_COUNT)),
        "version": blocksci.heuristics.change.smart_fingerprint(fp, get_fp_mask(Fingerprint.VERSION_2)),
        "locktime": blocksci.heuristics.change.smart_fingerprint(fp, get_fp_mask([Fingerprint.LOCKTIME_HEIGHT, Fingerprint.LOCKTIME_TIME])),
        "rbf": blocksci.heuristics.change.smart_fingerprint(fp, get_fp_mask(Fingerprint.RBF)),
        "segwit": blocksci.heuristics.change.smart_fingerprint(fp, get_fp_mask(Fingerprint.SEGWIT)),
        "possible_segwit": blocksci.heuristics.change.smart_fingerprint(fp, get_fp_mask(Fingerprint.SEGWIT_COMPATIBLE)),
        "ordered_inouts": blocksci.heuristics.change.smart_fingerprint(fp, get_fp_mask(Fingerprint.SORTED_INOUTS)),
        "zeroconf": blocksci.heuristics.change.smart_fingerprint(fp, get_fp_mask(Fingerprint.ZEROCONF))
    }

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

LABELED_CLUSTERS = {
    "YoBit.net": "1JPeYXhrxkE4HdTZp4sfuV2P1DY7DApaJ4",
    "CoinPayments.net": "1MRZqY6api1xwu73PrTahauy7zvdcaQvWW",
    "AgoraMarket": "12iCRdr8ivxe9rPiB2AVzoJqMjGEefjzzg",
    "Cryptsy.com-old": "1EiRBMY9C8DU4VoneYuCQiUNwekx8af87M",
    "Cex.io": "1NoqH2V9pymNorDQxY8CBgAkrrWfes6zkC",
    "AlphaBayMarket": "13RXZ4xvX1QWBoj5gdtKne6m4ZhRRFvcck",
    "Cryptonator.com": "18f75mTzmQdwwP2q6edvd6kfzmQdw63Got",
    "SilkRoad2Market": "1Ma6ECZg5BGAr5hWzKLzWkHhF1kghXEcWR",
    "NitrogenSports.eu": "1PWs2vAHFWon1t3Nr4oRnFKSS5bAPqDVtY",
    "SilkRoadMarketplace": "1A2e6HRRd6yM9PKdp13uMVN15Uof4QnNUS",
    "BTC-e.com-old": "1ALaYRmZzXpthc7Ge9btjLWxx1zGYAAXht",
    "SatoshiMines.com": "1BBnGBN8Ee4TrnK9qpHFZEfHvmh1ReaZPH",
    "SecondsTrade.com": "1PDN3teoHEwGqpNZThzsaWPmkZKjCo9pX4",
    "999Dice.com": "1HM14r7MfUAWUAcmvtvsibPFV12q1HWTCZ",
    "FortuneJack.com": "13Rvk5viHLwpRjtn6DbkckGMCgeSVcYrJ7",
    "Cryptsy.com": "1CCCPHewU5mdfVczA3pdXHW6nAAfMy9Ckq",
    "Hashnest.com": "1MxCpDzMBJYD4k4fKnmgE72DSiq73uPxRK",
    "HolyTransaction.com": "1DtC1Bq7xatMn5nYo42JonsGmjEZU1WVW",
    "OKCoin.com-2": "15EJCP5mWUHjQmDAoUXg9nHAXizRCudF7U",
    "LocalBitcoins.com": "13CyHFw1c1FFYmwbuAAyfMcHNWEHmTvJtt",
    "Kraken.com-old": "1D5JsEtNZphR2yw8TMXRq9tijnxsAa4JWo",
    "Poloniex.com": "16KhuXHfMD1HxrCryFeumN9isZYVcrZSgz",
    "CoinKite.com": "154ExQxSYSgvmfSQAe7fUCHk4yfeyNBncK",
    "AbraxasMarket": "1L5mmgJZSyby3srSLxF9ZrY2HZCFUKuLrM",
    "Rollin.io": "1KxD8rLrnyfNXJHpsYzpnkXqTUp2TFsGGj",
    "PocketDice.io": "1N6yfANUbDXprxwCTcSP9ay8oUuSmiQtXA",
    "MaiCoin.com": "199VvLrw7AqC6YkFZamviA3n8G4eebpcX8",
    "BTCJam.com": "16XtEKcRX2P9wuByvGqys7TuwzmP7Ksfc3",
    "CoinGaming.io": "1LumtrVbTaAEqSSKQbMUP4epDgwutWv37V",
    "Bitfinex.com-old2": "1Ncc7Dfh2aNSd5MoxdJHpHT5RFYKpwhucb",
    "BitZino.com": "1CdFPEia6fHTuP8ypy4rzGX2ra3jgarEdQ",
    "Instawallet.org": "1J8h5NubFsX5pMUUYpUSgVjw5afPw6uVDa",
    "Cryptopay.me": "34yQWsbzdEa7kCACR7ce1dwiqxYNkVdG5P",
    "LuckyB.it": "1NxaBCFQwejSZbQfWcYNwgqML5wWoE3rK4",
    "Xapo.com": "34GwetF2RboHBW5ynw4u9rbrwkaM1DJPfP",
    "HaoBTC.com": "16SqcHSwC2MuD2g2NLRwAek3cUCzJHdCPG",
    "BetcoinDice.tm": "1Eih5CGNsVi1FB6MAerVLDKwzr8bUAv1eh",
    "BitZillions.com": "1Ef7DRzziJQEDRpcMxNWsYMkUmFgsiCpVF",
    "UpDown.BT": "13YMmxN8HP6rAMGqYAZiyRtjA58cu5CrKG",
    "SatoshiDice.com-original": "1dice9wVtrKZTBbAZqz1XiTmboYyvpD3t",
    "Bittrex.com": "1EoJACEcyswn1DjsMBrf2fH3JHyUZif5jM",
    "Huobi.com-2": "1MLrZdFp5L3bMgz94147dKyBugUQbGk8Q"
}

class Fingerprint(Enum):
    TWO_OUTPUTS = 1
    MORE_OUTPUTS = 2
    OUTPUT_COUNT = 3  # combined
    VERSION_2 = 4
    LOCKTIME_HEIGHT = 8
    LOCKTIME_TIME = 16
    RBF = 32
    SEGWIT = 64
    SEGWIT_COMPATIBLE = 128
    SORTED_INPUTS = 256
    SORTED_OUTPUTS = 512
    SORTED_INOUTS = 1024
    ZEROCONF = 2048
    P2PKH = 4096
    P2WPKH = 8192
    P2SH = 16384
    P2WSH = 32768
    MULTISIG = 65536
    ADDRESS_OTHER = 131072
    TWO_INPUTS = 262144
    MORE_INPUTS = 524288
    INPUT_COUNT = 786432  # combined


def get_fp_mask(flags):
    mask = 0
    if type(flags) == list:
        for flag in flags:
            mask |= flag.value
    elif isinstance(flags, Fingerprint):
        mask |= flags.value
    else:
        raise ValueError("Unsupported parameter type")
    return mask
