import json

from company_master.authorized_cap import auth_data
from company_master.company_register_by_year import sort_company_data
from company_master.business_activity import sort_business_name_data
from company_master.stacked_bar_plot\
    import sort_by_year_store_businessname_list


if __name__ == "__main__":

    data = {
        "authoried_cap": auth_data(),
        "company_register": sort_company_data(),
        "number_of_company": sort_business_name_data(),
        "stack_result": sort_by_year_store_businessname_list()
    }

    json_object = json.dumps(data, indent=4)

    with open("public/data.json", "w") as outfile:
        outfile.write(json_object)
