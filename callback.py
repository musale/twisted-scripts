from twisted.internet.defer import Deferred


def callbacker(result):
    print result


def multiple_callbacks(d):
    d.addCallback(callback_a)
    d.addCallback(callback_b)
    d.addCallback(print_html)
    d.callback("slay!!")


def callback_a(result):
    return '<b>%s</b>' % (result,)


def callback_b(result):
    return '<i>%s</i>' % (result,)


def print_html(result):
    print result


if __name__ == '__main__':
    d = Deferred()
    multiple_callbacks(d)
