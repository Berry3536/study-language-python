import theater_module
theater_module.price(3)
theater_module.price_morning(3)
theater_module.price_soilder(3)

import theater_module as mv
mv.price(3)
mv.price_morning(3)
mv.price_soilder(3)

from theater_module import *
price(3)
price_morning(3)
price_soilder(3)

from theater_module import price, price_morning
price(3)
price_morning(3)
price_soilder(3)

from theater_module import price_soilder as ps
ps(3)