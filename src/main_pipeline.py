from .validation.pan_validation import validate_pan_pipeline
from .validation.aadhar_validation import validate_aadhar_pipeline
from .document_detector import detect_doc_type

def validate_documents(ocr_text: str):

    """
    Main Document Validation Pipeline
    
    """

    doc_type = detect_doc_type(ocr_text)

    if doc_type == "PAN" :
        result = validate_pan_pipeline(ocr_text)

    elif doc_type == "AADHAR" :
        result = validate_aadhar_pipeline(ocr_text)

    else:
        return{
            "document_type" : "UNKNOWN",
            "decision" : "REJECT",
            "reason" : "Unrecognizable Document Provided"
        }   

    return result


if __name__ == "__main__":

    sample_pan = """
    INCOME TAX DEPARTMENT

    Name: TAMMY BELTRAN
    DOB: 18/11/1969
    PAN: GHDOA8008B
    """

    sample_aadhaar = """
    GOVERNMENT OF INDIA

    Name: RAHUL SHARMA
    DOB: 21/05/1998

    1234 5678 9123

    Address:
    22 MG Road
    Bangalore
    Karnataka
    """


    pan_result= validate_documents(sample_pan)

    for k,v in pan_result.items():
        print(f"{k} : {v}")


    aadhar_result= validate_documents(sample_aadhaar)

    for k,v in aadhar_result.items():
        print(f"{k} : {v}")    


