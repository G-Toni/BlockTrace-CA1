from web3 import Web3
import json
import os

# --------------------------------
# BLOCKTRACE CONFIGURATION
# --------------------------------

GANACHE_URL = "http://127.0.0.1:8545"

CONTRACT_ADDRESS = "0x595c8fF1C8a49836B3EFEcdDfBdd3F8aEb26b0d8"

# Connect to Ganache
web3 = Web3(Web3.HTTPProvider(GANACHE_URL))

print("================================")
print("       BLOCKTRACE SYSTEM")
print("================================")

if not web3.is_connected():
    print("Failed to connect to Ganache.")
    exit()

print("Connected to Ganache successfully!")
print("Chain ID:", web3.eth.chain_id)
print("Latest Block:", web3.eth.block_number)

# --------------------------------
# LOAD SMART CONTRACT ABI
# --------------------------------

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

abi_path = os.path.join(
    base_dir,
    "contracts",
    "FoodTraceabilityABI.json"
)

with open(abi_path, "r") as file:
    contract_abi = json.load(file)

# --------------------------------
# CONNECT TO SMART CONTRACT
# --------------------------------

contract = web3.eth.contract(
    address=Web3.to_checksum_address(CONTRACT_ADDRESS),
    abi=contract_abi
)

print("Contract connected successfully!")
print("Contract Address:", CONTRACT_ADDRESS)

# --------------------------------
# READ BLOCKCHAIN DATA
# --------------------------------

product_count = contract.functions.productCount().call()

print("Number of products:", product_count)


# --------------------------------
# REGISTER A NEW PRODUCT
# --------------------------------

if product_count == 0:

    farmer = web3.eth.accounts[0]

    print("\nRegistering new product...")
    print("Farmer:", farmer)

    transaction_hash = contract.functions.registerProduct(
        "Organic Coffee",
        "Brazil"
    ).transact({
        "from": farmer
    })

    receipt = web3.eth.wait_for_transaction_receipt(
        transaction_hash
    )

    print("Product registered successfully!")
    print("Transaction Hash:", transaction_hash.hex())
    print("Block Number:", receipt.blockNumber)

else:
    print("\nProduct already registered.")


# --------------------------------
# DISPLAY PRODUCT INFORMATION
# --------------------------------

product = contract.functions.getProduct(1).call()

print("\n================================")
print("       PRODUCT DETAILS")
print("================================")
print("Product ID:", product[0])
print("Name:", product[1])
print("Origin:", product[2])
print("Current Owner:", product[3])
print("Status:", product[4])
print("Timestamp:", product[5])


# --------------------------------
# UPDATE PRODUCT STATUS
# --------------------------------

if product[4] == "Registered":

    farmer = web3.eth.accounts[0]

    print("\nUpdating product status to Harvested...")

    transaction_hash = contract.functions.updateStatus(
        1,
        "Harvested"
    ).transact({
        "from": farmer
    })

    receipt = web3.eth.wait_for_transaction_receipt(
        transaction_hash
    )

    print("Status updated successfully!")
    print("Transaction Hash:", transaction_hash.hex())
    print("Block Number:", receipt.blockNumber)

    # Read the product again after the update
    updated_product = contract.functions.getProduct(1).call()

    print("\nNew Status:", updated_product[4])

else:
    print("\nProduct status is already:", product[4])


# --------------------------------
# TRANSFER PRODUCT TO DISTRIBUTOR
# --------------------------------

farmer = web3.eth.accounts[0]
distributor = web3.eth.accounts[1]

current_product = contract.functions.getProduct(1).call()

if current_product[3].lower() == farmer.lower():

    print("\nTransferring product to Distributor...")
    print("Farmer:", farmer)
    print("Distributor:", distributor)

    transaction_hash = contract.functions.transferProduct(
        1,
        distributor
    ).transact({
        "from": farmer
    })

    receipt = web3.eth.wait_for_transaction_receipt(
        transaction_hash
    )

    print("Product transferred successfully!")
    print("Transaction Hash:", transaction_hash.hex())
    print("Block Number:", receipt.blockNumber)

    transferred_product = contract.functions.getProduct(1).call()

    print("\nNew Owner:", transferred_product[3])

else:
    print("\nProduct has already been transferred.")
    print("Current Owner:", current_product[3])


# --------------------------------
# DISTRIBUTOR UPDATES STATUS
# --------------------------------

distributor = web3.eth.accounts[1]

current_product = contract.functions.getProduct(1).call()

if (
    current_product[3].lower() == distributor.lower()
    and current_product[4] == "Harvested"
):

    print("\nDistributor updating status to In Transit...")

    transaction_hash = contract.functions.updateStatus(
        1,
        "In Transit"
    ).transact({
        "from": distributor
    })

    receipt = web3.eth.wait_for_transaction_receipt(
        transaction_hash
    )

    print("Status updated successfully!")
    print("Transaction Hash:", transaction_hash.hex())
    print("Block Number:", receipt.blockNumber)

    updated_product = contract.functions.getProduct(1).call()

    print("New Status:", updated_product[4])

else:
    print("\nDistributor status update not required.")
    print("Current Status:", current_product[4])


# --------------------------------
# TRANSFER PRODUCT TO RETAILER
# --------------------------------

distributor = web3.eth.accounts[1]
retailer = web3.eth.accounts[2]

current_product = contract.functions.getProduct(1).call()

if (
    current_product[3].lower() == distributor.lower()
    and current_product[4] == "In Transit"
):

    print("\nTransferring product to Retailer...")
    print("Distributor:", distributor)
    print("Retailer:", retailer)

    transaction_hash = contract.functions.transferProduct(
        1,
        retailer
    ).transact({
        "from": distributor
    })

    receipt = web3.eth.wait_for_transaction_receipt(
        transaction_hash
    )

    print("Product transferred to Retailer successfully!")
    print("Transaction Hash:", transaction_hash.hex())
    print("Block Number:", receipt.blockNumber)

    transferred_product = contract.functions.getProduct(1).call()

    print("New Owner:", transferred_product[3])

else:
    print("\nRetailer transfer not required.")
    print("Current Owner:", current_product[3])


# --------------------------------
# RETAILER UPDATES FINAL STATUS
# --------------------------------

retailer = web3.eth.accounts[2]

current_product = contract.functions.getProduct(1).call()

if (
    current_product[3].lower() == retailer.lower()
    and current_product[4] == "In Transit"
):

    print("\nRetailer updating status to Available for Sale...")

    transaction_hash = contract.functions.updateStatus(
        1,
        "Available for Sale"
    ).transact({
        "from": retailer
    })

    receipt = web3.eth.wait_for_transaction_receipt(
        transaction_hash
    )

    print("Final status updated successfully!")
    print("Transaction Hash:", transaction_hash.hex())
    print("Block Number:", receipt.blockNumber)

    final_product = contract.functions.getProduct(1).call()

    print("\n================================")
    print("       FINAL PRODUCT STATE")
    print("================================")
    print("Product ID:", final_product[0])
    print("Name:", final_product[1])
    print("Origin:", final_product[2])
    print("Current Owner:", final_product[3])
    print("Status:", final_product[4])
    print("Timestamp:", final_product[5])

else:
    print("\nRetailer status update not required.")
    print("Current Status:", current_product[4])