def accum(s):
    return '-'.join([c.upper()+c.lower()*idx for idx,c in enumerate(s)])
