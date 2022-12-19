<p align="center">
    <br><b> INSTAW </b><br>
</p>
<p align="center"><a href="https://t.me/aruacksupport"><img src="https://telegra.ph/file/0a16484862e6bed471a49.jpg"></a></p>

> instaw 

<p align="center">
    <img src="https://img.shields.io/github/stars/aruack/instaw?style=for-the-badge" alt="Stars">
    <img src="https://img.shields.io/github/forks/aruack/instaw?style=for-the-badge" alt="Forks">
    <img src="https://img.shields.io/github/watchers/aruack/instaw?style=for-the-badge" alt="Watchers">
    <img src="https://img.shields.io/github/license/aruack/instaw?style=for-the-badge" alt="LICENSE">
    <img src="https://img.shields.io/github/commit-activity/w/aruack/instaw?style=for-the-badge" alt="Commit Activity">
    <a href="https://github.com/aruack/instaw/commits/aruack"> <img src="https://img.shields.io/github/last-commit/aruack/instaw?color=blue&logo=github&logoColor=green&style=for-the-badge" /></a>
    <img src="https://img.shields.io/github/contributors/aruack/instaw?style=for-the-badge" alt="Contributors">
    <a href="https://pypi.org/project/Pyrogram/"> <img src="https://img.shields.io/pypi/v/pyrogram?color=yellow&label=pyrogram&logo=python&logoColor=green&style=for-the-badge" /></a>
</p>

<h3>Requirements 📝</h3>

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7 or higher
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

# instagram-followers-bot

Functionality: 

- **Info**: Show report

- **Follow users**: from tag, from location, from a list or follow back who you do not follow back

- **Unfollow users**: who do not follow you back or all of them

---------------------

## Usage: 

```
apt install git
```

```
git clone https://github.com/aruack/instaw
```

**Show report (who follows, unfollows, follows you back):**
```
python main.py -u USERNAME -p PASSWORD -o info
```

**Follow users using the tag you introduce:**

```
python main.py -u USERNAME -p PASSWORD -o follow-tag -t TAG
```

**Follow users from a location:**

```
python main.py -u USERNAME -p PASSWORD -o follow-location -t LOCATION_ID
```

**Follow back all the users who you don't follow back:**
```
python main.py -u USERNAME -p PASSWORD -o super-followback
```

**Follow users from a list:**

```
python main.py -u USERNAME -p PASSWORD -o follow-list -t USER_LIST
```

**Unfollow all the users who don't follow you back:**
```
python main.py -u USERNAME -p PASSWORD -o super-unfollow
```
**NOTE**: Fill "whitelist.txt" file with the accounts you will never want to unfollow


**Unfollow all the users:**

```
python main.py -u USERNAME -p PASSWORD -o unfollow-all
```
**NOTE**: Fill "whitelist.txt" file with the accounts you will never want to unfollow

---------------------

## Examples:

*python main.py -u USERNAME -p PASSWORD -o follow-tag -t cat* : **Follow users using the tag 'cat'** 

*python main.py -u USERNAME -p PASSWORD -o follow-location -t 127963847* : **Follow users from Spain** 

*python main.py -u USERNAME -p PASSWORD -o super-followback*: **Now you are following users you didn't follow but they followed you**

*python main.py -u USERNAME -p PASSWORD -o follow-list -t userlist.txt* : **Follow users in each line of userlist.txt** 

*python main.py -u USERNAME -p PASSWORD -o super-unfollow*: **Now you are not following users who don't follow you**


---------------------


## Acknowledgment

The really good repo is the levpasha's one (https://github.com/LevPasha/Instagram-API-python) 

---------------------

## Note

Tested both in Python2.x (2.7.15rc1) and Python 3.x (3.6.7)



### Special Credits 💖
- [ARUACK](https://github.com/officalkumar): Developer

[![ForTheBadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

### Support & Developer 🎑
<a href="https://telegram.me/aruacksupport"><img src="https://img.shields.io/badge/Join-Support%20Group-blue.svg?style=for-the-badge&logo=Telegram"></a> <a href="https://telegram.me/aruackofficial"><img src="https://img.shields.io/badge/%20Developer-blue.svg?style=for-the-badge&logo=Telegram"></a>
