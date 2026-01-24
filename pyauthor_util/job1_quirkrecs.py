# XXX study WLC notes in Job
# XXX study UXLC changes in Job
# XXX review quirks-Daat-Miqra.txt
# XXX review quirks-BHQ.txt
#
# XXX use location estimator to sanity check lc-loc entries

from pyauthor_util.qr_z_wlc_dexi import RECORDS_Z_WLC_DEXI
from pyauthor_util.qr_0316_and_friends import (
    RECORD_0316,
    RECORD_0816,
    RECORD_1413,
    RECORD_1535,
    RECORD_2212,
    RECORD_3410,
)
from pyauthor_util.qr_2228 import RECORD_2228
from pyauthor_util.qr_3105 import RECORD_3105
from pyauthor_util.qr_3107 import RECORD_3107
from pyauthor_util.qr_3206 import RECORD_3206
from pyauthor_util.qr_3612 import RECORD_3612
from pyauthor_util.qr_4125 import RECORD_4125
from pyauthor_util.qr_2221_A import RECORD_2221_A
from pyauthor_util.qr_2221_B import RECORD_2221_B
from pyauthor_util.qr_2421 import RECORD_2421
from pyauthor_util.qr_2702 import RECORD_2702
from pyauthor_util.qr_2919 import RECORD_2919
from pyauthor_util.qr_3629 import RECORD_3629
from pyauthor_util.qr_3902 import RECORD_3902
from pyauthor_util.qr_3913 import RECORD_3913
from pyauthor_util.qr_2808 import RECORD_2808
from pyauthor_util.qr_2911 import RECORD_2911
from pyauthor_util.qr_3920 import RECORD_3920
from pyauthor_util.qr_1203 import RECORD_1203
from pyauthor_util.qr_1804_A import RECORD_1804_A
from pyauthor_util.qr_1804_B import RECORD_1804_B
from pyauthor_util.qr_1806 import RECORD_1806
from pyauthor_util.qr_1604 import RECORD_1604
from pyauthor_util.qr_2125 import RECORD_2125
from pyauthor_util.qr_0417 import RECORD_0417
from pyauthor_util.qr_0914 import RECORD_0914
from pyauthor_util.qr_0930 import RECORD_0930
from pyauthor_util.qr_0709 import RECORD_0709
from pyauthor_util.qr_0721 import RECORD_0721
from pyauthor_util.qr_0906 import RECORD_0906
from pyauthor_util.qr_0935 import RECORD_0935
from pyauthor_util.qr_1001 import RECORD_1001
from pyauthor_util.qr_1015 import RECORD_1015
from pyauthor_util.qr_1103 import RECORD_1103
from pyauthor_util.qr_1106 import RECORD_1106
from pyauthor_util.qr_1107 import RECORD_1107
from pyauthor_util.qr_1113 import RECORD_1113
from pyauthor_util.qr_1508 import RECORD_1508
from pyauthor_util.qr_1613 import RECORD_1613
from pyauthor_util.qr_1620 import RECORD_1620
from pyauthor_util.qr_1704 import RECORD_1704
from pyauthor_util.qr_1706 import RECORD_1706
from pyauthor_util.qr_1711 import RECORD_1711
from pyauthor_util.qr_1809 import RECORD_1809
from pyauthor_util.qr_2230_B import RECORD_2230_B
from pyauthor_util.qr_2416 import RECORD_2416
from pyauthor_util.qr_2614 import RECORD_2614
from pyauthor_util.qr_3133 import RECORD_3133
from pyauthor_util.qr_3312 import RECORD_3312
from pyauthor_util.qr_3419 import RECORD_3419
from pyauthor_util.qr_3706 import RECORD_3706
from pyauthor_util.qr_3812_B import RECORD_3812_B
from pyauthor_util.qr_3817 import RECORD_3817
from pyauthor_util.qr_3906 import RECORD_3906
from pyauthor_util.qr_4010 import RECORD_4010
from pyauthor_util.qr_4026 import RECORD_4026
from pyauthor_util.qr_4213 import RECORD_4213
from pyauthor_util.qr_0121 import RECORD_0121
from pyauthor_util.qr_0629 import RECORD_0629
from pyauthor_util.qr_0701 import RECORD_0701
from pyauthor_util.qr_0801 import RECORD_0801
from pyauthor_util.qr_0807 import RECORD_0807
from pyauthor_util.qr_1216 import RECORD_1216
from pyauthor_util.qr_1409 import RECORD_1409
from pyauthor_util.qr_1534 import RECORD_1534
from pyauthor_util.qr_1905 import RECORD_1905
from pyauthor_util.qr_1916 import RECORD_1916
from pyauthor_util.qr_2230_A import RECORD_2230_A
from pyauthor_util.qr_2826 import RECORD_2826
from pyauthor_util.qr_3330 import RECORD_3330
from pyauthor_util.qr_3812_A import RECORD_3812_A
from pyauthor_util.qr_0409 import RECORD_0409

QUIRKRECS = [
    *RECORDS_Z_WLC_DEXI,
    RECORD_0121,
    RECORD_0316,
    RECORD_0409,
    RECORD_0417,
    RECORD_0629,
    RECORD_0701,
    RECORD_0709,
    RECORD_0721,
    RECORD_0801,
    RECORD_0807,
    RECORD_0816,
    RECORD_0906,
    RECORD_0914,
    RECORD_0930,
    RECORD_0935,
    RECORD_1001,
    RECORD_1015,
    RECORD_1103,
    RECORD_1106,
    RECORD_1107,
    RECORD_1113,
    RECORD_1203,
    RECORD_1216,
    RECORD_1409,
    RECORD_1413,
    RECORD_1508,
    RECORD_1534,
    RECORD_1535,
    RECORD_1604,
    RECORD_1613,
    RECORD_1620,
    RECORD_1704,
    RECORD_1706,
    RECORD_1711,
    RECORD_1804_A,
    RECORD_1804_B,
    RECORD_1806,
    RECORD_1809,
    RECORD_1905,
    RECORD_1916,
    RECORD_2125,
    RECORD_2212,
    RECORD_2221_A,
    RECORD_2221_B,
    RECORD_2228,
    RECORD_2230_A,
    RECORD_2230_B,
    RECORD_2416,
    RECORD_2421,
    RECORD_2614,
    RECORD_2702,
    RECORD_2808,
    RECORD_2826,
    RECORD_2911,
    RECORD_2919,
    RECORD_3105,
    RECORD_3107,
    RECORD_3133,
    RECORD_3206,
    RECORD_3312,
    RECORD_3330,
    RECORD_3410,
    RECORD_3419,
    RECORD_3612,
    RECORD_3629,
    RECORD_3706,
    RECORD_3812_A,
    RECORD_3812_B,
    RECORD_3817,
    RECORD_3902,
    RECORD_3906,
    RECORD_3913,
    RECORD_3920,
    RECORD_4010,
    RECORD_4026,
    RECORD_4125,
    RECORD_4213,
]
