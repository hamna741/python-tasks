import asyncio
import websockets
import json
import time
import logging
#client_count={}
async def handle_client(websocket, path):
    #client_count=client_count[id(websocket)] = websocket
    logging.basicConfig(filename = 'websocket_logs.log',
                        level = logging.INFO,
                    
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    # Send initial message to client
    print("---------WELCOME TO WEB SERVER---------")
    logging.info(f"CLIENT-->{id(websocket)} CONNECTED SUCCESSFULLY ")
    
   # initial_message = {'message': 'Welcome to the WebSocket server!'}
    #await websocket.send(json.dumps(initial_message))

    # Wait for messages from the client
    while True:
        try:
            # Receive message from client
            message = await websocket.recv()

            # Parse received message as JSON
            data = json.loads(message)
            logging.info("DATA RECEIVED FROM CLIENT SUCCESSFULLY ")

            # Get current timestamp
            timestamp = time.localtime()

            # Append timestamp to received data
            data['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S", timestamp)

            # Send response to client
            response = data
            await websocket.send(json.dumps(response))
            logging.info(f"DATA SENT FROM SERVER TO CLIENT -->{id(websocket)}  SUCCESSFULLY")
        except websockets.exceptions.ConnectionClosed:
            # Handle case when client closes the connection
            logging.critical(f"CLIENT-->{id(websocket)}DISCONNECTED")
            print("Client disconnected.")
            
            break
    client_count+=1
    
client_count=1
# Start WebSocket server
start_server = websockets.serve(handle_client, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
