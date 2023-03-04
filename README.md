# Pytest-different-locales

Testing different locales with single testing solution

## Steps for trying this out

1. Create a local project using Virtualenv
2. Clone this repository using following command

```shell
git clone https://github.com/Lexxx42/Pytest-different-locales.git
```

3. Install [Python 3.11](https://www.python.org/downloads/) if you haven't already
4. Install [ChromeDriver](https://chromedriver.chromium.org/downloads)

+ Work tested for Chrome Version 110.0.5481.178 (Official Build) (64-bit)

5. Install [GeckoDriver](https://github.com/mozilla/geckodriver/releases/)

+ Work tested for Firefox Version 110.0 (64-bit)

6. Add drivers to the Environment Variables based on your OS settings

+ [Windows] [computerhope](https://www.computerhope.com/issues/ch000549.htm)

7. Install requirements using the following command

```shell
pip install -r requirements.txt
```

8. Run the following command to start the tests

```shell
pytest --language=es
```

9. You can change webdriver to firefox

```shell
pytest --language=es --browser_name=firefox
```

9. You can change language to

```python
['ru', 'en', 'fr', 'es']
```

```shell
pytest --language=fr
```
