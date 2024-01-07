# Three-Server Web Infrastructure Design
[!1-distributed_web_infrastructure](1-distributed_web_infrastructure.jpg)
## Components:

1. **Server 1 (Primary):**
   - Hosting the primary instance of the application server.

2. **Server 2 (Replica):**
   - Hosting a replica instance of the application server.

3. **Server 3 (Load Balancer):**
   - HAProxy is configured as the load balancer, distributing incoming traffic between Server 1 and Server 2.

4. **Server 4 ():**
   - Another replica of the primary server (Master-Slave) cluster.

5. **Web Server (Nginx):**
   - Nginx is responsible for handling incoming HTTP requests, serving static content directly, and forwarding dynamic content requests to the application servers.

6. **Application Server:**
   - The application server, where your codebase resides. It processes requests from the web server, interacts with the database, and generates the appropriate responses.

7. **Application Files (Code Base):**
   - The codebase for the website resides on both Server 1 and Server 2, allowing for redundancy and load distribution.

8. **Database (MySQL Primary-Replica Cluster):**
   - MySQL is set up as a Primary-Replica (Master-Slave) cluster between Server 1 (Primary) and Server 2 (Replica).

## Explanation:

### Load Balancer (HAProxy):

- **Why:** To distribute incoming traffic, improve redundancy, handle increased loads, and provide fault tolerance.
- **Distribution Algorithm:** Round Robin (simple and effective for distributing traffic equally among servers).
- **Active-Active or Active-Passive:** Active-Active (both Server 1 and Server 2 actively handle incoming requests).

### Primary-Replica MySQL Cluster:

- **How it works:** The Primary (Master) node handles write operations, making changes to the database. The Replica (Slave) node mirrors the data from the Primary node and can handle read operations, distributing the load.
- **Difference:**
  - *Primary Node:* Handles write operations, making changes to the database.
  - *Replica Node:* Mirrors the data from the Primary node and can handle read operations, distributing the load.

## Issues with this Infrastructure:

1. **Single Points of Failure (SPOF):**
   - The Load Balancer (HAProxy) itself can become a potential single point of failure. Introducing redundancy for the load balancer and other critical components would help mitigate this.

2. **Security Issues:**
   - Lack of firewall protection poses security risks. Implementing firewalls, securing communication with HTTPS, and applying other security measures are essential.

3. **No Monitoring:**
   - Lack of monitoring tools makes it challenging to detect and address performance issues or potential failures promptly. Implementing monitoring solutions is crucial for maintaining a healthy infrastructure.
