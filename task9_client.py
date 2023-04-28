import asyncio
import websockets
import json
import time
import logging
import os
async def send_messages():
    logger = logging.getLogger()
    # Define console handler with DEBUG log level
    console_handler = logging.StreamHandler()
    
    console_handler.setLevel(logging.DEBUG)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)
    logger.addHandler(console_handler)

    file_handler = logging.FileHandler("websocket_logs.log")
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)

    # logging.basicConfig(filename = 'websocket_logs.log',
    #                     level = logging.CRITICAL,
    #                 format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

    try:
        async with websockets.connect('ws://localhost:8765') as websocket:

            # Load messages from JSON file
            with open('client_messages.json', 'r') as file:
                
                messages = json.load(file)
                logging.info("FILE READ SUCCESSFULLY ")

            # Connect to server
            print("Connecting to server...")
            logging.info(f"CLIENT-->{id(websocket)}CONNECTED TO SERVER AT PORT: ",8765 )
            
           # await websocket.send(json.dumps({'action': 'connect'}))
            #response = await websocket.recv()
        
        
            
          

            # Send messages to server and receive responses
            
           
            if os.path.exists("client_server_data.json"):
                    
                   
                    os.remove("client_server_data.json")
            
            for message in messages:
                start_time = time.time()
                await websocket.send(json.dumps(message))
                
                response = await websocket.recv()
                end_time = time.time()

                #response
                response_data = json.loads(response)
            

                # writing messages to file
                
                with open('client_server_data.json', 'a') as file:
                    file.write("Sent: {}\n".format(message))
                    file.write("Received: {}\n".format(response_data))
                    print(response_data)
                    file.write("Time taken: {:.4f} seconds\n".format(end_time - start_time))
                    file.write("--------------\n")
                    
    except Exception as e:
            
            logging.error("CONNECTION TO SERVER FAILED  %s",e, extra={'handler': console_handler})
def main():
     # Run WebSocket client
     asyncio.get_event_loop().run_until_complete(send_messages())
                    
if __name__ == '__main__':
     main()

