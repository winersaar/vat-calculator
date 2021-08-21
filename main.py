import os
import vat_calculator

if __name__ == "__main__":
    file_path = os.environ.get("TRANSACTION_FILE", "./files/transaction3.json")
    try:
        vat = vat_calculator.calculate_mileage_eligibility(file_path)
        print("Calculation VAT: ", vat)
    except:
        print("Unhandled error occurred while trying to calculate VAT")