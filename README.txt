Komendy platformy Docker:

Komenda 1 -> wersja dockera: docker version
Komenda 2 -> uruchomiemnie kontenera z pakietu diamol: docker container run diamol/ch02-hello-diamol
Komenda 3 -> uruchuomienia interakcyjnego kontenera: docker container run --interactive --tty diamol/base
Komenda 4 -> podgląd informacji o działających kontenerach: docker container ls
Komenda 5 -> podgląd listy procesów na wybranym kontenerze: docker container top e1039436d6c1
Komenda 6 -> uruchomienie aplikacji webowej w tle: docker container run --detach --publish 8088:80 diamol/ch02-hello-diamol-web
Komenda 7 -> statystyki obciążenia procesora, sieci, pamięci ect: docker container stats
