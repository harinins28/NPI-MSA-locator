from fastapi import FastAPI
import pandas as pd
import requests
import json

app = FastAPI()

# Load dataset with correct data types
file_path = r"C:\Users\harin\OneDrive\Desktop\VIV\merged_data.csv"
df = pd.read_csv(file_path, dtype={"msa": str, "zip": str, "county_code": str})

@app.get("/get_npi/{msa}")
def get_npi(msa: str, max_zips: int = 10):
    """
    Fetch NPI data for a given MSA.
    
    Args:
        msa (str): The MSA code.
        max_zips (int): Limit the number of ZIP codes processed (default: 10).
    
    Returns:
        dict: Grouped provider data by practice address.
    """

    # Step 1: Filter dataset by MSA
    msa_df = df[df["msa"] == msa]

    # Step 2: Get unique ZIP codes and limit processing
    zip_codes = msa_df["zip"].dropna().astype(str).unique()[:max_zips]  # Limit number of ZIPs

    npi_data = []

    # Step 3: Search NPI API for each ZIP code
    for zip_code in zip_codes:
        url = f"https://npiregistry.cms.hhs.gov/api/?version=2.1&postal_code={zip_code}&enumeration_type=NPI-1"
        response = requests.get(url)

        if response.status_code == 200:
            results = response.json().get("results", [])

            for res in results:
                if not res:  # Skip empty results
                    continue

                npi_number = res.get("number")

                # Query NPI details using NPI number
                details_url = f"https://npiregistry.cms.hhs.gov/api/?version=2.1&number={npi_number}"
                details_response = requests.get(details_url)

                if details_response.status_code == 200:
                    details_data = details_response.json().get("results", [{}])[0]
                    practice_address = details_data.get("addresses", [{}])[0].get("address_1", "Unknown")
                else:
                    practice_address = "Unknown"

                # Append provider data
                npi_data.append({
                    "NPI": npi_number,
                    "Name": f"{res.get('basic', {}).get('first_name', '')} {res.get('basic', {}).get('last_name', '')}".strip(),
                    "Specialty": res.get("taxonomy", [{}])[0].get("desc", "Unknown"),
                    "Primary_Practice_Address": practice_address,
                    "City": res.get("addresses", [{}])[0].get("city", "Unknown"),
                    "State": res.get("addresses", [{}])[0].get("state", "Unknown"),
                    "ZIP": zip_code
                })

    # Step 4: Group providers by address
    grouped_data = {}
    npi_locations = {}

    for provider in npi_data:
        address = provider.get("Primary_Practice_Address", "Unknown")
        npi_number = provider.get("NPI", "Unknown")

        # Group by address
        if address in grouped_data:
            grouped_data[address].append(provider)
        else:
            grouped_data[address] = [provider]

        # Track all locations where an NPI appears
        if npi_number in npi_locations:
            npi_locations[npi_number].add(address)
        else:
            npi_locations[npi_number] = {address}

    # Convert NPI locations to a serializable format (list instead of set)
    npi_locations = {npi: list(locations) for npi, locations in npi_locations.items()}

    # Step 5: Save the data to JSON files
    with open("grouped_npi.json", "w") as f:
        json.dump(grouped_data, f, indent=4)

    with open("npi_locations.json", "w") as f:
        json.dump(npi_locations, f, indent=4)

    return {
        "grouped_npi": grouped_data,
        "npi_locations": npi_locations
    }
