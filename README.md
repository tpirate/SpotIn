[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://github.com/tpirate/SpotIn/)   [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/tpirate/SpotIn/blob/main/LICENSE)   [![Size](https://img.shields.io/github/languages/code-size/tpirate/SpotIn)](https://github.com/tpirate/SpotIn/)

# spotIn



Welcome to spotIn is a open source ubuntu spotify app. It detects which song you are listening to and opens it's lyrics in 
your local terminal.
----
> Disclaimer: There might be little bugs. Its on beta for now
----
# Prerequisites
* Python 3.8 or above
* Nothing else
----
# Setup
 
Enter the following lines to your terminal:
```sh
$ sudo git clone https://github.com/tpirate/SpotIn/
$ cd SpotIn
$ nano findsongname.py
```
Go to [here] and copy your oAuth.
```sh
...

5 import spotipy

6 # headers

7 headers={

8	 'Accept': 'application/json',

9	'Content-Type': 'application/json',

10	'Authorization': 'Bearer !!!paste your auth token here!!!' 

}

url="https://api.spotify.com/v1/me/player/currently-playing"
```
Paste your token to line 10.
Press 'ctrl + o' to save.
Press 'ctrl + x' to finish.
Run command:
```sh
$ python3 setup.py
```
Then you are good to go.
If you want to use it simply type 'spotin' to your terminal. It will detect what song you are listening to and show its lyrics!
------
# License
MIT License

Copyright (c) [2020] [SpotIn - Spotify Lyrics]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Made by [Can (tpirate) Galba]




[here]: <https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types=>
[Can (tpirate) Galba]: <https://twitter.com/lelpirate>
