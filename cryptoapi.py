import requests
import request

question_answer = {
    "How to Set Up a Neo Wallet": f"{request.How_to_setup}",
    "How to Buy FLM Token": f"{request.How_to_buy_FLM_Token}",
    "How to Buy FLM Token on Binance": f"Will be Updated Soon",
    "How to Stake and Earn Token": f"Will be Updated Soon",
    "How to Swap Token": f"Will be Updated Soon",
    "Flamingo Advanced Trade": f"Will be Updated Soon",
    "Flamingo Lend": f"{request.Flamingo_Lend}",
    "Flamingo FUSD Pool Bonus": f"Will be Updated Soon",
    "Wrap & Unwrap": f"{request.wrap_Unwrap}",
    "How to Stake FLP-FLM-fCAKE LP Token": f"Will be Updated Soon",
    "How to Buy FLM Tokens on Gate.io": f"Will be Updated Soon",
    "WETH assets migration": f"Will be Updated Soon",
    "Flamincome": f"Will be Updated Soon",
    "Asset Type Guide": f"Will be Updated Soon"

}

hash_coin = {'0xf0151f528127558851b39c2cd8aa47da7418ab28': 'FLM',
             '0xa9603a59e21d29e37ac39cf1b5f5abf5006b22a3': 'FLUND',
             '0x340720c7107ef5721e44ed2ea8e314cce5c130fa': 'TIPS',
             '0xef4073a0f2b305a38ec4050e4d3d28bc40ea63f5': 'NEO',
             '0xd2a4cff31913016155e38e474a2c06d08be276cf': 'GAS',
             '0x48c40d4666f93408be1bef038b6722404d9a4c2a': 'bNEO',
             '0x1005d400bcc2a56b7352f09e273be3f9933a5fb1': 'FUSD',
             '0x8c07b4c9f5bc170a3922eac4f5bb7ef17b0acc8b': 'LRB',
             '0xa8c51aa0c177187aeed3db88bdfa908ccbc9b1a5': 'USDL',
             '0x2d4c6cf0417209a7eb410160344e224e74f87195': 'SOM',
             '0x88da18a5bca86ec8206d9b4960a7d0c4355a432f': 'CANDY',
             '0x322b5a366ca724801a1aa01e669b5f3d7f8c7f6f': 'DOGER',
             '0xa3291b66f70d4687fc0e41977d8acb0699f235ae': 'DOGEF',
             '0x9770f4d78a19d1a6fa94b472bcedffcc06b56c49': 'FDE',
             '0xcd48b160c1bbc9d74997b803b9a7ad50a4bef020': 'fUSDT',
             '0xc14b601252aa5dfa6166cf35fe5ccd2e35f3fdf5': 'fWETH',
             '0xd6abe115ecb75e1fa0b42f5e85934ce8c1ae2893': 'fWBTC',
             '8122bc2212ec971690a044b37a6f52a9349b702b': 'pONT',
             '0xeeccd60ed722111f8400434dac3ba42c14d8beb1': 'pWING',
             '0x9b049f1283515eef1d3f6ac610e1595ed25ca3e9': 'GM',
             '0xe65b462b90516012826f8a9c4c285d8c750e3a77': 'fCAKE',
             '0x78e1330db47634afdb5ea455302ba2d12b8d549f': 'SWTH',
             '0xb56f0fba45cc57a948b342186274dfd863996bb3': 'fBNB'}

