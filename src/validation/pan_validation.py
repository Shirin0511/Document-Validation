import re

def extract_pan(ocr_text : str):

    for line in ocr_text.splitlines():
        if "PAN" in line.upper():
            parts= line.split(":")
            if len(parts)>1:
                return parts[1].strip().upper()
    return None

def validate_pan(pan: str):

    PAN_REGEX= r"[A-Z]{5}[0-9]{4}[A-Z]"

    if not pan:
        return None
    return bool(re.fullmatch(PAN_REGEX, pan))


def validate_pan_pipeline(ocr_text: str) :

    pan= extract_pan(ocr_text)

    if not pan:
        return{
            "pan_present" : False,
            "pan_number"  : None,
            "pan_valid"   : False,
            "reason"      : "PAN not found"
        }
    
    if not validate_pan(pan):

        return{
            "pan_present" : True,
            "pan_number"  : pan,
            "pan_valid"   : False,
            "reason"      : "PAN format is not valid"
        }
    
    return{
            "pan_present" : True,
            "pan_number"  : pan,
            "pan_valid"   : True,
            "reason"      : "PAN format is valid"
    }


if __name__=="__main__":

    sample_input= """
    INCOME TAX DEPARTMENT
    GOVERNMENT OF INDIA

    Name: TAMMY BELTRAN
    DOB: 18/11/1969
    PAN: GHDOA8008B

    """

    pan_dict= validate_pan_pipeline(sample_input)

    print(pan_dict)


    
