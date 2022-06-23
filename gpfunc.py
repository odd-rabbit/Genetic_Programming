import gplearn as gp
import talib
import bottleneck as bn


def ts_min(c):
    window = 24
    if window < len(c):
        return bn.move_max(c, window, 1)
    else:
        return bn.move_max(c, len(c), 1)


def ts_max(c):
    window = 24
    if window < len(c):
        return bn.move_max(c, window, 1)
    else:
        return bn.move_max(c, len(c), 1)


def ts_argmin(c):
    window = 24
    if window < len(c):
        return bn.move_argmin(c, window, 1)
    else:
        return bn.move_argmin(c, len(c), 1)


def ts_argmax(c):
    window = 24
    if window < len(c):
        return bn.move_argmax(c, window, 1)
    else:
        return bn.move_argmax(c, len(c), 1)


def ts_rank(c):
    window = 24
    if window < len(c):
        return bn.move_rank(c, window, 1)
    else:
        return bn.move_rank(c, len(c), 1)


def ts_sum(c):
    window = 24
    if window < len(c):
        return bn.move_sum(c, window, 1)
    else:
        return bn.move_sum(c, len(c), 1)


def ts_std(c):
    window = 24
    if window < len(c):
        return bn.move_std(c, window, 1)
    else:
        return bn.move_std(c, len(c), 1)


# w=24
# df['ts_min'] = bn.move_min(c, w)
# df['ts_max'] = bn.move_max(c, w)
# df['ts_argmin'] = bn.move_argmin(c, w)
# df['ts_argmax'] = bn.move_argmax(c, w)
# df['ts_rank'] = (bn.move_rank(c, w)+1)/2
# df['ts_sum'] = bn.move_sum(c, w)
# df['ts_std'] = bn.move_std(c, w)
# # df['ts_corr'] = bn.move_var(c, w)

# df['DEMA'] = talib.DEMA(c, w)
# df['KAMA'] = talib.KAMA(c, w)
# df['MA'] = talib.MA(c, w)
# df['MIDPOINT'] = talib.MIDPOINT(c, w)
# df['MIDPRICE'] = talib.MIDPRICE(h, l, w)
# df['AROONOSC'] = talib.AROONOSC(h, l, w)
# df['CCI'] = talib.CCI(h,l,c,w)
# df['ADX'] = talib.ADX(h,l,c,w)
# df['MFI'] = talib.MFI(h,l,c,v,w)
# df['NATR'] = talib.NATR(h,l,c,w)
# # df['BETA'] = BETA(X,Y,d)
# df['LINEARREG_ANGEL'] = talib.LINEARREG_ANGLE(c,w)
# df['LINEARREG_INTERCEPT'] = talib.LINEARREG_INTERCEPT(c,w)
# df['LINEARREG_SLOPE'] = talib.LINEARREG_SLOPE(c,w)
# df['HT_DCPHASE'] = talib.HT_DCPHASE(c)