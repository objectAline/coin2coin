from coinmarketcap import Market
coincap = Market()


def get_ticker(currency='', limit=-1, convert='TWD'):
    _parms = {
        'currency': currency
    }
    if limit:
        _parms['limit'] = limit
    if convert:
        _parms['covnert'] = convert
    ret = coincap.ticker(**_parms)

    if len(ret) == 1:
        return ret[0]
    return ret
