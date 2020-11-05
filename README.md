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
Run command:
```sh
$ python3 setup.py
```
Then you are good to go.
If you want to use it simply type 'spotin' to your terminal. It will detect what song you are listening to and show its lyrics!
------
# License
Free software. 
Made by [Can (tpirate) Galba]




[here]: <https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types=>
[Can (tpirate) Galba]: <https://twitter.com/lelpirate>
