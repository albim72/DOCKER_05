komenda 1 - wersja dockera : docker version
komenda 2 - uruchomienue kontenera: docker container run diamol/ch02-hello-diamol
komenda 3 - uruchamianie iterakcyjnego kontenera :  docker container run --interactive --tty diamol/base
komenda 4 - uruchomienie kontenera ze serwerem apache i stroną www: docker container run --detach --publish 8088:80 diamol/ch02-hello-diamol-web
komenda 5 - pobranie obrazu dockera - docker image pull diamol/ch03-web-ping
komenda 6 - uruchomienia kontenra ping: docker container run -d --name web-ping diamol/ch03-web-ping
komenda 7 - wyświetlenie logów - efektów pracy kontenera ping
komenda 8 - zastopowanie pracy kontenera: docker rm - f web-ping
komenda 9  - ustawienie nowego celu (adresu url): docker container run --env TARGET=google.com diamol/ch03-web-ping
komenda 10 - wejście do katalogu z docckerfile: cd C:\diamol\ch03\exercises\web-ping
komenda 11 - utworzenie nowego obrazu: docker image build --tag web-ping .
komenda 12 - uruchomienie konetera z zadaniem nowych zmiennych środowiskowych:  docker container run -e TARGET=docker.com -e INTERVAL=5000 web-ping
komenda 13 - wyświetlenie historii obrazów: docker image history web-ping
komenda 14 - zestawienie obrazów i ich rozmiarów: docker image ls
komenda 15 - badanie rozmiaru elementów dockera: docker system df
Zadanie Python 
utowrzenie obrazu: 
docker build -t sigmoid-app .

uruchomienie kontenera:
docker container run --interactive --tty sigmoid-app

aplikacja www flask:
docker build -t flask-app .

uruchomienie: docker run -p 5000:5000 flask-app
Docker-Compose:

1. docker network create nat
2. docker-compose up
3. cd .ch07/excercises/image_of_the_day
4. docker-compose up --detach
5. docker-compose up -d --scale iotd=3
6. docker-compose logs ==tail=1 iotd
7.docker-compose stop
8,docker-compose start
9,docker container ls
