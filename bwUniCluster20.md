## 1 Run a UM-Bridge model on the bwUniCluster2.0
In this course we are using the [bwUniCluster2.0](https://wiki.bwhpc.de/e/BwUniCluster2.0).
To access this HPC follow the instruction for the [registration](https://wiki.bwhpc.de/e/Registration/bwUniCluster).

To set up UM-Bridge on the HPC log in to the HPC and follow the instructions from the [UM-Bridge Documentation](https://um-bridge-benchmarks.readthedocs.io/en/docs/umbridge/hpc.html) on HPCs.

To run a model on the bwUniCluster2.0 it must be put into a container. You can follow the instructions below to run your model on the HPC UM-Bridge setup. 

1. **UM-Bridge server as a Python script:** First you have to have to transfere your UM-Bridge server into a Python script (.py). In the script you can loos the first two lines of code:
   ```
   import nest_asyncio
   nest_asyncio.apply()
   ```
   those are only necessary in notebooks.

   On the botom line of your server you need to specify the port as follows: ```umbridge.serve_models([model], int(os.environ.get("PORT", 4242)))```.
3. **Install Docker:** Go to [Docker.com](https://www.docker.com/) and install Docker on your local machine.
4. **Sign up to Docker Hub:** Go to [Docker Hub](https://hub.docker.com/) and create an account.
5. **Write a Dockerfile:** To create a Docker container you need to write a Dockerfile and place it into the folder next to your Python script.
6. **Build the Docker image:** ```docker build -t <container_name> .```
7. **Run the Docker container:** To finally run your UM-Bridge server from the Docker container do: ```docker run -it -p 4242:4242 <container_name>```
8. **Upload the container to Docker Hub**
   
   7.1 **Tag the Docker image:** ```docker tag <container_name> <yourusername>/<container_name>:latest```
   
   7.2 **Log in to Docker Hub:** ```docker login```
   
   7.3 **Push the image to Docker Hub:** ```docker push <yourusername>/<container_name>:latest```
   
   7.4 **Verify the upload:** ```docker run -it -p 4242:4242 <yourusername>/<container_name>```
   
8. **Upload the container to the HPC**
    
   8.1 **Log in to bwUniCluster2.0:** ```ssh <username>@bwunicluster.scc.kit.edu```

   
   8.2 **Import the container image with singularity:** ```singularity build <container_name>.sif docker://<yourusername>/<container_name>```
   
   8.3 **Start the container with singularity:** ```singularity run --writable-tmpfs --pwd / <container_name>.sif```
   In this command, ```--pwd /``` sets the working directory inside the container. If your Dockerfile specifies a different working directory, you must replace ```/``` with that path to match the configured directory.
   
10. **Edit job.sh:** Go to the job.sh file in your UM-Bridge HPC setup and add the following line: ```singularity run --writable-tmpfs --pwd / <container_name>.sif``` Again make sure that you set the correct working directory.
11. **Run the load-balancer:** ```./load-balancer```
12. **Create a tunnel from your local machine to the HPC:** ```ssh <username>@bwunicluster.scc.kit.edu -N -f -L 4242:localhost:4242```
13. **Connect your UM-Bridge client through the tunnel** by simply running the client on your local machine on port 4242.
