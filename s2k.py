import xml.etree.ElementTree as ET
import argparse


def xml2csv(file: str = "default.xml"):
    tree = ET.parse(file)

    database = tree.find("Database")
    accounts = database.find("Accounts")
    logins = database.find("Logins")
    groups = database.find("Groups")

    id_group = {x.attrib["ID"]: x for x in groups}
    id_account = {x.attrib["ID"]: x for x in accounts}

    sourceid_login = {
        x.attrib["SourceLoginID"]: x
        for x in accounts.findall(".//Login")
    }

    for login in logins:
        account_login = sourceid_login.get(login.attrib.get("ID"))
        if account_login is None:
            continue

        account = id_account.get(account_login.attrib.get("ParentID"))
        if account is None:
            continue

        group_elem = id_group.get(account.attrib.get("ParentID"))

        group = (
            group_elem.attrib.get("Name")
            if group_elem is not None
            else ""
        )

        title = account.attrib.get("Name", "")

        username = (
            login.attrib.get("Name")
            or login.attrib.get("Username")
            or ""
        )

        password = (
            login.attrib.get("Password")
            or login.attrib.get("Pass")
            or ""
        )

        url = (
            account.attrib.get("Link")
            or account.attrib.get("URL")
            or ""
        )

        last_modified = login.attrib.get("ModifiedDate", "")
        created = login.attrib.get("CreatedDate", "")

        yield f"{group},{title},{username},{password},{url},{last_modified},{created}\n"


def main(xml_file, csv_file):
    with open(csv_file, "w", encoding="utf-8") as f:
        f.write("group,title,username,password,url,last_modified,created\n")
        f.writelines(xml2csv(xml_file))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Convert Sticky Password XML file to CSV file for KeePass"
    )

    parser.add_argument("input_file", nargs="?", default="default.xml")
    parser.add_argument("output_file", nargs="?", default="sticky.csv")

    args = parser.parse_args()
    main(args.input_file, args.output_file)
