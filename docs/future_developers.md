Notes for Future Developers
============================

## Testing

### Unit Tests
To run the unitesting suite run 
`python manage.py test`
from the directory `manage.py` is located. 

###Functional Tests
the functional/integration tests are powered by Selenium. You will need to have Selenium installed on your system, as well as the `chromedriver` for selenium downloaded and available in your path. 

once Selenium in installed you can find the tests in `../sitterson-tour/tour/tests/`. 
To run them execute:
```
python functional_tests.py
```

These tests will take much longer to run than unit tests, so should not be run as frequently. 

## Installation
See the README for development installation instructions.


## TODO:
This is a list of TODOs that we never quite got to. Future work on this project would do well to start by tackling some of the items on this list. 

* Upgrade to Django 1.8
