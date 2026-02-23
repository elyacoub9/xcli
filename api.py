import requests
import config

# username=config.USERNAME
# password=config.PASSWORD
# host=config.HOST


def list_vms(host, username, password, limit=50):
    url = f"https://{host}:9440/api/vmm/v4.2/ahv/config/vms?$limit={limit}"
    
    response = requests.get(
        url,
        auth=(username, password),
        headers={"Accept": "application/json"},
        verify=False
    )
    
    return response.json()


####

def list_images(host, username, password, limit=50):
    url = f"https://{host}:9440/api/vmm/v4.2/content/images?$limit={limit}"
    
    response = requests.get(
        url,
        auth=(username, password),
        headers={"Accept": "application/json"},
        verify=False
    )
    
    return response.json()


####
def list_subnets(host, username, password, limit=50):
    url = f"https://{host}:9440/api/networking/v4.2/config/subnets?$limit={limit}"
    
    response = requests.get(
        url,
        auth=(username, password),
        headers={"Accept": "application/json"},
        verify=False
    )
    
    return response.json()

#### project api to be determined (i can't find the correct path)
# def list_projects(host, username, password, limit=50):
#     url = f"https://{host}:9440/api////projects?$limit={limit}"
    
#     response = requests.get(
#         url,
#         auth=(username, password),
#         headers={"Accept": "application/json"},
#         verify=False
#     )
    
#     return response.json()

####

def list_categories(host, username, password, limit=50):
    url = f"https://{host}:9440/api/prism/v4.2/config/categories?$limit={limit}"
    
    response = requests.get(
        url,
        auth=(username, password),
        headers={"Accept": "application/json"},
        verify=False
    )
    
    return response.json()


####
def list_containers(host, username, password, limit=50):
    url = f"https://{host}:9440/api/clustermgmt/v4.2/config/storage-containers?$limit={limit}"
    
    response = requests.get(
        url,
        auth=(username, password),
        headers={"Accept": "application/json"},
        verify=False
    )
    
    return response.json()


####(to be determined if keep this or use the one after it (list both pe/pc clusters))
def list_pcs(host, username, password, limit=50):
    url = f"https://{host}:9440/api/prism/v4.2/config/domain-managers?$limit={limit}"
    
    response = requests.get(
        url,
        auth=(username, password),
        headers={"Accept": "application/json"},
        verify=False
    )
    return response.json()

####
def list_clusters(host, username, password, limit=50):
    url = f"https://{host}:9440/api/clustermgmt/v4.2/config/clusters?$limit={limit}"
    
    response = requests.get(
        url,
        auth=(username, password),
        headers={"Accept": "application/json"},
        verify=False
    )
    return response.json()