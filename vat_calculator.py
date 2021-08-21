from engine_type import VEHICLE_PETROL
from engine_type import FUEL_RATES

import json
import os

file_path = "files/transaction2.json"
file_path_true = "files/transaction3.json"

def calculate_mileage_eligibility(file_path):
   transaction = read_transaction(file_path)
   if not is_mileage(transaction):
      print("Transaction is not mileage. file_path=", file_path)
      return

   vat = calc_vat(transaction)
   return vat

def read_transaction (file_path):
   with open(file_path, encoding="utf-8") as jsonFile:
      transaction = json.load(jsonFile)
      return enrich_vehicle(transaction)

def is_mileage (transaction):
   return len(transaction["labels"]) == 1 and transaction["labels"][0].lower() == "mileage"

def calc_vat (transaction):
   #calculating total mileages
   total_mileage = sum([expense['expenseData']['mileage'] for expense in transaction["expenses"]])

   current_vehicle_rate = calc_vehicle_rate(transaction)
   if current_vehicle_rate is None:
      raise Exception("Vehicle is invalid")

   expense_actual_amount = total_mileage * current_vehicle_rate
   expense_approved_amount = transaction["expenseApprovedAmount"]

   if expense_actual_amount > expense_approved_amount:
      raise("The amount is higher than approved")

   return expense_actual_amount - (expense_actual_amount * (1.0/1.2))


def enrich_vehicle(transaction):
   size_in_cc = int(os.environ.get("VEHICLE_SIZE_IN_CC", 1500))
   vehicle_type = int(os.environ.get("VEHICLE_TYPE", VEHICLE_PETROL))

   transaction["vehicle"] = {"size_in_cc": size_in_cc, "type": vehicle_type}
   return transaction

def calc_vehicle_rate(transaction):
   engine_size = transaction["vehicle"]["size_in_cc"]
   engine_type = transaction["vehicle"]["type"]

   row_index = -1
   if engine_size <= 1400:
      row_index = 0
   elif engine_size <= 1600:
      row_index = 1
   elif engine_size >= 1401 and engine_size <= 2000:
      row_index = 2
   elif engine_size >= 1601 and engine_size <= 2000:
      row_index = 3
   elif engine_size > 2000:
      row_index = 4
   else:
      raise Exception("engine_size is not valid")

   return FUEL_RATES[row_index][engine_type]