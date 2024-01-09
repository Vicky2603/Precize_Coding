import json, os

dictionary_records = {"name":[], "address":[], "city":[], "country":[], "pincode":[], "SAT_Score":[], "status":[]}
list_name, list_address, list_city, list_country, list_pincode, list_sat_score, list_status = [], [], [], [], [], [], []

while True:
    option = int(input("""Please choose one option: 
    1. Insert data
    2. View all data
    3. Get rank
    4. Update score
    5. Delete one record
    6. Put the inserted data in json format in a file.
    7. To Exit.
    """))
    if option == 1:
        print("Insert data: ")
        name = input("Name (Unique Identifier): ")
        address = input("Address: ")
        city = input("City: ")
        country = input("Country: ")
        pincode = input("Pincode: ")
        SAT_Score = float(input("SAT Score: "))
        if SAT_Score > 30:
            print("Pass")
            status = "Pass"
        else:
            print("Fail")
            status = "Fail"
            
        list_name.append(name)
        list_address.append(address)
        list_city.append(city)
        list_country.append(country)
        list_pincode.append(pincode)
        list_sat_score.append(SAT_Score)
        list_status.append(status)
        
        dictionary_records["name"] = list_name
        dictionary_records["address"] = list_address
        dictionary_records["city"] = list_city
        dictionary_records["country"] = list_country
        dictionary_records["pincode"] = list_pincode
        dictionary_records["SAT_Score"] = list_sat_score
        dictionary_records["status"] = list_status
        
    elif option == 2:    
        print(json.dumps(dictionary_records))
        
    elif option == 3:    # Not clear about this point(Get Rank). Decided to show the ranks based on index.
        get_rank_by_name = input("Get rank: ")
        for i in range(len(dictionary_records["name"])):
            if dictionary_records["name"][i] == get_rank_by_name:
                print(f"Rank is: {i+1}")
    
    elif option == 4:
        print("Update Score: ")
        user_exists = input("Please enter the name: ")
        for i in range(len(dictionary_records["name"])):
            if dictionary_records["name"][i] == user_exists:
                sat_updated_score = float(input("Please enter the updated score: "))
                dictionary_records["SAT_Score"][i] = sat_updated_score
                print("Score updated!")
                break
        else:
            print("User not found.")
    elif option == 5:
        dlt_name = input("Please enter the name of the user to be deleted: ")
        for i in range(len(dictionary_records["name"])):
            if dictionary_records["name"][i] == dlt_name:
                del dictionary_records["name"][i]
                del dictionary_records["address"][i]
                del dictionary_records["city"][i]
                del dictionary_records["country"][i]
                del dictionary_records["pincode"][i]
                del dictionary_records["SAT_Score"][i]
                print("User Deleted.")
                break
        else:
            print("User does not exists.")
    elif option == 6:
        print("6. Put the inserted data in json format in a file.")
        with open("Json_Data_File.json", "w") as outfile:
            json.dump(dictionary_records, outfile)
        print("Done, Please check the file(Json_Data_File) in this location -> ", os.getcwd())

    elif option == 7:
        print("Exited.")
        break
    else:
        print("Please, select a valid option.")
    print("--"*50)    