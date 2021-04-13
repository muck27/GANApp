########### Download the Model from this path########
1. drive link: https://drive.google.com/uc?id=1MEGjdvVpUsu1jB4zrXZN7Y4kBBOzizDQ
2. Keep the downloaded model as gan.pkl in backend folder
3. from root directory $docker-compose build
4. from root directory $docker-compose up -d
5. Go to localhost:9000/create/gan/ on browser
6. API requires 2 arguments images and prefix
----  example body
	 {
	   "images":10,
           "prefix":"batch-1"
	
	}
