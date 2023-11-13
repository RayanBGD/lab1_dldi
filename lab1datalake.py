import os
from azure.storage.filedatalake import (
    DataLakeServiceClient,
    DataLakeDirectoryClient,
    FileSystemClient
)
from azure.identity import DefaultAzureCredential

class DataLake:
    
    # Access resources

    def get_service_client_account_key(self, account_name, account_key) -> DataLakeServiceClient:
        account_url = f"https://{account_name}.dfs.core.windows.net"
        service_client = DataLakeServiceClient(account_url, credential=account_key)

        return service_client

    # Create container

    def create_file_system(self, service_client: DataLakeServiceClient, file_system_name: str) -> FileSystemClient:
        file_system_client = service_client.create_file_system(file_system=file_system_name)

        return file_system_client

    # Create directory

    def create_directory(self, file_system_client: FileSystemClient, directory_name: str) -> DataLakeDirectoryClient:
        directory_client = file_system_client.create_directory(directory_name)

        return directory_client

    # Upload file

    def upload_file_to_directory(self, directory_client: DataLakeDirectoryClient, local_path: str, file_name: str):
        file_client = directory_client.get_file_client(file_name)

        with open(file=os.path.join(local_path, file_name), mode="rb") as data:
            file_client.upload_data(data, overwrite=True)

if __name__ == '__main__':
    objectA = DataLake()
    service_client = objectA.get_service_client_account_key("lab1dldi", "tQLlRCd/KmbaDOhqGESLHhbC4lwBl1ewYcM/oI3qpTFOuGhfcC5Ajr8WYm7X9dPQkFguUkFcpnHn+ASti8Xcig==")
    file_system = objectA.create_file_system(service_client, "testmichou")
    directory = objectA.create_directory(file_system, "lab1_push_google_drive")
    for filename in os.listdir("/home/michou/Documents/datas"):
        objectA.upload_file_to_directory(directory, "/home/michou/Documents/datas", filename)