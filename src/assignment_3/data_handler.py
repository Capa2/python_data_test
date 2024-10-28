
from contextlib import contextmanager
from utils.logger import get_logger
import re
import csv

LOGGER = get_logger("assignment_2_errors")

def get_validated_customer(customer):
    fields = [field.strip() for field in customer.split(',')]

    customer_id = name = email = purchase_amount = None

    for field in fields:
        if field.isdigit() and customer_id is None:
            customer_id = field

        elif re.match(r'^\d+(\.\d+)?$', field) and purchase_amount is None:
            purchase_amount = field

        elif re.match(r'[\w\.-]+@[\w\.-]+\.\w+', field) and email is None:
            email = field

        elif re.match(r'[A-Za-z\s]{2,}', field) and name is None:
            name = field

    if (all(field is None for field in [customer_id, name, email, purchase_amount])):
        LOGGER.error(f"No customer data found in entry: {customer}")
        return None
    
    issues = []
    if not customer_id:
        issues.append("ID missing or invalid")
    if not name:
        issues.append("Name missing or invalid")
    if not email:
        issues.append("Email missing or invalid")
    if not purchase_amount:
        issues.append("Purchase Amount missing or invalid")

    if issues:
        LOGGER.error(f"Customer data invalid: {', '.join(issues)}. Entry: {customer}")
        return None

    return (customer_id, name, email, purchase_amount)


@contextmanager
def safe_open(path, mode='r', newline=None):
    action = 'read' if mode == 'r' else 'write to' if mode == 'w' else 'append' if mode == 'a' else 'access'
    file = None
    try:
        file = open(path, mode, newline=newline)
        yield file
    except FileNotFoundError:
       LOGGER.error(f"File {path} was not found.")
       raise
    except PermissionError:
        action = 'read' if mode == 'r' else 'write to' if mode == 'w' else 'append' if mode == 'a' else 'access'
        LOGGER.error(f"Permission denied to {action} file: {path}.")
        raise
    except ValueError:
        LOGGER.error(f"Invalid file mode: {mode}. Valid options are 'r', 'w' and 'a'")
        raise
    except IOError as e:  # Handle any general I/O error (writing, disk issues, etc.)
        LOGGER.error(f"I/O error occurred while trying to {action} {path}: {e}")
        raise
    except Exception as e:
        LOGGER.error(f"An unexpected error occurred: {e}")
        raise
    finally:
        if file is not None:
            file.close()

def safe_write(path, data):
    with safe_open(path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Customer ID", "Name", "Email", "Purchase Amount"])
        for customer_id, name, email, purchaseamount in data:
            writer.writerow([customer_id, email, purchaseamount])


def main():
    validated_customers = []
    print("Processing data...")
    with safe_open("src/data/assignment_3_source_data.csv") as file:
        for customer in file:
            validated_customer = get_validated_customer(customer)
            if validated_customer:
                validated_customers.append(validated_customer)
    
    if validated_customers:
        print("Writing data...")
        safe_write("src/data/assignment_3_processed_data.csv", validated_customers)
        print("Writing data complete")
    else:
        LOGGER.error("No valid customer data to write")
    