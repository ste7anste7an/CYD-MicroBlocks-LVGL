# CYD-MicroBlocks-LVGL - One firmware to rule them all!
Cheap Yellow Displays come in various forms and types. They mainly differ in the type of TFT panel driver and type of Touch controller. Generating a MicroBlocks firmware for each variant is tedious and need to be cdone for every new type.

This firmware supports the MicroBlcoks TFT library, but also supports LVGL. See ... for the library and examples

## Getting started
Go to the [firmware downloader](https://firmware.ste7an.nl) and choose 'generic CYD firmware'. Follow the steps on the webpage to install the firmware. Some CYD's do not enter Firmware upload mode automaticaly. When you see the the upload starts, while keeping the BOOT0 button pressed, briefly press the RST button and release BOOT0. 

Connect your CYD with MicroBlocks. Select a `config.txt` file from this repository and drag the file into the IDE program background, or use the File -> Put file on baord. Reboot your board and you should see the BLE identifier showing on the screen (black screen with Ggreen blocks). Now, load the 'touch_check.ubp' to see whether the touch panel is working and wether the coordinates correspond with the TFT panel. To get the coordiantes correct, vary `rotation`, `flip_x', `flip_y` and `flip_x_y` in the config file, reupload, reset and try again. 

## Configuration file
Therefore, I created a firmware that reads a configuration file from the LittleFS filesystem on the board. This file can easily be edited and replaced as to fit the configuration for a specific board. 

This results in a single fimrware for all the SPI-based TFT panel CYD's and for each type a configuration file. Go to the [configurator]() webpage to see all the options and to build a config file.

### LCD section
Here you define the controller type (which is ILI9341) and the GPIO's used for the SPI, DC, RST, CS and backlight. The SPI hardware interface used is specified. Usually choose either 2 or 3. Furthermore you can define the height, wisth and the rotation from 0..3 which corresponds to 0, 90, 180 and 270 degrees.
### LVGL section
In some cases the height and width of the TFT panel are 90 degrees rotated. Therefore, the height and width used in LVGL (and also in the TFT library of MicroBlocks) are redefined here. In most cases, they are the same as in the LCD section
### Touch section
Two types of touch controllers are typically used. Resistive touch displays use XPT2046, capacitive touch displays use CST820. The XOT2046 is connected via SPI. In some cases it uses the same SPI controller as the TFT panel. In that case tyhe signals MISO, MOSI, and SCLK are the same and it uses the same SPI hardware interface. When the XPT is connected to a different SPI bus, the corresponding SPI signals MISO, MOSI, SCLK are defined and the SPI hardware controller should be different from the one osed in the LCD section.

Because in some panels the touch controlller is rotated with respect to the LCD panel, there are 3 boolean coreection options: flip_x, flip_y and flip_x_y. Together with the rotation of the Touch controller, the values have to be experimentally determined.

## LED
All the CYD panels come with an RGB LED driven by GPIO4 (R), GPIO16 (G), and GPIO17 (B). The Red led is confugured as the default Output LED in MicroBlcoks

## Ports
All the CYD's come typically with 3 4-pin ports: P1 is usually the UART port which is connected to TX and RX of the boards UART (which is also connected to a CH341 for USB connection), P3 (GND, GPIO35, GPIO22, and GPIO21), and CN1 (3V3, GPIO21, GPIO22, GND). Some boards use GPIO21 for the TFT Backlight, other use GPIO27, and yet other have CN1 with (3V3, GPIO27, GPIO22). Note that GPIO35 is an input-only pin.

## Buttons
On all CYD there are push buttons for RST and BOOT0. BOOT0 is GPIO0, so that buton is by default configured as 'Button A' oin MicroBlocks. Some variants have a small push button which controls how the battery is used (so it is not connected to a GPIO).


