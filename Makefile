build:
    docker build -t task5 .

push:
    docker tag task5 zinoor/task5:latest
    docker push zinoor/task5:latest

deploy:
    kubectl apply -f deployment.yaml

service:
    kubectl apply -f service.yaml
	minikube service task5-service


