# Jaspcan-dll

Simple python/bash script to get your favourite mangas from japscan.cc
> Created by fadeos and sam5558


## How to use it

Just download the git projet.
run this command for the dependencies : 
``` pip -r install dependencies```

and run the following command to download your manga :

```./loop.sh https://www.japscan.cc/lecture-en-ligne/manganame first last [-v]```

Replace :

* manganame : by the manga name specified in jaspcan.cc
* first : by the number of the first volume/chapter you want to dl
* last :  by the number of the last volume/chapter you want to dl

N.B : Also note that if you want to dl volumes use the -v option.

Examples:

DL volume 1 to volume 10 of a manga :

``` ./loop.sh https://www.japscan.cc/lecture-en-ligne/manganame 1 10 -v```

DL chapter 100 to chapter 200 of a manga :

``` ./loop.sh https://www.japscan.cc/lecture-en-ligne/manganame 100 200```

### Enjoy

Don't forget to star this project if you like it.
