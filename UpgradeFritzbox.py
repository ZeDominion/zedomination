import sys

def format_cpe_ids(cpe_ids):
    """
Format list voor Fritzbox upgrades in policy
    """
    formatted_ids = ["'{}'".format(cpe_id) for cpe_id in cpe_ids]
    query = "cpe.cpeid IN ({})".format(','.join(formatted_ids))
    return query

def main():
    if len(sys.argv) > 1:
        cpe_ids = sys.argv[1].replace(',', ' ').split()
        print(format_cpe_ids(cpe_ids))
    else:
        print("Paste the CPE IDs, then press Enter (or CTRL+D) :")
        user_input = sys.stdin.read().strip()
        cpe_ids = user_input.replace(',', ' ').replace('\n', ' ').split()
        print(format_cpe_ids(cpe_ids))

if __name__ == "__main__":
    main()