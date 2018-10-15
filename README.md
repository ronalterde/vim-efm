# Sample code for the blog article *Vim Errorformat Challenge*
[link to blog](http://steffen.ronalter.de/2018/04/15/vim-errorformat-challenge/)

## Run the examples
Create output to be injected via `cfile`:
```
make error_output.txt
```

## Challenge solution
Setting Vim's errorformat option to this value will enable parsing the output
from `query_match.py`:
```
:set errorformat=%f\:%l\:%c
```
