#!/usr/bin/env python
import os, sys, re

barcodeTable = [
    [" ",            " ",             "00",           "11011001100"],
    ["!",            "!",             "01",           "11001101100"],
    ['"',            '"',             "02",           "11001100110"],
    ["\#",           "\#",            "03",           "10010011000"],
    ["$",            "$",             "04",           "10010001100"],
    ["%",            "%",             "05",           "10001001100"],
    ["&",            "&",             "06",           "10011001000"],
    ["'",            "'",             "07",           "10011000100"],
    ["(",            "(",             "08",           "10001100100"],
    [")",            ")",             "09",           "11001001000"],
    ["*",            "*",             "10",           "11001000100"],
    ["+",            "+",             "11",           "11000100100"],
    [",",            ",",             "12",           "10110011100"],
    ["-",            "-",             "13",           "10011011100"],
    [".",            ".",             "14",           "10011001110"],
    ["/",            "/",             "15",           "10111001100"],
    ["0",            "0",             "16",           "10011101100"],
    ["1",            "1",             "17",           "10011100110"],
    ["2",            "2",             "18",           "11001110010"],
    ["3",            "3",             "19",           "11001011100"],
    ["4",            "4",             "20",           "11001001110"],
    ["5",            "5",             "21",           "11011100100"],
    ["6",            "6",             "22",           "11001110100"],
    ["7",            "7",             "23",           "11101101110"],
    ["8",            "8",             "24",           "11101001100"],
    ["9",            "9",             "25",           "11100101100"],
    [":",            ":",             "26",           "11100100110"],
    [";",            ";",             "27",           "11101100100"],
    ["<",            "<",             "28",           "11100110100"],
    ["=",            "=",             "29",           "11100110010"],
    [">",            ">",             "30",           "11011011000"],
    ["?",            "?",             "31",           "11011000110"],
    ["@",            "@",             "32",           "11000110110"],
    ["A",            "A",             "33",           "10100011000"],
    ["B",            "B",             "34",           "10001011000"],
    ["C",            "C",             "35",           "10001000110"],
    ["D",            "D",             "36",           "10110001000"],
    ["E",            "E",             "37",           "10001101000"],
    ["F",            "F",             "38",           "10001100010"],
    ["G",            "G",             "39",           "11010001000"],
    ["H",            "H",             "40",           "11000101000"],
    ["I",            "I",             "41",           "11000100010"],
    ["J",            "J",             "42",           "10110111000"],
    ["K",            "K",             "43",           "10110001110"],
    ["L",            "L",             "44",           "10001101110"],
    ["M",            "M",             "45",           "10111011000"],
    ["N",            "N",             "46",           "10111000110"],
    ["O",            "O",             "47",           "10001110110"],
    ["P",            "P",             "48",           "11101110110"],
    ["Q",            "Q",             "49",           "11010001110"],
    ["R",            "R",             "50",           "11000101110"],
    ["S",            "S",             "51",           "11011101000"],
    ["T",            "T",             "52",           "11011100010"],
    ["U",            "U",             "53",           "11011101110"],
    ["V",            "V",             "54",           "11101011000"],
    ["W",            "W",             "55",           "11101000110"],
    ["X",            "X",             "56",           "11100010110"],
    ["Y",            "Y",             "57",           "11101101000"],
    ["Z",            "Z",             "58",           "11101100010"],
    ["[",            "[",             "59",           "11100011010"],
    ["\\",           "\\",            "60",           "11101111010"],
    ["]",            "]",             "61",           "11001000010"],
    ["^",            "^",             "62",           "11110001010"],
    ["_",            "_",             "63",           "10100110000"],
    ["\0",           "`",             "64",           "10100001100"], # Null
    ["SOH",          "a",             "65",           "10010110000"],
    ["STX",          "b",             "66",           "10010000110"],
    ["ETX",          "c",             "67",           "10000101100"],
    ["EOT",          "d",             "68",           "10000100110"],
    ["ENQ",          "e",             "69",           "10110010000"],
    ["ACK",          "f",             "70",           "10110000100"],
    ["BEL",          "g",             "71",           "10011010000"],
    ["\b",           "h",             "72",           "10011000010"], # Backspace
    ["\t",           "i",             "73",           "10000110100"], # Horizontal Tab
    ["\n",           "j",             "74",           "10000110010"], # Linefeed
    ["\v",           "k",             "75",           "11000010010"], # Vertical Tab
    ["\f",           "l",             "76",           "11001010000"], # Form Feed
    ["\r",           "m",             "77",           "11110111010"], # Carriage Return
    ["SO",           "n",             "78",           "11000010100"],
    ["SI",           "o",             "79",           "10001111010"],
    ["DLE",          "p",             "80",           "10100111100"],
    ["DC1",          "q",             "81",           "10010111100"],
    ["DC2",          "r",             "82",           "10010011110"],
    ["DC3",          "s",             "83",           "10111100100"],
    ["DC4",          "t",             "84",           "10011110100"],
    ["NAK",          "u",             "85",           "10011110010"],
    ["SYN",          "v",             "86",           "11110100100"],
    ["ETB",          "w",             "87",           "11110010100"],
    ["CAN",          "x",             "88",           "11110010010"],
    ["EM",           "y",             "89",           "11011011110"],
    ["SUB",          "z",             "90",           "11011110110"],
    ["ESC",          "{",             "91",           "11110110110"],
    ["FS",           "|",             "92",           "10101111000"],
    ["GS",           "}",             "93",           "10100011110"],
    ["RS",           "~",             "94",           "10001011110"],
    ["US",           "DEL",           "95",           "10111101000"],
    ["FNC 3",        "FNC 3",         "96",           "10111100010"],
    ["FNC 2",        "FNC 2",         "97",           "11110101000"],
    ["Shift B",      "Shift A",       "98",           "11110100010"],
    ["Code C",       "Code C",        "99",           "10111011110"],
    ["Code B",       "FNC 4",         "Code B",       "10111101110"],
    ["FNC 4",        "Code A",        "Code A",       "11101011110"],
    ["FNC 1",        "FNC 1",         "FNC 1",        "11110101110"],
    ["Start Code A", "Start Code A",  "Start Code A", "11010000100"],
    ["Start Code B", "Start Code B",  "Start Code B", "11010010000"],
    ["Start Code C", "Start Code C",  "Start Code C", "11010011100"],
    ["Stop",         "Stop",          "Stop",         "11000111010"],
    ["Reverse Stop", "Reverse Stop",  "Reverse Stop", "11010111000"],
    ["Stop pattern", "Stop pattern",  "Stop pattern", "1100011101011"]
]

