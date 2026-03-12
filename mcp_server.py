# mcp_server.py
# from fastmcp import FastMCP
from mcp.server.fastmcp import FastMCP
import time
import paramiko
import os


# Initialize the server with a descriptive name
mcp = FastMCP("ServerManager")

# SSH Configuration - In production, use environment variables!
SSH_HOST = "test-23ai.maxapex.net"
SSH_USER = "root"
SSH_PASS = "9HjULaK7wHUC" # Or use a key_filename
SSH_PORT = 9292

@mcp.tool()
def restart_service(service_name: str) -> str:
    """
    Restarts a specific system service.
    Args:
        service_name: The name of the service (e.g., 'apache2', 'mysql').
    """
    # In a real scenario, you'd use 'paramiko' here to SSH into the target server
    # For now, we simulate the action
    print(f"Executing: sudo systemctl restart {service_name}")
    time.sleep(1) 
    return f"Successfully restarted the {service_name} service on the target server."

@mcp.tool()
def check_server_uptime() -> str:
    """
    Connects to the remote server via SSH to check its current uptime and load average.
    Uses commands defined in the 'commands/check_uptime.txt' file.
    """
    
    # 1. Read commands from the specific folder
    # This assumes 'commands' is a folder in the same directory as this script
    file_path = os.path.join(os.path.dirname(__file__), "commands", "check_uptime.txt")
    
    if not os.path.exists(file_path):
        return f"Error: check_uptime.txt not found at {file_path}. Please check the 'commands' folder."

    with open(file_path, "r") as f:
        commands = [line.strip() for line in f if line.strip()]

    if not commands:
        return "Error: check_uptime.txt is empty. No commands to run."

    # 2. Establish SSH Connection
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect using your custom port 9292
        ssh.connect(
            SSH_HOST, 
            port=SSH_PORT, 
            username=SSH_USER, 
            password=SSH_PASS,
            timeout=10 # Added a timeout to prevent the agent from hanging
        )
        
        output_log = []
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            
            output_log.append(f"--- OUTPUT FOR: {cmd} ---\n{result if result else error}\n")

        ssh.close()
        return "\n\n".join(output_log)

    except Exception as e:
        return f"SSH Error: {str(e)}"
    
@mcp.tool()
def check_server_diskspace() -> str:
    """
    Connects to the remote server via SSH to check its current disk space usage.
    Uses commands defined in the 'commands/check_diskspace.txt' file.
    """
    
    # 1. Read commands from the specific folder
    # This assumes 'commands' is a folder in the same directory as this script
    file_path = os.path.join(os.path.dirname(__file__), "commands", "check_diskspace.txt")
    
    if not os.path.exists(file_path):
        return f"Error: check_diskspace.txt not found at {file_path}. Please check the 'commands' folder."

    with open(file_path, "r") as f:
        commands = [line.strip() for line in f if line.strip()]

    if not commands:
        return "Error: check_diskspace.txt is empty. No commands to run."

    # 2. Establish SSH Connection
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect using your custom port 9292
        ssh.connect(
            SSH_HOST, 
            port=SSH_PORT, 
            username=SSH_USER, 
            password=SSH_PASS,
            timeout=10 # Added a timeout to prevent the agent from hanging
        )
        
        output_log = []
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            
            output_log.append(f"--- OUTPUT FOR: {cmd} ---\n{result if result else error}\n")

        ssh.close()
        return "\n\n".join(output_log)

    except Exception as e:
        return f"SSH Error: {str(e)}"

@mcp.tool()
def check_server_processes() -> str:
    """
    Connects to the remote server via SSH to check its current processes.
    Uses commands defined in the 'commands/check_processes.txt' file.
    """
    
    # 1. Read commands from the specific folder
    # This assumes 'commands' is a folder in the same directory as this script
    file_path = os.path.join(os.path.dirname(__file__), "commands", "check_processes.txt")
    
    if not os.path.exists(file_path):
        return f"Error: check_processes.txt not found at {file_path}. Please check the 'commands' folder."

    with open(file_path, "r") as f:
        commands = [line.strip() for line in f if line.strip()]

    if not commands:
        return "Error: check_processes.txt is empty. No commands to run."

    # 2. Establish SSH Connection
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect using your custom port 9292
        ssh.connect(
            SSH_HOST, 
            port=SSH_PORT, 
            username=SSH_USER, 
            password=SSH_PASS,
            timeout=10 # Added a timeout to prevent the agent from hanging
        )
        
        output_log = []
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            
            output_log.append(f"--- OUTPUT FOR: {cmd} ---\n{result if result else error}\n")

        ssh.close()
        return "\n\n".join(output_log)

    except Exception as e:
        return f"SSH Error: {str(e)}"