tokenjson = {
    'FLM': {
        'symbol': "FLM",
        'decimals': 8,
        'hash': "0xf0151f528127558851b39c2cd8aa47da7418ab28",
    },
    'FLUND': {
        'symbol': "FLUND",
        'decimals': 8,
        'hash': "0xa9603a59e21d29e37ac39cf1b5f5abf5006b22a3",
    },
    'TIPS': {
        'symbol': "TIPS",
        'decimals': 8,
        'hash': "0x340720c7107ef5721e44ed2ea8e314cce5c130fa",
    },
    'NEO': {
        'symbol': "NEO",
        'decimals': 0,
        'hash': "0xef4073a0f2b305a38ec4050e4d3d28bc40ea63f5",
    },
    'GAS': {
        'symbol': "GAS",
        'decimals': 8,
        'hash': "0xd2a4cff31913016155e38e474a2c06d08be276cf",
    },
    'bNEO': {
        'symbol': "bNEO",
        'decimals': 8,
        'hash': "0x48c40d4666f93408be1bef038b6722404d9a4c2a",
    },
    'FUSD': {
        'symbol': "FUSD",
        'decimals': 8,
        'hash': "0x1005d400bcc2a56b7352f09e273be3f9933a5fb1",
    },
    'LRB': {
        'symbol': "LRB",
        'decimals': 8,
        'hash': "0x8c07b4c9f5bc170a3922eac4f5bb7ef17b0acc8b",
    },
    'USDL': {
        'symbol': "USDL",
        'decimals': 8,
        'hash': "0xa8c51aa0c177187aeed3db88bdfa908ccbc9b1a5",
    },
    'SOM': {
        'symbol': "SOM",
        'decimals': 8,
        'hash': "0x2d4c6cf0417209a7eb410160344e224e74f87195",
    },
    'CANDY': {
        'symbol': "CANDY",
        'decimals': 9,
        'hash': "0x88da18a5bca86ec8206d9b4960a7d0c4355a432f",
    },
    'DOGER': {
        'symbol': "DOGER",
        'decimals': 8,
        'hash': "0x322b5a366ca724801a1aa01e669b5f3d7f8c7f6f",
    },
    'DOGEF': {
        'symbol': "DOGEF",
        'decimals': 8,
        'hash': "0xa3291b66f70d4687fc0e41977d8acb0699f235ae",
    },
    'FDE': {
        'symbol': "FDE",
        'decimals': 8,
        'hash': "0x9770f4d78a19d1a6fa94b472bcedffcc06b56c49",
    },
    'fUSDT': {
        'symbol': "fUSDT",
        'decimals': 6,
        'hash': "0xcd48b160c1bbc9d74997b803b9a7ad50a4bef020",
    },
    'fWETH': {
        'symbol': "fWETH",
        'decimals': 18,
        'hash': "0xc14b601252aa5dfa6166cf35fe5ccd2e35f3fdf5",
    },
    'fWBTC': {
        'symbol': "fWBTC",
        'decimals': 8,
        'hash': "0xd6abe115ecb75e1fa0b42f5e85934ce8c1ae2893",
    },
    'pONT': {
        'symbol': "pONT",
        'decimals': 9,
        'hash': "8122bc2212ec971690a044b37a6f52a9349b702b",
    },
    'pWING': {
        'symbol': "pWING",
        'decimals': 9,
        'hash': "0xeeccd60ed722111f8400434dac3ba42c14d8beb1",
    },
    'GM': {
        'symbol': "GM",
        'decimals': 8,
        'hash': "0x9b049f1283515eef1d3f6ac610e1595ed25ca3e9",
    },
    'fCAKE': {
        'symbol': "fCAKE",
        'decimals': 18,
        'hash': "0xe65b462b90516012826f8a9c4c285d8c750e3a77",
    },
    'SWTH': {
        'symbol': "SWTH",
        'decimals': 8,
        'hash': "0x78e1330db47634afdb5ea455302ba2d12b8d549f",
    },
    'fBNB': {
        'symbol': "fBNB",
        'decimals': 18,
        'hash': "0xb56f0fba45cc57a948b342186274dfd863996bb3",
    }
}

coin_list = [hash_coin[i] for i in hash_coin]

real_wallet_balance = {}

coin_latestPrice = 'https://neo-api.b-cdn.net/flamingo/live-data/prices/latest'
flamingo_analytics = f'https://neo-api.b-cdn.net/flamingo/analystics/daily-latest/'
flamingo_liveData = f'https://neo-api.b-cdn.net/flamingo/live-data/transfter/history'
flamingo_totalsupply = 'https://neo-api.b-cdn.net/flamingo/analytics/flamingo/total-supply'

# live data price from timestamp


# Wallet Related Api
get_WalletHistory = 'https://neo-api.b-cdn.net/wallet/wallet/history/'
get_WalletHistoryLatest = 'https://neo-api.b-cdn.net/wallet/wallet/latest?neo_address='

