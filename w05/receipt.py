import csv
from datetime import datetime, timedelta

def read_dictionary(filename, key_column_index):

    products_dict = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        next(reader)

        for row in reader:
            if len(row) == 0:
                continue  
            key = row[key_column_index]
            products_dict[key] = row

    return products_dict


def main():
    try:
        STORE_NAME = "Inkom Emporium"
        TAX_RATE = 0.06

        products_dict = read_dictionary("products.csv", 0)

        total_items = 0
        subtotal = 0.0

        print(STORE_NAME)
        print()
        print("Requested Items")

        with open("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)

            for row in reader:
                if len(row) == 0:
                    continue

                prod_num = row[0]
                quantity = int(row[1])

                product_info = products_dict[prod_num]

                product_name = product_info[1]
                product_price = float(product_info[2])

                line_total = product_price * quantity

                print(f"{product_name}: {quantity} @ {product_price:.2f}")

                total_items += quantity
                subtotal += line_total

        print()

        sales_tax = subtotal * TAX_RATE
        total = subtotal + sales_tax

        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")
        print(f"Thank you for shopping at the {STORE_NAME}.")

        now = datetime.now()
        print(now.ctime())

        new_year = datetime(now.year + 1, 1, 1)
        days_until_new_year = (new_year.date() - now.date()).days
        print(f"New Years Sale starts in {days_until_new_year} day(s).")


        return_by = now + timedelta(days=30)
        return_by = return_by.replace(hour=21, minute=0, second=0, microsecond=0)
        print("Return by:", return_by.ctime())

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)

    except PermissionError as e:
        print("Error: permission denied when trying to read a file")
        print(e)

    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)


if __name__ == "__main__":
    main()
