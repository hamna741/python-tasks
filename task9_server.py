import asyncio
import websockets
import json
import time
import logging

async def handle_client(websocket, path):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    # Define console handler with DEBUG log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    #console_handler.propagate=False
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("websocket_logs.log")
    file_handler.setLevel(logging.DEBUG)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    #logging.disable(logging.INFO)
    # logging.basicConfig(handlers=[logging.StreamHandler(), logging.FileHandler("websocket_logs.log")],
    #                     level = logging.DEBUG,
                    
    #                 format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    # Send initial message to client
    print("---------WELCOME TO WEB SERVER---------")
    logging.info(f"CLIENT-->{id(websocket)} CONNECTED SUCCESSFULLY ")
    

    # Wait for messages from the client
    while True:
        try:
            # Receive message from client
            message = await websocket.recv()

            # Parse received message as JSON
            data = json.loads(message)
            logging.info("DATA RECEIVED FROM CLIENT SUCCESSFULLY ", extra={'handler': console_handler})

            # Get current timestamp
            timestamp = time.localtime()

            # Append timestamp to received data
            data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S", timestamp)

            # Send response to client
            response = data
            await websocket.send(json.dumps(response))
            logging.info(f"DATA SENT FROM SERVER TO CLIENT -->{id(websocket)}  SUCCESSFULLY", extra={'handler': console_handler})
        except websockets.exceptions.ConnectionClosed:
            #logger.debug(f"CLIENT-->{id(websocket)} DISCONNECTED")
            # Handle case when client closes the connection
            logging.critical(f"CLIENT-->{id(websocket)} DISCONNECTED")
           # logging.critical(f"CLIENT-->{id(websocket)} DISCONNECTED", extra={'handler': console_handler})
            
            break

    

     
if __name__ == '__main__':
     
    # Set up logging configuration
    #logging.basicConfig(level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')

    # Start WebSocket server
    start_server = websockets.serve(handle_client, 'localhost', 8765)
    logging.info("WebSocket server started at ws://localhost:8765")

    try:
            
        # Run event loop indefinitely
            asyncio.get_event_loop().run_until_complete(start_server)
    #asyncio.get_event_loop().run_forever()
            asyncio.get_event_loop().run_forever()
    except KeyboardInterrupt:
        logging.critical('SERVER INTERUPTTED')
        exit(0)
     
    
    

# # Start WebSocket server
# start_server = websockets.serve(handle_client, 'localhost', 8765)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()