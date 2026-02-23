import config
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HOST = config.HOST
USERNAME = config.USERNAME
PASSWORD = config.PASSWORD


def parse_entities(response_json, entity_type):
    results = []
    data = response_json.get("data", [])

    for item in data:
        
        uuid = item.get("extId")
        name = item.get("name")

        if entity_type == "category":
            name = f"{item.get('key')}:{item.get('value')}"

        elif entity_type == "container":
            uuid = item.get("containerExtId")




        if entity_type == "pc":
        
            software_list = item.get("config", {}).get("clusterSoftwareMap", [])

            for software in software_list:
                if software.get("softwareType") == "PRISM_CENTRAL":
                    break
            else:
                continue
            
        elif entity_type == "pe":
        
            software_list = item.get("config", {}).get("clusterSoftwareMap", [])

            for software in software_list:
                if software.get("softwareType") == "NOS":
                    break
            else:
                continue

        results.append({
            "name": name,
            "uuid": uuid,
            "type": entity_type
        })

    return results


# containerss=list_containers(HOST,USERNAME, PASSWORD)
# #print(response_json)
# subnetss=list_subnets(HOST,USERNAME, PASSWORD)

# subnets_uuid=parse_entities(subnetss,"subnet")
# print(subnets_uuid)
# print("####################")
# containers_uuid=parse_entities(containerss,"container")
# print(containers_uuid)