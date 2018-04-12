======================
Docker Compose cleanup
======================


.. image:: https://img.shields.io/pypi/v/docker-compose-cleanup.svg
        :target: https://pypi.python.org/pypi/docker-compose-cleanup

.. image:: https://img.shields.io/travis/rivol/docker-compose-cleanup.svg
        :target: https://travis-ci.org/rivol/docker-compose-cleanup


Helps you cleanup Docker images of multiple Docker Compose projects.


* Free software: ISC license
* Documentation: https://docker-compose-cleanup.readthedocs.io.


Usage
-----

Install with

.. code-block:: console

    $ pip install docker-compose-cleanup

Once installed, just run

.. code-block:: console

    $ docker-compose-cleanup
    $ # Or, alternatively
    $ doco-cleanup

The script will print out commands to remove Docker images related to Docker Compose projects, grouped by projects,
e.g.:

.. code-block:: console

    Images without tags:
    docker image rm sha256:c8f20d0f9a sha256:462683af4d
    Project images:
    myproject
    docker image rm myproject_django:latest myproject_node:latest myproject_celery:latest
    pycharm
    docker image rm pycharm_helpers:PY-181.4203.547
    thtools
    docker image rm thtools_app:latest

You can then simply copy & paste to get rid of the specific projects.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
