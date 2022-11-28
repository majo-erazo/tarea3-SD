# Tarea 3: Hadoop

## Integrantes
- Maria José Erazo Gonzalez
- Catalina Gómez Zapkovic

## Hadoop

En este repositorio se tiene el informe, video, código e instrucciones para poder ejecutar la tarea 3 sobre Hadoop. Cabe destacar que para esta tarea nos basamos en el repositorio entregado por el ayudante sobre Hadoop y mapreduce el cual se encuentra en los anexos.

### Paso 1: Correr el contenedor de Hadoop

Para comenzar se debe buildear el contenedor con el siguiente comando. Asegurarse antes de que no hay ningún contenedor con el nombre de hadoop.

```
docker build --no-cache -t hadoop .
```
Luego se levanta el contenedor con el siguiente comando.

```
docker run --name hadoop -p 9864:9864 -p 9870:9870 -p 8088:8088 -p 9000:9000 --hostname sd hadoop
```

Una vez ejecutado los comando, estará listo para entrar al contenedor de Hadoop.


### Paso 2: Ingresar al contenedor de Hadoop

Para poder utilizar el wordcount de Hadoop lo primero que se deberá hacer es entrar a este contenedor, para ello se utiliza el siguiente comando.

```
docker exec -it hadoop bash
```
Luego estando aquí se deberá crear las siguientes carpetas con los siguientes comandos.

```
 hdfs dfs -mkdir /user
 hdfs dfs -mkdir /user/hduser
 hdfs dfs -mkdir input
```

Una vez hecho esto se deberá pasar el input a utilizar con el siguiente comando.

```
hdfs dfs -put map_red/documents/doc1-5/*txt map_red/documents/doc6-10/*txt input
```

### Paso 3: Utilizar mapreduce

Una vez creadas las carpetas y entregado el input en Hadoop, se utiliza el siguiente comando para poder crear y correr los mapper y reducer que será los que realizarán el wordcount.

```
 mapred streaming -files mapper.py,reducer.py -input /user/hduser/input/*.txt -output /user/hduser/output -mapper ./mapper.py -reducer ./reducer.py
```
Una vez hecho esto se utiliza el siguiente comando para poder insertar el output en un txt.

```
hdfs dfs -cat /user/hduser/output/*
```


### Anexos

[Video de funcionamiento del sistema e informe ☜](https://drive.google.com/drive/folders/1A8m2xoFoNtB7i7H31HjrmZElzpK8QHqk?usp=sharing)

[Repositorio del que nos basamos para esta tarea ☜](https://github.com/Naikelin/map-reduce-hadoop)
