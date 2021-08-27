*************
Meet The Stack
*************

A SMS app for collecting and presenting the topics for discussion during Sunday
Service. Because if it's Sunday, it's Meet The Stack.


Powered by `Django`_ and `Twilio`_.


.. image:: https://travis-ci.org/RobSpectre/meetthestack.com.svg?branch=master
    :target: https://travis-ci.org/RobSpectre/meetthestack.com

.. image:: https://codecov.io/gh/RobSpectre/meetthestack.com/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/RobSpectre/meetthestack.com


**Table of Contents**


.. contents::
    :local:
    :depth: 1
    :backlinks: none


Installation
===========

Install this `Django`_ application by first cloning the repository.

.. code-block:: bash
  
    git clone https://github.com/RobSpectre/meetthestack.com


Install the Python dependencies.

.. code-block:: bash

    cd meetthestack.com
    pip install -r requirements.txt


Create a local configuration file and customize with your settings.

.. code-block:: bash
   
    cd meetthestack.com/meetthestack
    cp local.sample local.py


Create database.

.. code-block:: bash

    cd ..
    python manage.py makemigrations
    python manage.py migrate

Run the server

.. code-block:: bash

    python manage.py runserver

Configure a `Twilio phone number`_ to point to the `/sms` endpoint of your host.


Text "HELP" to the number you configured.


Development
===========

Hacking
-----------


To hack on the project, fork the repo and then clone locally.

.. code-block:: bash

    $ git clone https://github.com/RobSpectre/meetthestack.com.git

Move to the project directory.

.. code-block:: bash

    $ cd meetthestack.com

Install the Python dependencies (preferably in a virtualenv).

.. code-block:: bash

    $ pip install -r requirements.txt 

Then customize your local variables to configure your `Twilio`_, email and
admin accounts you want to receive tips.

.. code-block:: bash

    $ cp meetthestack.com/meetthestack/local.sample meetthestack.com/meetthestack/local.py
    $ vim meetthestack.com/meetthestack/local.py

Move to the Django project root.

.. code-block:: bash

    $ cd meetthestack.com

Start the Django app.

.. code-block:: bash

    $ python manage.py runserver 


Testing
------------

Use Tox for easily running the test suite.

.. code-block:: bash

    $ tox


Meta
============

* Written by `Rob Spectre`_
* Released under `MIT License`_
* Software is as is - no warranty expressed or implied.


.. _Rob Spectre: http://www.brooklynhacker.com
.. _MIT License: http://opensource.org/licenses/MIT
.. _Django: https://www.djangoproject.com/
.. _Twilio: https://twilio.com
.. _Twilio phone number: https://www.twilio.com/console/phone-numbers/incoming
