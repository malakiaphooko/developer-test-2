Developer Test
##############

We're going to use a few things that are probably a little bit unfamiliar to you
but you should be able to get it using the documentation.

So we're going to use a web framework called Flask:

http://flask.pocoo.org/docs/1.0/

To spin up the little test app you'll just run it as if it was a script:

.. code:: shell

  $ python app.py

And we're going to use an ORM called:

http://docs.peewee-orm.com/en/latest/

ORMs, simply put, are convenient data models that sit over the SQL data.

We'll use an SQLite database, and I've given you some very basic boilerplate to
work with.

I don't really care about how pretty everything looks, so don't bring out your
best CSS and HTML skills, but I do expect the design to look vaguely clean,
intuitive and useable.

We're build a simple currency conversion applet, user enters an amount, a
source currency and a target currency and you should convert it. Simple?

We'll take it a bit further and we'll expect the rate to be live, taken from an
API like:

https://free.currencyconverterapi.com/

And we'll be sane and use a Python library like Requests to query the data:

http://docs.python-requests.org/en/master/

So once you're getting live rates you should probably consider a few other
things: the rates on the currency converter API are updated every 60 minutes so
it doesn't make sense to send each and every request to the API, maybe we can
cache the rate? And as a side effect, some external service can't get an idea
of what sort of figures we deal with.
