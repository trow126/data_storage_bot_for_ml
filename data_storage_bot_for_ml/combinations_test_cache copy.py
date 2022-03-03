import pprint as pp
import time

features = sorted([
                        'ADX',
                        'ADXR',
                        'APO',
                        'AROON_aroondown',
                        'AROON_aroonup',
                        'AROONOSC',
                        'CCI',
                        'DX',
                        'MACD_macd',
                        'MACD_macdsignal',
                        'MACD_macdhist',
                        'MFI',
                        'MINUS_DI',
                        'MINUS_DM',
                        'MOM',
                        'PLUS_DI',
                        'PLUS_DM',
                        'RSI',
                        'STOCH_slowk',
                        'STOCH_slowd',
                        'STOCHF_fastk',
                        'STOCHRSI_fastd',
                        'ULTOSC',
                        # 'WILLR',
                        # 'ADOSC',
                        # 'NATR',
                        # 'HT_DCPERIOD',
                        # 'HT_DCPHASE',
                        # 'HT_PHASOR_inphase',
                        # 'HT_PHASOR_quadrature',
                        # 'HT_TRENDMODE',
                        # 'BETA',
                        # 'LINEARREG',
                        # 'LINEARREG_ANGLE',
                        # 'LINEARREG_INTERCEPT',
                        # 'LINEARREG_SLOPE',
                        # 'STDDEV',
                        # 'BBANDS_upperband',
                        # 'BBANDS_middleband',
                        # 'BBANDS_lowerband',
                        # 'DEMA',
                        # 'EMA',
                        # 'HT_TRENDLINE',
                        # 'KAMA',
                        # 'MA',
                        # 'MIDPOINT',
                        # 'T3',
                        # 'TEMA',
                        # 'TRIMA',
                        # 'WMA',
                    ])

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def combination(n, r):
    return factorial(n) / (factorial(n - r) * factorial(r))

n = 8
total = 0

# for r in range(1, n+1):
#     res = combination(n, r)
#     print("{n}C{r} = {res}".format(
#         n=n,
#         r=r,
#         res=res))
#     total += res

# print("合計:", total)
num_list = list(range(1, 9))


start = time.perf_counter()

cache = {}
def join(a):
    s = ""
    for b in a:
        s += str(b) + "_"
    return s

def nCr(s1, r):  # ただしmは、1 <= m <= len(s1) の範囲とする

    a = s1[0]  # 配列の最初の値を対象する
    # a と組み合わせられる値は aを以外の配列を対象とすれば良い
    s2 = s1[1:]  # => [2, 3, 4, 5]

    res = []
    if r == 1:  # 例外ケースとして処理
        for a in s1:
            res.append(a)
        return res

    elif r == 2:
        for b in s2:
            res.append([a, b])
    else:
        for bc in nCr(s2, r-1):
            # bc.insert(0, a)
            bc.append(a)
            res.append(bc)

    if len(s1) > r - 1:
        prefix = join(s2)
        key = "{prefix}{n}C{r}".format(prefix=prefix, n=len(s2), r=r)

        if cache.get(key) is None:
            cache[key] = nCr(s2, r)

        return res + cache[key]
    else:
        return []

for i in range(1, len(features)+1):
    # print(len(nCr(features, i)))
    nCr(features, i)


end = time.perf_counter()
print("実行時間:",end - start)