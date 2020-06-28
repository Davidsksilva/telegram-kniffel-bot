<p align="left">
   <img src=".github/logo.svg" width="160"/>
</p>

# Telegram Kniffel Bot

> A telegram bot that lets users play kniffel dice game together.

A bot in development that uses this [Python Telegram API](https://github.com/python-telegram-bot/python-telegram-bot).

## Prerequisites

* You have an updated version of `python` installed.

## Getting Started

First you need to create a `constants.py` fily under the source folder containing your telegram bot token, or just replace it the imported variable in `main.py`. To generate a token, you will need to create a bot by talking to  @BotFather in telegram, its quick and easy, just follow his lead.

After that, to start the bot, just run the following command:

```bash
$ python ./src/main.py
```

If you run into the error `ImportError: cannot import name 'Type'`, try using python3 or downgrade yourtornado version with:

```bash
$ pip install tornado==5.1.1
```

## Acknowledgements

* Dice icon made by [Pixel perfect](https://www.flaticon.com/authors/pixel-perfect) from www.flaticon.com

## License

This project uses the following license: [MIT](https://github.com/Davidsksilva/drone-network-dashboard/blob/master/LICENSE.md).
