import bottle, os
from beaker.middleware import SessionMiddleware

#I changed the file
#changed file through github

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = SessionMiddleware(bottle.app(), session_opts)

products = [{"pid": 1, "name": "Kandifloss"},
            {"pid": 2, "name": "Koko Mjolk"},
            {"pid": 3, "name": "Prins Polo"},
            {"pid": 4, "name": "Bounty"},
            {"pid": 5, "name": "Noa Kropp"}
            ]


@bottle.route('/')
def index():
    session = bottle.request.environ.get('beaker.session')
    session['teljari'] = session.get('teljari', 0) + 1
    session.save()
    return bottle.template("index.tpl", products=products, teljari=session['teljari'])


@bottle.route("/cart")
def cart():
    session = bottle.request.environ.get('beaker.session')
    info=""
    karfa=[]
    if session.get('1'):
        vara1 = session.get('1')
        karfa.append(vara1)
    if session.get('2'):
        vara2 = session.get('2')
        karfa.append(vara2)
    if session.get('3'):
        vara3 = session.get('3')
        karfa.append(vara3)
    if session.get('4'):
        vara4 = session.get('4')
        karfa.append(vara4)
    if session.get('5'):
        vara5 = session.get('5')
        karfa.append(vara5)
    if len(karfa) == 4:
        info="Karfan er full"
        pass

    if len(karfa) > 4:
        info="Karfan er full"
        del karfa[-1]
        pass

    # og svo framvegis
    return bottle.template("cart.tpl", karfa = karfa, info=info)


@bottle.route("/cart/add/<id:int>")

def add_to_cart(id):
    if id == 1:
        session = bottle.request.environ.get('beaker.session')
        session["1"] = "Kandifloss"
        session.save()  # vistum session
        return bottle.redirect("/cart")
    if id == 2:
        session = bottle.request.environ.get('beaker.session')
        session["2"] = "Koko Mjolk"
        session.save()  # vistum session
        return bottle.redirect("/cart")
    if id == 3:
        session = bottle.request.environ.get('beaker.session')
        session["3"] = "Prins Polo"
        session.save()  # vistum session
        return bottle.redirect("/cart")
    if id == 4:
        session = bottle.request.environ.get('beaker.session')
        session["4"] = "Bounty"
        session.save()  # vistum session
    if id == 5:
        session = bottle.request.environ.get('beaker.session')
        session["5"] = "Noa kropp"
        session.save()  # vistum session
    #og svo framvegis
    return bottle.redirect("/cart")

@bottle.route("/cart/remove")
def remove_from_cart():
    session = bottle.request.environ.get('beaker.session')
    session.delete()
    return bottle.redirect("/cart")

@bottle.route('/static/<skra>')
def static_skrar(skra):
    return bottle.static_file(skra, root='./public/')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    bottle.run(host='0.0.0.0', port=port)
