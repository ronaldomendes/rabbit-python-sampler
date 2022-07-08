# RabbitMQ Python Sampler

An example includes integration with RabbitMQ and showing a simple way to publish and subscribe messages in a single queue using Python language. 

If you want to configure a new Docker image on your computer, use the command below.

``docker run -d --name rabbit-docker -p 15672:15672 -p 5672:5672 -e RABBITMQ_DEFAULT_USER=master -e RABBITMQ_DEFAULT_PASS=m45t3r rabbitmq:3-management``