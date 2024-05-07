komenda 1 - wersja dockera : docker version
komenda 2 - uruchomienue kontenera: docker container run diamol/ch02-hello-diamol
komenda 3 - uruchamianie iterakcyjnego kontenera :  docker container run --interactive --tty diamol/base
komenda 4 - uruchomienie kontenera ze serwerem apache i stroną www: docker container run --detach --publish 8088:80 diamol/ch02-hello-diamol-web
komenda 5 - pobranie obrazu dockera - docker image pull diamol/ch03-web-ping
komenda 6 - uruchomienia kontenra ping: docker container run -d --name web-ping diamol/ch03-web-ping
komenda 7 - wyświetlenie logów - efektów pracy kontenera ping
komenda 8 - zastopowanie pracy kontenera: docker rm - f web-ping
komenda 9  - ustawienie nowego celu (adresu url): docker container run --env TARGET=google.com diamol/ch03-web-ping
