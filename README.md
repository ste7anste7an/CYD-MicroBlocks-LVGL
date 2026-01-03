# CYD-MicroBlocks-LVGL  
**One firmware to rule them all!**

Cheap Yellow Displays (CYDs) come in various forms and types. They mainly differ in the type of TFT panel driver and the type of touch controller used. Generating a separate MicroBlocks firmware for each variant is tedious and needs to be redone for every new board type.

This firmware supports the **MicroBlocks TFT library** and also **LVGL**. See … for the library and examples.

---

## Getting started

Go to the [firmware downloader](https://firmware.ste7an.nl) and choose  
**“MicroBlocks 3.70 for Cheap Yellow Display using TFT configurator”**.  
Follow the steps on the webpage to install the firmware.

Some CYDs do not enter firmware upload mode automatically. In that case, keep the **BOOT0** button pressed while uploading.

Next, connect your CYD to MicroBlocks. Select a `config.txt` file from this repository and drag it into the IDE background, or use **File → Put file on board**.

Reboot the board. You should see the BLE identifier displayed on the screen (black background with green blocks). Then load `touch_check.ubp` to verify that:

- the touch panel is working
- the touch coordinates match the TFT orientation

To get the coordinate mapping correct, adjust `rotation`, `flip_x`, `flip_y`, and `flip_x_y` in the configuration file. Re-upload the file, reset the board, and test again.

---

## Configuration file

This firmware reads a configuration file from the **LittleFS** filesystem on the board. The file can easily be edited and replaced to match the configuration of a specific CYD variant.

This approach results in a **single firmware** for all SPI-based TFT CYDs, with a separate configuration file per board type.

Go to the [configurator]() webpage to see all available options and to build a configuration file.

---

### LCD section

In this section you define:

- The LCD controller type (currently **ILI9341**)
- GPIOs used for SPI, DC, RST, CS, and backlight
- The SPI hardware interface to use (usually **SPI2** or **SPI3**)
- Display `width`, `height`, and `rotation`

The `rotation` value ranges from `0` to `3`, corresponding to **0°, 90°, 180°, and 270°**.

---

### LVGL section

In some cases the physical orientation of the TFT panel is rotated by 90 degrees. Therefore, the width and height used by **LVGL** (and also by the MicroBlocks TFT library) can be redefined here.

In most cases, these values are the same as those in the LCD section.

---

### Touch section

Two types of touch controllers are typically used:

- **XPT2046** for resistive touch displays  
- **CST820** for capacitive touch displays

The XPT2046 is connected via SPI. In some designs it shares the same SPI bus as the TFT panel. In that case, the `MISO`, `MOSI`, and `SCLK` signals are shared, and the same SPI hardware interface is used.

If the XPT2046 is connected to a different SPI bus, the corresponding `MISO`, `MOSI`, and `SCLK` pins must be defined, and a different SPI hardware interface should be selected than the one used for the LCD.

Because the touch controller may be rotated relative to the LCD panel, three boolean correction options are provided:

- `flip_x`
- `flip_y`
- `flip_x_y`

Together with the touch controller rotation setting, these values must be determined experimentally.

---

## LED

All CYD panels include an RGB LED driven by:

- GPIO4 (Red)
- GPIO16 (Green)
- GPIO17 (Blue)

The **red LED** is configured as the default output LED in MicroBlocks.

---

## Ports

CYDs typically provide three 4-pin ports:

- **P1**: UART port connected to the board’s TX and RX pins  
  (also connected to a CH341 for USB)
- **P3**: GND, GPIO35, GPIO22, GPIO21
- **CN1**: 3V3, GPIO21, GPIO22, GND

Some boards use **GPIO21** for the TFT backlight, others use **GPIO27**, and some have CN1 wired as `(3V3, GPIO27, GPIO22, GND)`.

⚠️ Note: **GPIO35 is input-only**.

---

## Example `config.txt`

```ini
# CYD-MicroBlocks-LVGL configuration file

[lcd]
controller = ILI9341
spi_host   = 2
cs         = 15
dc         = 2
rst        = 4
backlight  = 21
sclk       = 18
mosi       = 23
miso       = 19
width      = 240
height     = 320
rotation   = 1

[lvgl]
width  = 240
height = 320

[touch]
type       = XPT2046
spi_host   = 2
cs         = 5
irq        = 34
sclk       = 18
mosi       = 23
miso       = 19
rotation   = 0
flip_x     = false
flip_y     = true
flip_x_y   = false

[other]

green = 16
blue  = 17
