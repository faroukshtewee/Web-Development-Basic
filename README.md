# Web-Development-Basic
instructions to run the MoviesProject:
1) in powershell go to where you downloaded the project and CD    to /WebDevelopment/MoviesProject/MoviesProject
2)  run this bash in  your  terminal/powershell:
    docker build -t my-django-app . 
    (you can change the image name "my-django-app" and put  what you want)
3) and you should run this bash in your terminal/powershell to    run the Docker container:
   docker run -d -p 8000:8000 --name my-django-container my-django-app
   
   (you can change the container name "my-django-container" and put what you want)

attention:

if u changed the image name at step 2 in instructions u should put the same image name at step 3 

4) and now u can go to localhost:8000 in your web browser and    u can choose wich movie you want to watch
