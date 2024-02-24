## Instalando o Kubernetes através do King e criando um cluster

Digitar no terminal

```bash

# verificação da instalação do kind
kind

# verificação da instalação do kubectl
kubectl

# criando nosso cluster Kubernetes utilizando o Kind
kind create cluster

# para se conectar ao cluster nas configuração do Kubernetes para o contexto do kind

kubectl cluster-info --context kind-kind

# verificando os nós disponíveis utilizando o kubectl
kubectl get nodes

# verificando que o cluster está rodando no docker
docker ps -a

# deleteando o cluster kind com apenas um nó
kind delete cluster --name=kind

```

## Criando Cluster com multíplos nós utilizando o kind

Digitar no terminal

```bash

# entrando no diretório da criação do cluster
cd 1.criar-cluster

# criar o cluster com 3 nós workers e um painel de controle no cluster
kind create cluster --config=cluster.yaml --name=k8s-cluster

# aplicar o novo contexto para se conectar ao arquivo de configuração do kubectl
kubectl cluster-info --context kind-k8s-cluster

# verificando os nós disponíveis
kubectl get nodes

# verificando cada container do cluster
docker ps -a

```

## Criando o primeiro pod no cluster Kubernetes com a nossa aplicação

Digitar no terminal

```bash

# voltando um diretório no caminho atual
cd ..

# acesar o diretório
cd 2.criar-pod

# acesar o diretório da aplicacao
cd aplicacao

# criar a imagem docker da aplicação
docker build . -t `USUARIO_DOCKER_HUB`/servidor-python:1.0

# voltando um diretório no caminho atual
cd ..

# verificando se o container roda em ambiente docker
docker-compose up -d

# removendo o docker compose via vs code

# subindo a imagem para o repositório público do Docker Hub
docker push `USUARIO_DOCKER_HUB`/servidor-python:1.0

# criar o secret utilizando o arquivod de configuração .yaml
kubectl apply -f secrets.yaml

# criar o pod utilizando o arquivod de configuração .yaml
kubectl apply -f pod.yaml

# verificando a situação atual do pod criado
kubectl get pods

# verificando as informações do pod utilizando o comando kubectl describe
kubectl describe pod servidor-python

# verificando os logs do pod utilizando o comando kubectl logs
kubectl logs -f servidor-python

# tentando acessar o pod via browser
# http://localhost:8000

# fazendo um proxy-forward para acessar a porta do pod
kubectl port-forward pod/servidor-python 8000:8000

# tentando acessar o pod via browser
# http://localhost:8000

# sair do redirecionamento de portas
ctrl+c

# excluindo o pod criado
kubectl delete pod servidor-python
```

## Criando o primeiro ReplicaSet da nossa aplicação

Digitar no terminal

```bash

# voltando um diretório no caminho atual
cd ..

# acessando a pasta 3.criar-replicaset
cd 3.criar-replicaset

# criando o replicaset com 5 réplicas da aplicação
kubectl apply -f replicaset.yaml

# verificando o replicaset criado
kubectl get replicaset

# verificando os pods ativos com o replicaset
kubectl get pods

# deletando um pod aleatório
kubectl delete pod `NOME_DO_POD`

# verificando novamente os pods ativos
kubectl get pods

# verificando novamente o replicaset
kubectl get replicaset

# atualizando a versão da aplicação para a versão 2.0
cd aplicacao-atualizada
docker build . -t `USUARIO_DOCKER_HUB`/servidor-python:2.0

# adicionando essa imagem para o repositório particular do Docker Hub (Registry)
docker push `USUARIO_DOCKER_HUB`/servidor-python:2.0

# atualizando as configurações do replicaset
cd ..
kubectl apply -f replicaset.yaml

# vefificando os pods ativos
kubectl get pods

# verificando as informações de um dos pods
kubectl describe pod `NOME_DO_POD`

# delentando um pod aleatório do replicaset
kubectl delete pod `NOME_DO_POD`

# vefificando os pods ativos
kubectl get pods

# verificando as informações do pod mais novo
kubectl describe pod `NOME_DO_POD_MAIS_NOVO`

# deletando o replicaset do servidor-python
kubectl delete replicaset servidor-python

# vefificando os pods ativos
kubectl get pods

```

## Criando o primeiro Deployment da nossa aplicação

Digitar no terminal

```bash

# voltando um diretório no caminho atual
cd ..

# acessando a pasta 4.criar-deployment
cd 4.criar-deployment

# criando o deployment com 5 réplicas da aplicação
kubectl apply -f deployment.yaml

# vefificando os a situação dos pods
kubectl get pods

# vefificando a situação dos deployments
kubectl get deployments

# vefificando a situação dos replicasets
kubectl get replicasets

# atualizando a versão da aplicação no deployment para a versão 2.0

# atualizando as configurações do deployment
kubectl apply -f deployment.yaml

# verificando os pods ativos
kubectl get pods

# verificando as informações de um dos pods
kubectl describe pod `NOME_DO_POD`

# vefificando a situação dos replicasets
kubectl get replicasets

```

## Criando o primeiro Service do tipo da nossa aplicação

Digitar no terminal

