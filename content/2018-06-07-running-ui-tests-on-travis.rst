Running UI tests on Travis
##########################
:category: Quality Engineering
:tags: pytest pytest-selenium python
:status: published

Travis allows you to run `Chrome <https://docs.travis-ci.com/user/chrome>`_ and
`Firefox <https://docs.travis-ci.com/user/firefox>`_ on their build environment
and those can be used to run UI tests using Selenium.

Today we are going to see how to install `chromedriver` and `geckodriver` in
order to be able to run UI tests using `pytest-selenium
<https://pytest-selenium.readthedocs.io>`_. To run those tests you will need to
have your web application running so that Travis can access it and this article
won't cover that.

Assuming that you already have Travis setup for your project, the first step to
do is to enable the Chrome and Firefox addons. You can do that by adding the
following lines to your ``.travis.yml`` file:

.. code-block:: yaml

    addons:
      chrome: stable
      firefox: latest

Those lines will make Travis make available both Chrome and Firefox but that
won't install neither `chromedrive` and `geckodriver` which are required to run
Selenium webdriver. To make the process of setting up them, let's create some
scripts.

First create the ``setup_chromedriver.sh`` script:

.. code-block:: bash

    #!/bin/bash
    set -euvo pipefail

    export LATEST_CHROMEDRIVER="$(curl -s https://chromedriver.storage.googleapis.com/LATEST_RELEASE)"
    curl -L -s -o /tmp/chromedriver.zip "https://chromedriver.storage.googleapis.com/${LATEST_CHROMEDRIVER}/chromedriver_linux64.zip"
    mkdir "${HOME}/chromedriver"
    unzip /tmp/chromedriver.zip -d "${HOME}/chromedriver"

The script is checking for the latest `chromedriver` and downloading it. Next
it creates a diretory where the ``chromedriver`` executable will be placed. We
are creating a directory because later we will be adding that directory to the
``PATH``.

Next is time to create the ``setup_geckodriver.sh`` script:

.. code-block:: bash

    #!/bin/bash
    set -euvo pipefail

    curl -L -s -o geckodriverrelease https://api.github.com/repos/mozilla/geckodriver/releases/latest

    cat > parser.py <<EOF
    import sys, json
    r = json.load(sys.stdin)
    if 'assets' in r:
        print([a for a in r['assets'] if 'linux64' in a['name']][0]['browser_download_url']);
    else:
        print('https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz')
    EOF

    export GECKODRIVER_DOWNLOAD="$(cat geckodriverrelease | python parser.py)"
    curl -L -s -o /tmp/geckodriver.tar.gz "${GECKODRIVER_DOWNLOAD}"

    mkdir "${HOME}/geckodriver"
    tar xvf /tmp/geckodriver.tar.gz -C "${HOME}/geckodriver"

As you can see, to install the latest `geckodriver` it requires some extra
logic. See below a detailed explanation about why that is required.

`geckodriver` is hosted on Github and you can get the latest release
information using Github's API. The script is fetching that information by
doing an unauthenticated request. The problem with unauthenticated requests to
Github's API is that it limits, currently, to 60 requests per hour. Even though
your project's tests may run once a day you can hit that request limit because
the Travis environment is shared.

To avoid the hitting the request rate limit and to parse the information about
the latest limit the script is creating the ``parser.py`` Python script that
will fetch the URL for the latest release by parsing the JSON response (saved
on ``geckodriverrelease`` file by curl) or default to the current latest
release URL if the Github API's rate limite is hit.

After fetching the proper URL to download the latest `geckodriver` the script
go ahead and get it and place it on the created ``geckodriver`` directory. Same
as `chromedriver` this directory will be added later to the ``PATH``.

With all that in place, it is time to edit the ``.travis.yml`` file again and
make it run the UI tests. In the example we are going to see here, both setup
scripts were placed into a ``scripts`` directory on the projects repository's
root directory.

To make it more visually appealing on Travis let's run UI tests using `build
stages <https://docs.travis-ci.com/user/build-stages/>`_. Below are the
definitions for the jobs to run tests using both Chrome and Firefox on
separated jobs. The environment variable ``NAME`` is there just provide context
on Travis UI since you can't set jobs name as of now. On the ``before_install``
section of each job is where `chromedriver` and `geckodriver` are setup and the
executables are added to the ``PATH``. Finally the tests are running on the
``script`` section using ``xvfb-run`` which is required to run the browsers in
headless mode.

.. code-block:: yaml

    - stage: test-ui
      env:
        - NAME=ui-chrome
      before_install:
        - ./scripts/setup_chromedriver.sh
        - export PATH="${HOME}/chromedriver:${PATH}"
        - chromedriver --version
      install:
        - make run-web-app
      script:
        - xvfb-run py.test -v --driver Chrome path/to/ui/tests

    - stage: test-ui
      env:
        - NAME=ui-firefox
      before_install:
        - ./scripts/setup_geckodriver.sh
        - export PATH="${HOME}/geckodriver:${PATH}"
        - geckodriver --version
      install:
        - make run-web-app
      script:
        - xvfb-run py.test -v --driver Firefox path/to/ui/tests

After all that you should be able to run UI tests on Travis. If you want a full
``.travis.yml`` example you can check `integrade's .travis.yml
<https://github.com/cloudigrade/integrade/blob/master/.travis.yml>`_.
