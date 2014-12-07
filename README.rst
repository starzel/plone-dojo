Installation
============

Mac or Linux
------------

If you have python 2.7 installed on your system.

Make sure you have virtualenv installed:

..  code-block:: bash

    $ pip install -U virtualenv

Go to where you want to create the folder for the dojo.

..  code-block:: bash

    $ cd <whereever you want>

In that folder clone the buildout for the dojo:

..  code-block:: bash

    $ git clone https://github.com/starzel/plone-dojo.git buildout
    $ cd buildout
    $ virtualenv-2.7 py27
    $ ./py27/bin/pip install -U setuptools==6.1
    $ ./py27/bin/python bootstrap.py
    $ ./bin/buildout

This will take **a lot of time** and produce a lot of output because it downloads and configures Plone.


Windows
-------

Use `VirtualBox <https://www.virtualbox.org>`_ and `Vagrant <http://www.vagrantup.com>`_ to run Linux in a virtual machine.

See below for instructions.


No python installed
-------------------

Same as Windows: Use `VirtualBox <https://www.virtualbox.org>`_ and `Vagrant <http://www.vagrantup.com>`_. See below.



Installation with vagrant
=========================

**Use this option if you can't run Plone natively on your system because you either use Windows or do not have Python 2.7 installed.**

Install VirtualBox
------------------

Vagrant uses Oracle’s VirtualBox to create virtual environments. Here is a link directly to the download page: https://www.virtualbox.org/wiki/Downloads. We use VirtualBox  4.3.x.


Install and configure Vagrant
-----------------------------

Get the latest version from http://www.vagrantup.com/downloads for your operating system and install it.

.. note::

    In Windows there is a bug in the recent version of Vagrant. Here are the instruction how to work around the warning ``Vagrant could not detect VirtualBox! Make sure VirtualBox is properly installed``.

Now your system has a command ``vagrant`` that you can run in the terminal.

First create a directory where you want to do the training in.

.. code-block:: bash

    $ mkdir training
    $ cd training

Setup Vagrant to automatically install the current guest-additions. You can choose to skip this step if you encounter any problems with it.

.. code-block:: bash

    $ vagrant plugin install vagrant-vbguest

Now download the vagrant config for the dojo and unzip its contents into your training directory.

.. code-block:: bash

    $ wget http://www.starzel.de/vagrant.zip
    $ unzip vagrant.zip

The training-directory should now hold the file ``Vagrantfile`` and the directory ``manifests`` which again contains several files.

Now start setting up the VM that is configured in ``Vagrantfile``:

.. code-block:: bash

    $ vagrant up

This takes a **veeeeery loooong time** since it does all the following steps:

* downloads a virtual machine (Official Ubuntu Server 14.04 LTS, also called "Trusty Tahr")
* sets up the VM
* updates the VM
* installs various packages needed for Plone development
* downloads and unpack the unified installer for Plone
* runs the unified installer for Plone.
* copy the eggs to a location we use in the training
* clones the training-buildout into /vagrant/buildout
* builds Plone using the eggs from the buildout-cache

.. note::

    Sometimes this stops with the message *Skipping because of failed dependencies*.

    .. code-block:: bash

        Skipping because of failed dependencies

    If this happens or you have the feeling that something has gone wrong and the installation has not finished correctly for some reason you need to run try the following command to repeat the process. This will only repeat steps that have not finished correctly.

    .. code-block:: bash

        $ vagrant provision

    You can do this multiple times to fix problems, e.g. if your network-connection was down and steps could not finish because of this.

Once Vagrant finishes the provisioning-process, you can login to the now running virtual machine.

.. code-block:: bash

    $ vagrant ssh

.. note::

    If you use Windows you'll have to login with `putty <http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html>`_. Connect to vagrant@127.0.01 at port 2222. User **and** password are ``vagrant``.

You are now logged in as the user vagrant in ``/home/vagrant``. We'll do everything as this user.

Plone is now found in ``/vagrant/buildout/``. Start it in foreground with ``./bin/instance fg``.

.. code-block:: bash

    vagrant@training:~$ cd /vagrant/buildout
    vagrant@training:/vagrant/buildout$ ./bin/instance fg
    2014-05-20 16:56:54 INFO ZServer HTTP server started at Tue May 20 16:56:54 2014
            Hostname: 0.0.0.0
            Port: 8080
    2014-05-20 16:56:56 INFO Products.PloneFormGen gpg_subprocess initialized, using /usr/local/bin/gpg
    2014-05-20 16:57:02 INFO PloneFormGen Patching plone.app.portlets ColumnPortletManagerRenderer to not catch Retry exceptions
    2014-05-20 16:57:02 INFO Zope Ready to handle requests

Now the Zope-instance we're using is running. You can stop the running instance anytime using ``ctrl + c``.

If you point your local browser at http://localhost:8080 you see that Plone is running in vagrant. This works because Virtualbox forwards the port 8080 from the guest-system (the vagrant-Ubuntu) to the host-system (your normal operating-system). Now create a new Plone site by clicking "Create a new Plone site". The username and the password are both "admin" (Never do this on a real site!).

The buildout for this Plone is in a shared folder, this means we run it in the vagrant-box from ``/vagrant/buildout`` but we can also access it in out own operating-system and use our favorite editor. You will find the directory ``buildout`` in the directory ``training`` that you created in the very beginning next to ``Vagrantfile`` and ``manifests``.

.. note::

    The database and the python-packages are not accessible in you own system since large files cannot make use of symlinks in shared folders. The database lies in ``/home/vagrant/var``, the python-packages are in ``/home/vagrant/packages``.

If you have any problems or questions please mail me at bauer@starzel.de.


What Vagrant does
-----------------

Installation is done automatically by vagrant and puppet. If you want to know which steps are actually done please see http://plone-training.readthedocs.org/en/latest/plone_training_config/what_vagrant_does.html.

