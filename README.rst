========
utaskweb
========

.. image:: https://travis-ci.org/wkentaro/utaskweb.svg
    :target: https://travis-ci.org/wkentaro/utaskweb

.. image:: https://badge.fury.io/py/utaskweb.svg
    :target: http://badge.fury.io/py/utaskweb

Utils for scraping and crawling Utask-web website and get announces from http://www.c.u-tokyo.ac.jp.

Installation
============

From pypi
---------
.. code-block:: sh

  pip install utaskweb

From source
-----------
.. code-block:: sh

  git clone https://github.com/wkentaro/utaskweb
  cd utaskweb
  python setup.py install


Usage
=====

.. code-block:: python

  >>> import utaskweb
  >>> for k, v in utaskweb.get_class_cancels()[1][0].items():
          print k,v
  ...
  updated 2015/3/25
  room 154教室
  period 2
  day 木
  date 4月9日
  teacher 相澤 隆
  subject ドイツ語二列

