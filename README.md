# ATM Simulator
CLI based app to simulate basic functions of an ATM machine. Initially this was created as a way for me to get comfortable with OOP principles, but has since been built out to include comprehensive unit testing and API calls.

## Setup instructions
1. Clone this repository by running the following in your command line:
```
git clone https://github.com/neji-s/atm.git
```

2. To run the app on mac:
```
python3 app.py
```
on windows run:
```
py app.py
```

3. To run the unit tests, you can either run the same command as above, replacing app.py for test_atm_stm.py as follows:
```
python3 test_atm_sim.py
```

or you can run the following command:
```
python3 -m unittest test_atm_sim.py
```

--Please note that the exchange rate feature may not run due to expired API key, but this will not stop the rest of the app from running--