```bash

# voltando um diretório no caminho atual
cd ..

# acessando a pasta 5.criar-service
cd 5.criar-service

# criando o service do tipo ClusterIP utilizando o arquivo manifesto
kubectl apply -f service-cluster-ip.yaml

# verificando os services ativos
kubectl get services

# verificando os services ativos utilizando o atalho svc
kubectl get svc

# fazendo um proxy-forward para acessar a porta do service
kubectl port-forward svc/servidor-python-service 8000:80

# sair do redirecionamento de portas
ctrl+c

# deletando o servido do tipo ClusterIP do servidor-python
kubectl delete svc servidor-python-service

# criando o service do tipo NodePort utilizando o arquivo manifesto
kubectl apply -f service-node-port.yaml

# verificando novamente os services ativos
kubectl get svc

# fazendo um proxy-forward para acessar a porta do service NodePort
kubectl port-forward svc/servidor-python-service 30001:80

# sair do redirecionamento de portas
ctrl+c

# fazendo um proxy-forward para acessar a porta do service NodePort em uma outra porta da faixa
kubectl port-forward svc/servidor-python-service 30002:80

# sair do redirecionamento de portas
ctrl+c

# deletando o servido do tipo NodePort do servidor-python
kubectl delete svc servidor-python-service

# criando o service do tipo LoadBalancer utilizando o arquivo manifesto
kubectl apply -f service-load-balancer.yaml

# verificando novamente os services ativos
kubectl get svc

# verificando o external-ip com o status de pending

# deletando o servido do tipo LoadBalancer do servidor-python
kubectl delete svc servidor-python-service

# criando novamente o service do tipo ClusterIP utilizando o arquivo manifesto
kubectl apply -f service-cluster-ip.yaml

```

## Criando o primeiro Ingress da nossa aplicação

Digitar no terminal

```bash

# voltando um diretório no caminho atual
cd ..

# acessando a pasta 6.criar-ingress
cd 6.criar-ingress

# configurando o ingress-nginx com todos os seus componentes no cluster kubernetes
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/main/deploy/static/provider/kind/deploy.yaml

# aguardando os componentes do ingress-nginx ficarem ativos
kubectl wait --namespace ingress-nginx --for=condition=ready pod --selector=app.kubernetes.io/component=controller --timeout=90s

# criando o service do tipo ClusterIP utilizando o arquivo manifesto
kubectl apply -f ingress.yaml

# acessando via browser a url http://localhost

# verificando a mudança de pod via terminal
for i in {1..10}; do curl http://localhost -w "\n"; done # Linux - Bash
1..10 | ForEach-Object { Invoke-WebRequest -Uri "http://localhost" -Method Get | Select-Object -ExpandProperty Content } # Windows - PowerShell

```

## AutoScalling, comunicação entre pod e teste de carga

Digitar no terminal

```bash

# voltando um diretório no caminho atual
cd ..

# acessando a pasta 6.criar-ingress
cd 7.criar-hpa

# acessar a pasta metric-server
cd metric-server

# fazer a instalação do metric server via arquivo manifesto
kubectl apply -f components.yaml

# voltando um diretório no caminho atual
cd ..

# configurando o autoscalling do tipo Horizontal com o arquivo manifesto
kubectl apply -f hpa.yaml

# verificar o hpt em modo watch
watch -n1 kubectl get hpa # Linux - Bash
while ($true) { kubectl get hpa; Start-Sleep -Seconds 1; Clear-Host } # Windows - PowerShell

# acessar a pasta do teste de carga
cd ..
cd teste-de-carga-app

# fazer o build na imagem do teste de carga
docker build . -t `USUARIO_DOCKER_HUB`/teste-carga:1.0

# adicionando essa imagem para o repositório particular do Docker Hub (Registry)
docker push `USUARIO_DOCKER_HUB`/teste-carga:1.0

# voltando um diretório no caminho atual
cd ..

# subir o deployment e o service do teste de carga
kubectl apply -f teste-de-carga.yaml

# verificar se todos os recursos estão rodando
kubectl get all

# adicionar um port-forward para acessar o service do teste-de-carga
kubectl port-forward svc/teste-carga-svc 8089:80

# acessar a aplicação do teste de carga via browser

# deletar os recursos do teste de carga
kubectl delete deployment teste-carga-deployment
kubectl delete svc teste-carga-svc

# deletar o recurso de autoscalling do servidor-python
kubectl delete hpa servidor-python

```

## LivenessProbe e ReadinessProbe

Digitar no terminal

```bash

# voltando um diretório no caminho atual
cd ..

# acessando a pasta 6.criar-ingress
cd 8.adicionar-probes

# atualizando a versão da aplicação para a versão 3.0
cd aplicacao-com-checks
docker build . -t `USUARIO_DOCKER_HUB`/servidor-python:3.0

# adicionando essa imagem para o repositório particular do Docker Hub (Registry)
docker push `USUARIO_DOCKER_HUB`/servidor-python:3.0

# voltando um diretório no caminho atual
cd ..

# atualizar deployment utilizando o novo arquivo de configuração
kubectl apply -f deployment-probes.yaml

# vefificando os a situação dos pods
kubectl get pods

# vefificando os logs de um dos pods
kubectl logs -f `NOME_DE_UM_DOS_PODS`
```

## Exclusão dos recursos

Digitar no terminal

```bash

# deletar todos os recursos que foram criados
kubectl delete all --all

# deletar o cluster kind e todos os seus nós
kind delete cluster --name=k8s-cluster

# verificando os containers dockers ativos
docker ps -a
```
