# kali

## kali hangul

```text
apt-get install fonts-nanum*
```

## install google chrome

```text
apt-get update
apt-get install gdebi
gdebi google-chrome-stable_current_amd64.deb
google-chrome
```

```text
apt-get update
dpkg -i google-chrome-stable_current_amb64.deb
apt-get --fix-broken install 
dpkg -i google-chrome-stable_current_amb64.deb
google-chrome
```

```text
google-chrome --no-sandbox 
vi /usr/bin/google-chrome
```

```text
exec -a "$0" "$HERE/chrome" "$0" --no-sandbox --user-data-dir
```

```text
apt-get install browser-plugin-freshplayer-pepperflash
```

## 한글

```text
apt-get install fcitx-lib*
apt-get install fcitx-hangul
apt-get install fonts-nanum
apt-get install fonts-nanum*
im-config
# ok -> yes -> fcitx -> ok 
fcitx-configtool
# InputMethod left-bottom click + button
# only show current language check 
# global config setting key 
reboot
```

## kakaotalk

```text
apt-get isntall wine wine32
```

## sshd