CODEA = 0
CODEB = 1
CODEC = 2

def calculateChecksum(message):
    sum = message[0][1]
    for i in range(1, len(message)):
        sum += i * message[i][1]

    return sum % 103

def lookup(char, mode):
    # Look for character in current mode
    for i in range(len(barcodeTable)):
        if barcodeTable[i][mode] == char:
            return i, mode

    # No matching character found in current mode. Check other modes:
    for i in range(len(barcodeTable)):
        if char in barcodeTable[i]:
            return i, barcodeTable[i].index(char)

    return -1, -1

def hex2rgb(h):
    return tuple(int(h[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def savePng(barcode, inputString, filename, settings):
    # Save PNG using Cairo
    from PIL import Image
    import cairo

    length_barcode = len(barcode)
    width_bar      = settings["scale"]
    font_size      = width_bar * 15
    width_barcode  = width_bar * length_barcode
    height_barcode = width_barcode / 3
    border         = width_bar * 10
    width_total    = width_barcode + (border * 2)
    height_total   = height_barcode + (border * 2)
    foreground     = settings["fgcolor"]
    background     = settings["bgcolor"]

    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width_total, height_total)
    ctx     = cairo.Context(surface)

    # Draw border
    ctx.set_source_rgb(*background)
    ctx.rectangle(0, 0, width_total, height_total)
    ctx.fill()

    # Draw Barcode
    for i in range(len(barcode)):
        if barcode[i] == "1":
            ctx.set_source_rgb(*foreground)
        else:
            ctx.set_source_rgb(*background)

        ctx.rectangle(i*width_bar + border,
                      border,
                      width_bar,
                      height_barcode)
        ctx.fill()

    # Overlay text value
    if settings["string"] == True:
        ctx.select_font_face("Courier",
                             cairo.FONT_SLANT_NORMAL,
                             cairo.FONT_WEIGHT_BOLD)
        ctx.set_font_size(font_size)
        x_bearing, y_bearing, width_text, height_text = ctx.text_extents(inputString)[:4]

        # Draw box behind text
        ctx.set_source_rgb(*background)
        width_startbars = width_bar * len(barcodeTable[103][3])
        width_endbars   = width_bar * len(barcodeTable[108][3])
        ctx.rectangle(border + width_startbars,
                      height_barcode - height_text + (border / 2),
                      width_barcode - width_startbars - width_endbars,
                      height_text + (border))
        ctx.fill()

        # Display text
        ctx.move_to((width_total - width_text) / 2, height_total-border)
        ctx.set_source_rgb(*foreground)
        ctx.show_text(inputString)

    # Write to file
    surface.write_to_png(filename+".png")
    return

def savePpm(barcode, filename, settings):
    # Save PPM of barcode
    height = len(barcode) / 4
    Buffer = "P1\n%d %d\n" % (len(barcode), height)
    for i in range(height):
        Buffer += " ".join(barcode)+"\n"
    f = open(filename+".ppm", 'w')
    f.write(Buffer)
    f.close()
    return

def barcodify(inputString, settings):
    filename    = inputString
    inputArray = list(inputString)
    mode        = CODEB # Start with this since is most common
    message     = []

    # Start
    startDict = ["Start Code A", "Start Code B", "Start Code C"]
    value, mode = lookup(startDict[mode], mode)
    message.append([startDict[mode], value])

    # Process inputArray and look for code changes
    modeDict = ["Code A", "Code B", "Code C"]
    for i in range(len(inputArray)):
        value, nextmode = lookup(inputArray[i], mode)
        if nextmode != mode:
            tvalue, mode = lookup(modeDict[nextmode], mode)
            message.append([modeDict[nextmode], tvalue])
            mode = nextmode
        message.append([inputArray[i], value])

    # Add close statement
    message.append(["CRC", calculateChecksum(message)])
    value, mode = lookup("Stop pattern", mode)
    message.append(["Stop pattern", value])

    # Generate Barcode String
    barcode = ""
    for i in message:
        characterBarcode = barcodeTable[i[1]][3]
        barcode += characterBarcode
        if settings["verbose"] == True:
            print characterBarcode, i

    # Create output filename
    filename    = re.sub("[\s]",        "_", filename)
    filename    = re.sub("[\\\/:;=()]", "",  filename)

    # Save to file
    savePng(barcode, inputString, filename, settings)
    return


if len(sys.argv) < 2:
    print("Please provide value or string to convert to barcode.")
    quit()

# Process arguments
settings = {
    "verbose" : False,
    "scale"   : 3,
    "bgcolor" : (1.0, 1.0, 1.0),
    "fgcolor" : (0.0, 0.0, 0.0),
    "string"  : True,
}

strings = []
i = 1
while i < len(sys.argv):
    argument = sys.argv[i]
    if argument in ["-v", "--verbose"]:
        settings.update({"verbose" : True})
    elif argument in ["--bgcolor"]:
        i += 1
        settings.update({"bgcolor" : hex2rgb(sys.argv[i])})
    elif argument in ["--fgcolor"]:
        i += 1
        settings.update({"fgcolor" : hex2rgb(sys.argv[i])})
    elif argument in ["-s", "--scale"]:
        i += 1
        settings.update({"scale" : int(sys.argv[i])})
    elif argument in ["--nolabel"]:
        settings.update({"string" : False})
    else:
        strings.append(argument)
    i += 1

for i in strings:
    barcodify(i, settings)

