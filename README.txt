Komendy platformy Docker:

Komenda 1 -> wersja dockera: docker version
Komenda 2 -> uruchomiemnie kontenera z pakietu diamol: docker container run diamol/ch02-hello-diamol
Komenda 3 -> uruchuomienia interakcyjnego kontenera: docker container run --interactive --tty diamol/base
Komenda 4 -> podgląd informacji o działających kontenerach: docker container ls
Komenda 5 -> podgląd listy procesów na wybranym kontenerze: docker container top e1039436d6c1
Komenda 6 -> uruchomienie aplikacji webowej w tle: docker container run --detach --publish 8088:80 diamol/ch02-hello-diamol-web
Komenda 7 -> statystyki obciążenia procesora, sieci, pamięci ect: docker container stats
Komenda 8 -> pobranie obrazu kontenera: docker image pull diamol/ch03-web-ping
Komenda 9 -> wykonanie kontenera na podstawie obrazu: docker image pull diamol/ch03-web-ping
Komenda 10 -> uruchomienie aplikacji w kontenerze działającym w tle: docker container run -d --name web-ping diamol/ch03-web-ping
Komenda 11 -> usunięcie kontenera: docker rm -f web-ping
Komenda 12 -> uruchomienie kontenera z przekazaniem zmiennej środowiskowej: docker container run --env TARGET=google.com diamol/ch03-web-ping

