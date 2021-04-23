'''
usb_codes = {
        0x04:"aA", 0x05:"bB", 0x06:"cC", 0x07:"dD", 0x08:"eE", 0x09:"fF",
        0x0A:"gG", 0x0B:"hH", 0x0C:"iI", 0x0D:"jJ", 0x0E:"kK", 0x0F:"lL",
        0x10:"mM", 0x11:"nN", 0x12:"oO", 0x13:"pP", 0x14:"qQ", 0x15:"rR",
        0x16:"sS", 0x17:"tT", 0x18:"uU", 0x19:"vV", 0x1A:"wW", 0x1B:"xX",
        0x1C:"yY", 0x1D:"zZ", 0x1E:"1!", 0x1F:"2@", 0x20:"3#", 0x21:"4$",
        0x22:"5%", 0x23:"6^", 0x24:"7&", 0x25:"8*", 0x26:"9(", 0x27:"0)",
        0x2a: "?",
        0x2C:"  ", 0x2D:"-_", 0x2E:"=+", 0x2F:"[{", 0x30:"]}",  0x32:"#~",
        0x33:";:", 0x34:"'\"",  0x36:",<",  0x37:".>", 0x38:"/?", 0x4f:">",
        0x50:"<"
        }
'''
usb_codes = {
    0X00:"",
    0X01:"Err_Ovf",
    0X02:"PostFail",
    0X03:"Err_Undef",
    0X04:"aA",
    0X05:"bB",
    0X06:"cC",
    0X07:"dD",
    0X08:"eE",
    0X09:"fF",
    0X0a:"gG",
    0X0b:"hH",
    0X0c:"iI",
    0X0d:"jJ",
    0X0e:"kK",
    0X0f:"lL",
    0X10:"mM",
    0X11:"nN",
    0X12:"oO",
    0X13:"pP",
    0X14:"qQ",
    0X15:"rR",
    0X16:"sS",
    0X17:"tT",
    0X18:"uU",
    0X19:"vV",
    0X1a:"wW",
    0X1b:"xX",
    0X1c:"yY",
    0X1d:"zZ",
    0X1e:"1",
    0X1f:"2",
    0X20:"3#",
    0X21:"4",
    0X22:"5",
    0X23:"6",
    0X24:"7",
    0X25:"8",
    0X26:"9",
    0X27:"00",
    0X28:"enter",
    0X29:"escape",
    0X2a:"del",
    0X2b:"tab",
    0X2c:"space",
    0X2d:"-_",
    0X2e:"=+",
    0X2f:"[{",
    0X30:"]}",
    0X31:"\\",
    0X33:";",
    0X34:"'",
    0X35:"^",
    0X36:",",
    0X37:".",
    0X38:"/",
    0X39:"capslock",
    0X3a:"f1",
    0X3b:"f2",
    0X3c:"f3",
    0X3d:"f4",
    0X3e:"f5",
    0X3f:"f6",
    0X40:"f7",
    0X41:"f8",
    0X42:"f9",
    0X43:"f10",
    0X44:"f11",
    0X45:"f12",
    0X46:"sysrq",
    0X47:"scrolllock",
    0X48:"pause",
    0X49:"insert",
    0X4a:"home",
    0X4b:"pageup",
    0X4c:"del",
    0X4d:"end",
    0X4e:"pagedown",
    0X4f:"right",
    0X50:"left",
    0X51:"down",
    0X52:"up",
    0X53:"numlock",
    0X68:"f13",
    0X69:"f14",
    0X6a:"f15",
    0X6b:"f16",
    0X6c:"f17",
    0X6d:"f18",
    0X6e:"f19",
    0X6f:"f20",
    0X70:"f21",
    0X71:"f22",
    0X72:"f23",
    0X73:"f24",
    0X74:"open",
    0X75:"help",
    0X76:"props",
    0X77:"front",
    0X78:"stop",
    0X79:"again",
    0X7a:"ctr-z",
    0X7b:"ctr-x",
    0X7c:"ctr-c",
    0X7d:"ctr-v",
    0X7e:"find",
    0X7f:"mute",
    0X82:"lockcaps",
    0X83:"locknum",
    0X84:"lockscroll",
    0Xb8:"[{",
    0Xb9:"]}",
    0Xba:"tab",
    0Xbb:"backspace",
    0Xbc:"A_hex",
    0Xbd:"B_hex",
    0Xbe:"C_hex",
    0Xbf:"D_hex",
    0Xc0:"E_hex",
    0Xc1:"F_hex",
    0Xc2:"xor",
    0Xcd:"space2",
    0Xce:"@",
    0Xcf:"!",
    0Xe0:"left-ctr",
    0Xe1:"left-shift",
    0Xe2:"left-alt",
    0Xe3:"left-meta",
    0Xe4:"right-ctrl",
    0Xe5:"right-shift",
    0Xe6:"right-alt",
    0Xe7:"right-meta"
    }

#CHTB{a_plac3_fAr_fAar_awway_ffr0m_eearth}

myKeys = open('file.txt')
texto = ""
shit = False

for line in myKeys:
    bytesArray = bytearray.fromhex(line.strip())
    #print ("Line Number: " + str(i))
    for byte in bytesArray:
        if byte != 0:
            if byte == 2:
                shift = True
            keyVal = int(byte)
            if keyVal in usb_codes:
                #print ("Value map : " + str(keyVal) + " — -> " + usb_codes[keyVal])
                '''
                if shift:
                    texto = texto + " " + usb_codes[keyVal]
                else:
                '''
                texto = texto + " " + usb_codes[keyVal]
                #print (usb_codes[keyVal])
            else:
                print("No map found for this value: " + str(keyVal))
print(texto)