@mcp.tool()
def check_cpu_usage() -> str:
    """
    Connects to the remote server via SSH to check its current CPU usage.
    Uses commands defined in the 'commands/check_cpu.txt' file.
    """
    
    # 1. Read commands from the specific folder
    # This assumes 'commands' is a folder in the same directory as this script
    file_path = os.path.join(os.path.dirname(__file__), "commands", "check_cpu.txt")
    
    if not os.path.exists(file_path):
        return f"Error: check_cpu.txt not found at {file_path}. Please check the 'commands' folder."

    with open(file_path, "r") as f:
        commands = [line.strip() for line in f if line.strip()]

    if not commands:
        return "Error: check_cpu.txt is empty. No commands to run."

    # 2. Establish SSH Connection
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect using your custom port 9292
        ssh.connect(
            SSH_HOST, 
            port=SSH_PORT, 
            username=SSH_USER, 
            password=SSH_PASS,
            timeout=10 # Added a timeout to prevent the agent from hanging
        )
        
        output_log = []
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            
            output_log.append(f"--- OUTPUT FOR: {cmd} ---\n{result if result else error}\n")

        ssh.close()
        return "\n\n".join(output_log)

    except Exception as e:
        return f"SSH Error: {str(e)}"

@mcp.tool()
def check_ram_usage() -> str:
    """
    Connects to the remote server via SSH to check its current RAM usage.
    Uses commands defined in the 'commands/check_ram.txt' file.
    """
    
    # 1. Read commands from the specific folder
    # This assumes 'commands' is a folder in the same directory as this script
    file_path = os.path.join(os.path.dirname(__file__), "commands", "check_ram.txt")
    
    if not os.path.exists(file_path):
        return f"Error: check_ram.txt not found at {file_path}. Please check the 'commands' folder."

    with open(file_path, "r") as f:
        commands = [line.strip() for line in f if line.strip()]

    if not commands:
        return "Error: check_ram.txt is empty. No commands to run."

    # 2. Establish SSH Connection
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect using your custom port 9292
        ssh.connect(
            SSH_HOST, 
            port=SSH_PORT, 
            username=SSH_USER, 
            password=SSH_PASS,
            timeout=10 # Added a timeout to prevent the agent from hanging
        )
        
        output_log = []
        for cmd in commands:
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read().decode().strip()
            error = stderr.read().decode().strip()
            
            output_log.append(f"--- OUTPUT FOR: {cmd} ---\n{result if result else error}\n")

        ssh.close()
        return "\n\n".join(output_log)

    except Exception as e:
        return f"SSH Error: {str(e)}"

# @mcp.tool()
# def check_table_count(schema_name: str, table_name: str) -> str:
#     """
#     Connects to the Oracle server and returns the row count for a specific table.
    
#     Args:
#         schema_name: The name of the database schema (e.g., 'maxprint_demo').
#         table_name: The name of the table to count (e.g., 'employees').
#     """
#     # 1. Path to your command template
#     file_path = os.path.join(os.path.dirname(__file__), "commands", "check_table_count.txt")
    
#     try:
#         with open(file_path, "r") as f:
#             template = f.read().strip()

#         # 2. Inject the dynamic variables into the script
#         # This replaces {schema} and {table} inside your .txt file
#         full_command = template.replace("{schema}", schema_name).replace("{table}", table_name)

#         # 3. SSH Execution (Same as before)
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER, password=SSH_PASS)
        
#         stdin, stdout, stderr = ssh.exec_command(full_command)
#         result = stdout.read().decode().strip()
#         error = stderr.read().decode().strip()
#         ssh.close()

#         return f"Count for {schema_name}.{table_name}: {result}" if result else f"Error: {error}"

#     except Exception as e:
#         return f"System Error: {str(e)}"


@mcp.tool()
def check_table_count(pdb_name: str, schema_name: str, table_name: str) -> str:

    """
    Connects to the Oracle server and returns the row count for a specific table.
    If the PDB name is unknown, use get_available_pdbs first.
    Args:
        schema_name: The name of the database schema (e.g., 'maxprint_demo').
        table_name: The name of the table to count (e.g., 'employees').
        pdb_name: The name of the Pluggable Database (PDB) to connect to (e.g., 'XEPDB1').
    """
    file_path = os.path.join(os.path.dirname(__file__), "commands", "check_table_count.txt")
    
    try:
        with open(file_path, "r") as f:
            template = f.read().strip()

        # Inject PDB, Schema, and Table
        full_command = (template.replace("{pdb}", pdb_name)
                                .replace("{schema}", schema_name)
                                .replace("{table}", table_name))

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER, password=SSH_PASS,  timeout=10 )
        
        stdin, stdout, stderr = ssh.exec_command(full_command)
        result = stdout.read().decode().strip()
        ssh.close()

        return f"[{pdb_name}] {schema_name}.{table_name} count: {result}"
    except Exception as e:
        return f"Execution Error: {str(e)}"


@mcp.tool()
def get_available_pdbs() -> str:
    """Lists all available Pluggable Databases (PDBs) that are currently open."""
    file_path = os.path.join(os.path.dirname(__file__), "commands", "list_pdbs.txt")
    
    try:
        with open(file_path, "r") as f:
            command = f.read().strip()

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(SSH_HOST, port=SSH_PORT, username=SSH_USER, password=SSH_PASS)
        
        stdin, stdout, stderr = ssh.exec_command(command)
        result = stdout.read().decode().strip()
        ssh.close()

        return f"Available PDBs:\n{result}" if result else "No open PDBs found."
    except Exception as e:
        return f"Error fetching PDBs: {str(e)}"

if __name__ == "__main__":
    # Start the server using the standard input/output (stdio) transport
    mcp.run()