
# Kafka Server Instructions

This README outlines the steps to set up and use Kafka for handling streaming data.

## Steps to Follow

1. **Start a Kafka Server**

   To start a Kafka server, use the following commands:

   ```
   bin\windows\kafka-server-start.bat config\server.properties
   bin\windows\kafka-server-start.bat config\server.properties
   ```

   Ensure that you have Kafka installed and the paths to the `kafka-server-start.bat` and `server.properties` files are correct.

2. **Create a New Topic**

   To create a new topic named `BigSale_test`, use the following command:

   ```
   bin\windows\kafka-topics.bat --create --topic BigSale_test --bootstrap-server localhost:9092
   ```

   This command will create a new topic in Kafka that you can use for streaming data related to 'BigSale_test'.

3. **Run Producer.py to Start the Producer**

   Execute the `producer.py` script to start sending messages. Use the following command:

   ```
   python producer.py
   ```

   Make sure that `producer.py` is correctly configured to send messages to the Kafka topic you created.

4. **Run Consumer.py to Receive Messages and Predict Output**

   To start the consumer and process the messages, run the `consumer.py` script with the command:

   ```
   python consumer.py
   ```

   This script will listen to the Kafka topic, receive messages, and perform the necessary predictions or processing as defined in the script.
