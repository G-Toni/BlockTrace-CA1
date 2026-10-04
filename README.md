# BlockTrace

## Blockchain-Based Food Traceability System

BlockTrace is a blockchain-based food traceability application developed
for the Distributed Digital Transactions CA1 at CCT College Dublin.

The system demostrate how blockchain technology and smart contracts
can be used to record and verify the movement of food products through
a supply chain.

## Supply Chain

Farmer → Distributor → Retailer → Customer

## Main Feautures

- Register food products
- Store product origin information
- Transfer product custody between blockchain accounts
- Update product status
- Retrieve product information
- Record blockchain transaction events

## Technologies

- Solidity
- Remix IDE
- Ganache
- Python
- Web3.py
- Shell Script
- GitHub

The smart contract will provide the following main functions:

- registerProduct()
- transferProduct()
- updateStatus()
- getProduct()

## Local Blockchain Testing with Ganache

BlockTrace was tested using Ganache as a local Ethereum blockchain.

### Configuration
- Ganache CLI: v7.9.2
- RPC URL: http://127.0.0.1:8545
- Chain ID: 1337
- Development Environment: Remix IDE
- Smart Contract: FoodTraceability.sol

### Supply Chain Test

The smart contract was tested through the complete product lifecycle:

1. Farmer registered "Organic Coffee" with origin "Brazil".
2. Farmer updated the product status to "Harvested".
3. Ownership was transferred from the Farmer to the Distributor.
4. Distributor updated the status to "In Transit".
5. Ownership was transferred from the Distributor to the Retailer.
6. Retailer updated the final status to "Available for Sale".

The test confirmed that only the current owner could transfer the product or update its status.

## Project Status

Development in progress.

## Academic Project

Module: Distributed Digital Transactions

Programme: BSc (Hons) in Computing in IT

Institution: CCT College Dublin

Assignment: CA1









