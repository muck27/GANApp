########### Download the Model from this path########
1. drive link: https://drive.google.com/uc?id=1MEGjdvVpUsu1jB4zrXZN7Y4kBBOzizDQ
2. Keep the downloaded model as gan.pkl in backend folder
3. Add /data in docker-compose.yml (new generated images will be downloaded here)
3. from root directory $docker-compose build
4. from root directory $docker-compose up -d
5. Go to localhost:9000/create/gan/ on browser
6. API requires 4 arguments images, prefix,width,height
----  example body
	 {
	   "images":10,
           "prefix":"batch-1"
           "width":100,
           "height":100,
           "seed":10000	
	}

7. Install dockerhub (https://hub.docker.com/editions/community/docker-ce-desktop-windows/)
