# MySQL and phpMyAdmin Docker Compose Setup

This Docker Compose setup runs MySQL and phpMyAdmin using Docker containers. It includes MySQL for database management and phpMyAdmin for a web-based database interface.

### Setup

1. **Create a `.env` file**

   In the root directory, create a `.env` file with the following environment variables:

   ```dotenv
   MYSQL_ROOT_PASSWORD=pass
   MYSQL_DATABASE=ecommerce
   MYSQL_USER=pass
   MYSQL_PASSWORD=pass
   MYSQL_AUTHENTICATION_PLUGIN=mysql_native_password
   PMA_ARBITRARY=0
   PMA_HOST=mysql
   ```

   Adjust these values according to your configuration.

2. **Start Services**

   Run the following command to start the services:

   ```bash
   docker-compose up -d
   ```

   This command will start MySQL and phpMyAdmin in detached mode.

### Accessing Services

- **phpMyAdmin**: [http://localhost:8000](http://localhost:8000)
  - Use phpMyAdmin to manage your MySQL databases and perform SQL queries.

### SQL Script

The `init.sql` script initializes the MySQL database with sample data. It does the following:

- **Creates** the `ecommerce` database.
- **Creates** the `category`, `seller`, and `product` tables.
- **Inserts** sample data into these tables.

**Location**: `./sql-scripts/init.sql`

**If `init.sql` doesn't run automatically:**

   1. Enter the MySQL container:
   
      ```bash
      docker exec -it mysql bash
      ```

   2. Execute the SQL script manually:

      ```bash
      mysql -u root -p ecommerce < /docker-entrypoint-initdb.d/init.sql
      ```

### Docker Compose Configuration

- **Networks**:
  - **bi-project-network**: The Docker network used by both services.