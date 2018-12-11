
1. Plug in the device to your computer (after you have put it on)
2. Find the name of the USB port on your computer by looking through the `/dev/` directory. It should be contain something like, "cu.usbserial".
3. Make the python file executable by running `chmod +x write_to_file.py`
4. Run the `write_to_file.py` script using the following -- `./write_to_file.py name_of_usb_port output.txt`
5. If it's working, it will start printing a bunch of values.
