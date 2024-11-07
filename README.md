# Web-Development-Basic
instruction version 1:
instructions to run the MoviesProject:
1)to download MoviesProject run this command in your terminal/powershell:
    git clone https://github.com/faroukshtewee/Web-Development-Basic/tree/DevOpsCourse
2) in powershell go to where you downloaded the project and CD    to /WebDevelopment/MoviesProject/MoviesProject
3)  run this bash in  your  terminal/powershell:
    docker build -t my-django-app . 
    (you can change the image name "my-django-app" and put  what you want)
4) and you should run this bash in your terminal/powershell to    run the Docker container:
   docker run -d -p 8000:8000 --name my-django-container my-django-app
   
   (you can change the container name "my-django-container" and put what you want)

attention:

if u changed the image name at step 3 in instructions u should put the same image name at step 4 

5) and now u can go to localhost:8000 in your web browser and u can choose wihch movie you want to watch
---------------------------------------------------------------------------------------
instruction version 2( after convert sqlite to mysql  ):
instructions to run the MoviesProject:
1)to download MoviesProject run this command in your terminal/powershell:
    git clone https://github.com/faroukshtewee/Web-Development-Basic/tree/DevOpsCourse
2) in powershell go to where you downloaded the project and CD    to /WebDevelopment/MoviesProject/MoviesProject
3)  run this bash in  your  terminal/powershell:
    docker compose up --build
4) and now u can go to localhost:8000 in your web browser and u can choose wihch movie you want to watch