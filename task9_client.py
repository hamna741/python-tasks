import asyncio
import websockets
import json
import time
import logging
import os
async def send_messages():
    logging.basicConfig(filename = 'websocket_logs.log',
                        level = logging.CRITICAL,
                    format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')
    async with websockets.connect('ws://localhost:8765') as websocket:

        # Load messages from JSON file
        with open('client_messages.json', 'r') as f:
            
            messages = json.load(f)
            logging.info("FILE READ SUCCESSFULLY ")

        # Connect to server
        print("Connecting to server...")
        logging.info(f"CLIENT-->{id(websocket)}CONNECTED TO SERVER AT PORT: ",8765 )
        print("sending data from server...")
        await websocket.send(json.dumps({'action': 'connect'}))
        response = await websocket.recv()
       
        #print("Connected to server! Response: {}".format(response))
        
        logging.info(f"CLIENT-->{id(websocket)} CONNECTED TO SERVER AT PORT: ",8765 )

        # Send messages to server and receive responses
        
        print("receiving data from server...")
        if os.path.exists("cleint_server_data.json"):
                 
                 print("deleting old copy of file")
                 os.remove("cleint_server_data.json")
        print("writng to json file")
        for message in messages:
            start_time = time.time()
            await websocket.send(json.dumps(message))
            
            response = await websocket.recv()
            end_time = time.time()

            #response
            response_data = json.loads(response)
           # print("Received from server: {}".format(response_data))
            #print("Time taken to receive response: {:.2f} seconds".format(end_time - start_time))

            # writing messages to file
            
            with open('cleint_server_data.json', 'a') as f:
                f.write("Sent: {}\n".format(message))
                f.write("Received: {}\n".format(response_data))
                f.write("Time taken: {:.4f} seconds\n".format(end_time - start_time))
                f.write("--------------\n")
                logging.info("TIME TAKEN TO SEND AND REVCEIVE DATA IN {:.4f} SECONDS: ",end_time - start_time )

# Run WebSocket client
asyncio.get_event_loop().run_until_complete(send_messages())
