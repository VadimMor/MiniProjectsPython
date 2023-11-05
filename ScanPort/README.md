# PORT SCANNER
## port scanner for udp and tcp sockets
---
#### Flags for running the script:
**-p** - range of ports to scan
```sh
-p 120-140
```
**-a** - scan address
```sh
-a ru.wikipedia.org
-a 185.15.59.224
```
**-sT** - tcp socket selection
```sh
-p 120-140 -sT -a ru.wikipedia.org 
```
**-sU** - udp socket selection
```sh
-p 120-140 -sU -a ru.wikipedia.org 
```
----
#### Example
```sh
python ./main.py -p 120-140 -sU -a ru.wikipedia.org 
```
![photo](https://ltdfoto.ru/images/2023/11/05/imagef87767382916b949.png)