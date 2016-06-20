Multiple Stories
==============================

Framework for the treatout MVVP March 2016


Design & Approach
-----------------

The system uses Flask, as it is lightweight, has minimal dependencies and few features that are superfluous in a small
project.  Werkzeug's SimpleCache is used to store data while using the application, since it is packaged with Flask and is
entirely suitable for short term storage of non-persistent data.  It would not be suitable for use in a production environment.

We have implemented a Sentence class, which stores sentence strings in explicit positional attributes, e.g:
    >>>sentence = Sentence(text="The quick brown fox jumped over the lazy dog")
    >>>sentence.centre``
    The quick brown fox jumped over the lazy dog
    >>>

It would be a relatively simple refactor to translate this into a database object if persistence were required.

Potential data structures & stores were considered and dismissed:

Global variable (dictionary, list, array) held in memory - classic python anti-pattern; more elegant solutions can achieve the same functionality
SQLlite backend with SQl-Alchemy- the obvious choice for a trial application that may be extended, as can be shifted over to Postgres or similar,
 initial prototype was done but was removed as overkill, given the lack of need for persistence, and desire to prototype swiftly.

Redis/Memcached caches - too heavyweight with non-trivial installations

Installation and Use
^^^^^^^^^^^^^^^^^^^^
Open this package, or clone from source at git@github.com:iamwithnail/testapp.git
Set up a virtualenv using
    virtualenv env
    source env/bin/activate
    pip install -r requirements.txt
    python run.py

You may need to alter file permissions on run.py; as default, they are allowed.
    chmod a+x run.py

Persistancy and Cache Expectations
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Per the original specification, the system does not persist beyond the immediate session; restarting the application
will result in data loss, and previous pages accessed at '/sentence/What's%20the%20story%20balamory?' will
throw a 500 error, if for example they are accessed through the back button or from history.


Test Intent
^^^^^^^^^^^
The technical test was intended to assess the ability to:
- make suitable tradeoffs on system complexity versus speed, while maintaining code quality.
- implement client specifications into a piece of functioning software
- write readable code
- write client-suitable technical documentation and supporting documents
- consider a range of technical solutions and implement one
- package and deliver a piece of functional software, rather than assessing standalone knowledge of CompSci concepts, which are often the focus of technical tests, but a less useful indicator of the ability to function in a team