# Transfers
get_latestTransfer = 'https://neo-api.b-cdn.net/wallet/transfer/latest?neo_address=NYAN6Nfd5rNWqJhqz6KxXBDJSv1DtMHU9G'


# question and answer functions

def get_answer(question):
    return question_answer[question]


# api related functions

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        return data


def getMarketdata(list):
    data = fetch_data('https://neo-api.b-cdn.net/flamingo/live-data/prices/latest')
    # coin_decimal = tokenjson[coin]['decimals']

    market_data = ''
    for i in data:
        for coin in list:
            if i['unwrappedSymbol'] == coin:
                symbol = coin
                price = i['usd_price']
                market_data += f'✅*{coin}*  :  💸*${round(price, 5)}* \n\n'

    # print(coinPrice)
    # print(market_data)
    return market_data


def getWalletDetails(address):
    wallet_balances = requests.get(f'https://neo-api.b-cdn.net/wallet/wallet/latest?neo_address={address}')
    wallet_balance = wallet_balances.json()
    wallet = wallet_balance['data'][0]['balances']

    # print(wallet)
    # print(wallet)
    return wallet


def getTotalTransactionCount(address):
    return


def getLatestTransactionHistory(address, page=1):
    return


def info():
    return


def getTotalCoins():
    return [hash_coin[i] for i in hash_coin]


def getPercentageRise(coin):
    return


def group(list):
    array = []
    if len(list) % 3 != 0:

        array += [[list[i], list[(i + 1)], list[(i + 2)]] for i in range(0, len(list) - (len(list) // 3), 3)]
        if len(list) % 3 == 1:
            array += [[list[len(list) - 1]]]
        elif len(list) % 3 == 2:
            array += [[list[len(list) - 1], list[len(list) - 2]]]

    else:
        array += [[list[i], list[i + 1], list[i + 2]] for i in range(0, len(list), 3)]

    # print(array)
    return array


def getPrice(args):
    data = fetch_data('https://neo-api.b-cdn.net/flamingo/live-data/prices/latest')
    hashprice = {}
    for i in args:
        print(i)
        for j in data:
            if i == j['hash']:
                hashprice[i] = j['usd_price']

    return hashprice


def getFlamingoMarketCap():
    coin = 'FLM'
    latestPrice = fetch_data(coin_latestPrice)
    total_supply = fetch_data(flamingo_totalsupply)
    price = [i['usd_price'] for i in latestPrice if i['unwrappedSymbol'] == coin]
    market_cap = round(int(price[0] * total_supply) / 1000000, 1)
    print(f'{market_cap}M')
    return f'{market_cap}M'


def calculateWallet(address):
    wallet_converted = {}
    wallet = getWalletDetails(address)
    for i in wallet:
        for j in tokenjson:
            if i == tokenjson[j]['hash']:
                x = tokenjson[j]['decimals'] * '0'
                decimal = f'1{x}'
                wallet_converted[f'{i}'] = int(wallet[i]) / int(decimal)

    # print(wallet_converted)
    return wallet_converted


def getLatestCoinPrice(coin):
    data = fetch_data('https://neo-api.b-cdn.net/flamingo/live-data/prices/latest')
    coin_decimal = tokenjson[coin]['decimals']

    coinPrice = ''
    for i in data:
        if i['unwrappedSymbol'] == coin:
            symbol = coin
            price = i['usd_price']
            coinPrice = f'{coin} : ${round(price, 5)}'

    # print(coinPrice)
    return coinPrice


def calculateWalletBalance(address):
    details = calculateWallet(address)
    price = getPrice([i for i in details])
    TotalWalletBalance = 0;

    for i in details:
        TotalWalletBalance += round(details[i] * price[i], 4)

    print(TotalWalletBalance)
    return round(TotalWalletBalance, 3)


def getWalletCoinBalance(address):
    details = calculateWallet(address)
    prices = getPrice([i for i in details])
    coin_balances = ''
    for i in details:
        balance = round(details[i] * prices[i], 3)
        coin_balances += f'💸*{hash_coin[i]}* : {details[i]} : 💵${balance} \n\n'
    # print(coin_balances)
    return coin_balances


if __name__ == "__main__":
    pass
