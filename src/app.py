import argparse
import os

from dotenv import load_dotenv

from src.hub.hub import hub

'''
    Always make sure to set the environment variable room
    --------------------------------------------
    Example:
    - python src/app.py hub
    - python src/app.py sensor --sensor temp
'''
if __name__ == "__main__":
    load_dotenv()
    room = os.environ.get('room')

    parser = argparse.ArgumentParser(
                    prog='smart-home',
                    description='Smart home application')
    parser.add_argument('app', choices=['hub', 'sensor'], help='Type of the device')
    parser.add_argument('-t', '--type', required=False, help='Type of the sensor', choices=['temp','motion'])
    
    args = parser.parse_args()
    
    match args.app:
        case 'hub':
            rpi_hub = hub()
            rpi_hub.start()
        case 'sensor':
            print('Starting sensor')
        case _:
            print('Unknown device type')