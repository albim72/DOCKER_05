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
Komenda 13 -> utworzenie własnego obrazu z zadaną nazwą, wejdż do katlogu z aplikacją: cd diamol\ch03\exercises\web-ping
              utwórz obraz: docker image build --tag web-ping .
Komenda 14 -> wyświetlenie aktywnych obrazów: docker image ls w*
Komenda 15 -> uruchomienie obrazu z dwoma zmiennymi środowiskowymi: docker container run -e TARGET=docker.com -e INTERVAL=5000 web-ping
Komenda 16 -> historia obrazu: docker history web-ping
Komenda 17 -> analiza zawartści lokalnej instancji dockera: docker system df

Zadanie Python:

1. wejście do katalogu projektu: cd python_sigmoid
2. budowa kontenera: docker build -t sigmoid-python
3. uruchomienie obrazu kontenera: docker container run --interactive --tty sigmoid-python

Docker-compose:
1. Stowrzenie sieci docker: docker network create nat
2. Wejście do katalogu projektu...
3. Uruchomie wielokontenerowej aplikacji: docker-compose up
- pobieranie danych z użyciem pliku docker-compose
