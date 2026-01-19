import asyncio, httpx, os
from audiotool.project.v1.project_service_connect import  ProjectServiceClient
from audiotool.project.v1.project_service_pb2 import ListProjectsRequest

from audiotool.auth.v1.auth_service_connect import AuthServiceClient
from audiotool.auth.v1.auth_service_pb2 import GetWhoamiRequest
# This file contains an example on how to use the generated code to call a gRPC method.

# You don't have to use Python to do this. Read the README.md for instructions.


async def main():

    # Create a httpx client as transport for our grpc client
    async with httpx.AsyncClient(headers={
        # authorize using the PAT
        "Authorization": "Bearer " + os.getenv("AT_PAT"),
    }) as session:


        # Simple Whoami request: Create auth service
        auth = AuthServiceClient(
            address="https://rpc.audiotool.com",
            session=session,
        )

        # call whoami method
        response = await auth.get_whoami(
            GetWhoamiRequest()
        )

        # print response
        print("authorized as", response.whoami.user_name)

        # Create a client for our ProjectService
        client = ProjectServiceClient(
            address="https://rpc.audiotool.com",
            session=session,
        )

        # call "list_projects" gRPC method
        response = await client.list_projects(
            ListProjectsRequest()
        )


        print(f"{'Name:':<40}{'Update time:':<20}")
        print("-" * 60)
        # Pretty print the response
        for project in response.projects:
            name = project.display_name
            time = project.update_time.ToDatetime().strftime('%Y-%m-%d %H:%M:%S')
            print(f"{name:<40}{time:<20}")




if __name__ == "__main__":
    asyncio.run(main())