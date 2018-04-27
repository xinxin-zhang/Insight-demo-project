# Terraform utilization in SETI streaming detection of anomalous signals

## Data source:
SETI(the Search for Extraterrestrial Intelligence) Given a suitable environment and sufficient time, life will develop on other planets. Such a civilization could be detected across interstellar distances, and may actually offer our best opportunity for discovering extraterrestrial life in the near future.

## Stream pipeline:
Producers - Kafka - Spark streaming -Cassandra

## Purpose

Terraform will be used to build, change, and version infrastructure safely and efficiently in spark streaming.
In terraform, a provider is responsible for understanding API interactions and exposing resources. 73 providers are available, AWS is just one of them. But Kafka is not supported. Implentmentation of Kafka terraform provider helps topic management and monitoring. 

## Challenges:

* Install tehologies on different nodes
* Scalability upon increase in data volumn
* More sophisciated calculation
* Fault tolerance examination
  
