from .validation.pan_validation import validate_pan_pipeline
from .validation.aadhar_validation import validate_aadhar_pipeline
from .document_detector import detect_doc_type
from .confidence_engine import calculate_confidence
from .ocr_engine import extract_text_from_img
import os

def validate_document_from_img(img_path : str):

    ocr_text = extract_text_from_img(img_path)

    if not ocr_text.strip():
        return{
            "document_type": "UNKNOWN",
            "final_decision": "REJECT",
            "reason": "OCR failed or empty text"
        }
    
    print("OCR Text is: ", ocr_text)

    print("Running Validation Pipeline")
    result = validate_documents(ocr_text)

    return result



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
        result= {
            "document_type" : "UNKNOWN",
            "decision" : "REJECT",
            "reason" : "Unrecognizable Document Provided"
        }   


    result = calculate_confidence(result)

    return result


if __name__ == "__main__":

    # sample_pan = """
    # INCOME TAX DEPARTMENT

    # Name: TAMMY BELTRAN
    # DOB: 18/11/1969
    # PAN: GHDOA8008B
    # """

    # sample_aadhaar = """
    # GOVERNMENT OF INDIA

    # Name: RA
    # DOB: 21/05/1998


    # Address:
    # 22 MG Road
    # Bangalore
    # Karnataka
    # """


    # pan_result= validate_documents(sample_pan)

    # for k,v in pan_result.items():
    #     print(f"{k} : {v}")


    # aadhar_result = validate_documents(sample_aadhaar)

    # for k,v in aadhar_result.items():
    #     print(f"{k} : {v}")    


    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    img_path = os.path.join(BASE_DIR, "data", "processed", "pan", "pan_0.png")
    result = validate_document_from_img(img_path)

    print("===============================")

    for k,v in result.items():
        print(f"{k} : {v}")