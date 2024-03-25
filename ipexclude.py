from ipaddress import ip_network, ip_address

def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().splitlines()


def write_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write('\n'.join(data))


def filter_addresses(ip_list, cidr_list):
    filtered_ips = []
    for ip_str in ip_list:
        try:
            ip_obj = ip_address(ip_str)
            if all(ip_obj not in ip_network(cidr, strict=False) for cidr in cidr_list):
                filtered_ips.append(ip_str)
        except ValueError:
            # Handle invalid IP address format
            pass
    return filtered_ips

def main():
    ip_list_path = 'C:\\Tools\\scripts\\uniqueIPtrimmedoct1-jan10.txt'
    cidr_list_path = 'C:\\Tools\\scripts\\awsALLipcidr.txt'
    output_file_path = 'C:\\Tools\\scripts\\trimmed.txt'

    ip_list = read_file(ip_list_path)
    cidr_list = read_file(cidr_list_path)
    filtered_ips = filter_addresses(ip_list, cidr_list)
    write_file(output_file_path, filtered_ips)
main()