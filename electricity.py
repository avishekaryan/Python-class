# WAP to calculate electricity bill using given units and rate per unit.


def calculate_bill() :
    try:
        # input units consumed 
        unit = float(input("Enter total units consumed : "))

        if unit<= 0 :
            print("Units can't be negative or zero.")
            return                                # Exiting the function if the input is invalid to prevent further calculations with invalid data.

        # initializing the variables              important to avoid bugs in the code
        energy_charge = 0
        service_charge = 0 
        total_bill = 0

        # Traffic rate and its structure (According to 2080/81 B.S. NEA rates)
        if unit <= 20 :                        # minimum charge is from 0 to 20 units
            energy_charge = unit * 4.0           
            service_charge = 50 
        elif unit <= 30 :                                 # 21 - 30 units 
            energy_charge = (20 *4.0) + (unit - 20)*6.5   # for 1st 20 its same rate then for remaining units its 6.5  
            service_charge = 75
        elif unit <= 50 :
            energy_charge = (20 *4.0) + (10 * 6.5) + (unit - 30)*8.0  # for 1st 20 its same rate then for next 10 units its 6.5 and for remaining units its 8.0
            service_charge = 75
        elif unit <= 150 :
            energy_charge = (20 * 4.0) + (10 * 6.5) + (20 * 8.0) + (unit - 50)*9.0 
            service_charge = 100 
        else :          # above 150 units 
            energy_charge = (20 * 4.0) + (10 * 6.5) + (20 * 8.0) + (100 * 9.0) + (unit - 150)*11.0 
            service_charge = 125

        
        # Total bill calculation
        total_bill = energy_charge + service_charge 

        # Display results
        print("\n--- Electricity Bill ---")
        print(f"Units Consumed : {unit}")
        print(f"Energy Charge : Rs. {energy_charge: .2f}")
        print(f"Service Charge : Rs. {service_charge: .2f}")
        print(f"Total Amount to Pay : Rs. {total_bill: .2f} ")


    except ValueError:
        print("Invalid input! Please enter numerical values.")

# Call the function to calculate the bill
calculate_bill()

