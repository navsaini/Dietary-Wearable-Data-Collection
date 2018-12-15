## How to start data collection
1. Plug in the device to your computer (after you have put it on)
2. Find the name of the USB port on your computer by looking through the `/dev/` directory. It should be contain something like, "cu.usbserial".
3. Make the python file executable by running `chmod +x write_to_file.py`
4. Make sure you have all the python dependencies needed by running `pip3 install -r requirements.txt`
5. Run the `write_to_file.py` script using the following -- 
```
./write_to_file.py name_of_usb_port output.txt
```
6. If it's working, it will start printing a bunch of values.

## How to label files
Name_Action_Environment_Orientation

Ex: Nav_ED_A_C.txt

### Actions
Eating
- Eating quietly (EQ)
- Snacking (ES)
- Eating and talking (ET)
- Drinking (ED)

Not Eating
- Talking (NT)
- Silence (NS)
- Coughing (NC)

### Environment
- Alone (A)
- In public (P)

### Proximity Sensor Orientation
- Left (L)
- Center (C)
- Right (R)
