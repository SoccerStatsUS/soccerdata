

def get_contents(l):
    if not hasattr(l, 'contents'):
        s = l
    else:
        s = ""
        for e in l.contents:
            s += get_contents(e)
    return s.strip()
