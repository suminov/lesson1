def get_summ(one, two, delimetr = '&'):
  summ = str(one) + delimetr + str(two)
  return summ


a = get_summ('Lern', 'Python')
print(a.upper())


def format_price(price):
  cost = 'Цена: {c} руб.'.format(c = int(price))
  return cost


b = format_price(56.24)
print(b)